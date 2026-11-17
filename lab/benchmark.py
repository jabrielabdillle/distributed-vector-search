"""Run: python -m lab.benchmark --output reports/cpu-smoke.json"""
import argparse, hashlib, json, platform, time
from pathlib import Path
import faiss
import numpy as np
import psutil
from .core import normalize, exact_neighbors, recall

def run(config):
    faiss.omp_set_num_threads(config['threads'])
    rng = np.random.default_rng(config['seed'])
    n,d,nq = config['corpus_count'],config['dimension'],config['query_count']
    centers = normalize(rng.normal(size=(64,d)))
    corpus = normalize(centers[rng.integers(64,size=n)] + rng.normal(0,.18,(n,d)))
    queries = normalize(centers[rng.integers(64,size=nq)] + rng.normal(0,.18,(nq,d)))
    truth = exact_neighbors(corpus, queries, config['k'])
    rows, summaries = [], []
    for spec in config['configs']:
        before = time.perf_counter()
        if spec['type']=='flat': index=faiss.IndexFlatIP(d)
        elif spec['type']=='hnsw':
            index=faiss.IndexHNSWFlat(d,16,faiss.METRIC_INNER_PRODUCT)
            index.hnsw.efConstruction=80
            index.hnsw.efSearch=spec['ef']
        else:
            index=faiss.IndexIVFPQ(faiss.IndexFlatIP(d),d,64,8,8,faiss.METRIC_INNER_PRODUCT)
            index.cp.seed=config['seed']
            index.train(corpus)
            index.nprobe=spec['nprobe']
        index.add(corpus)
        build_ms=(time.perf_counter()-before)*1000
        packed=faiss.serialize_index(index)
        loaded=faiss.deserialize_index(packed)
        assert np.array_equal(index.search(queries[:5],10)[1],loaded.search(queries[:5],10)[1])
        del loaded
        for q in queries[:20]: index.search(q.reshape(1,-1),config['k'])
        own=[]
        for repeat in range(config['repeats']):
            for qi in rng.permutation(nq):
                start=time.perf_counter_ns()
                _, ids=index.search(queries[qi:qi+1],config['k'])
                elapsed=(time.perf_counter_ns()-start)/1e6
                row={'config':spec['name'],'repeat':repeat,'query_id':int(qi),'latency_ms':elapsed,'recall':recall(truth[qi],ids[0]),'result_ids':ids[0].tolist()}
                own.append(row);rows.append(row)
        lat=[x['latency_ms'] for x in own]
        summaries.append({'name':spec['name'],'algorithm':spec['type'],'recall':float(np.mean([x['recall'] for x in own])),'p50_ms':float(np.percentile(lat,50)),'p95_ms':float(np.percentile(lat,95)),'p99_ms':float(np.percentile(lat,99)),'index_bytes':len(packed),'process_rss_bytes':psutil.Process().memory_info().rss,'build_ms':build_ms,'queries':len(own)})
        del index,packed
    return {'schema_version':1,'source':'measured','corpus_source':'synthetic clustered normalized vectors','hardware':{'platform':platform.platform(),'cpu_count':psutil.cpu_count(),'ram_bytes':psutil.virtual_memory().total,'faiss':faiss.__version__},'config':config,'corpus_sha256':hashlib.sha256(corpus.tobytes()).hexdigest(),'queries_sha256':hashlib.sha256(queries.tobytes()).hexdigest(),'summaries':summaries,'queries':rows,'limitations':['CPU single-process warm sequential search; no network or embedding latency.','Synthetic vectors, not a real text corpus or semantic relevance evaluation.','Serialized index bytes are not total serving RAM. RSS includes shared corpus and ground truth; not isolated per-engine peak memory.','Fixed preregistered configurations; no tuning on test queries.','Three timing repeats reuse the same index and queries; not independent build seeds.']}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',required=True);args=parser.parse_args()
    out=Path(args.output)
    if out.exists(): raise SystemExit('Output exists; use a fresh evidence path')
    cfg=json.loads(Path('configs/smoke.json').read_text())
    result=run(cfg);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summaries'],indent=2))
