# CPU feasibility milestone

7 correctness tests pass. Actual Faiss CPU search measured over 10,000 synthetic normalized 64-dimensional vectors, 200 independent queries, six fixed configurations and three timing repeats (3,600 measurements). Index serialization round trips passed for every configuration. See cpu-smoke.json and cpu-queries.csv.

Command: `.venv/bin/python -m pytest -q`; `.venv/bin/python -m lab.benchmark --output <fresh-path>`. Python 3.12/macOS arm64; dependency lock committed. CPU one thread. CUDA GPU, Spark, pgvector and OpenSearch not exercised. M0a is a scoped feasibility slice; original M0 real text embeddings/runtime matrix remains open. Serialized index size is not RAM; process RSS is diagnostic and not an isolated memory comparison.

HNSW ef16 reached 91.35% neighbor recall; ef64 98.9%; IVF-PQ reached 45.8%. These are measurements on synthetic geometry, not semantic relevance or universal performance claims.
