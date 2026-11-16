# Benchmark protocol

## Acceptance evidence
Produce comparable recall@10, latency p50/p95/p99, completed QPS, error/timeout rate, index bytes, steady and peak process/container memory, build time and embedding throughput. Report GPU memory separately from host RAM and disk. No target speedup is promised.

Generate exact ground truth with blocked exhaustive float32 inner-product search on the same normalized corpus. Keep query IDs separate from corpus IDs; define self-match exclusion before evaluating. Ground truth ties use stable document IDs. Recall@k is mean intersection size divided by k (or eligible corpus size if smaller); test set requires at least k eligible items. Validate against a tiny hand-computable fixture.

Split corpus training samples, development queries and held-out test queries deterministically. Fit IVF/PQ only on corpus samples. Tune on development queries; freeze configs before test evaluation. ANN recall measures neighbor agreement, not semantic relevance. Optional relevance labels require a separate nDCG/MRR report.

## Proposed tiers and sweeps
Smoke: 10k vectors/200 queries. Standard: 100k/2k. Scale: 1M/10k only after memory admission. These are planned sizes, not completed runs. Include clustered synthetic fixtures and one redistributable real text corpus selected in M0 with license/checksum review.

HNSW sweep M, efConstruction and efSearch; IVF-PQ sweep nlist, nprobe, subquantizers and code bits subject to dimension divisibility and sufficient training samples. Shards 1/2/4; concurrency 1/8/32 where resource budget permits. Avoid an unbounded Cartesian product: coarse development sweep, then preregister a small finalist set.

Compare Faiss HNSW/IVF-PQ, pgvector exact/HNSW/IVFFlat where supported, and OpenSearch documented vector engines. Do not claim all engines support the same compression. Hold corpus, vectors, distance, k, filters and resource limits constant. Record versions, index settings, replicas, segments, thread counts and query plans. Verify index usage. Run engines separately on the same host to prevent interference.

Run warmup separately; cold and warm measurements are separate experiments. Measure retrieval-only with precomputed query vectors and end-to-end text query latency separately. Use fixed request traces and documented arrival process; record queueing and client backpressure to avoid coordinated omission. Repeat at least three times, retain distributions and uncertainty, and never average percentile values as pooled percentiles. Include all coordinator/shard/container memory, aggregate concurrent peaks, and note cache accounting limitations.

Choose Pareto-efficient configs at matched recall; publish raw logs and failures. Multi-host scaling claims require actual multi-host evidence and network topology.
