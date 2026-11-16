# Architecture

Corpus manifest → Spark preprocessing → partition-local embedding inference → validated Parquet embedding generation → index builders → immutable shard artifacts → shard servers → query coordinator → benchmark harness/report.

Spark distributes bounded batches; load one model per worker process, not per row. GPU workers receive explicit scheduler resource assignments. Do not assume CUDA device ordinal equals Spark resource identifier. Validate assignment in M0. CPU fallback is a separate labeled execution profile. Never collect the full embedding corpus onto the driver.

Shard by a documented stable hash of document ID. Coordinator embeds a text query once, fans out to all shards of a pinned generation, merges comparable scores, deduplicates IDs and returns top-k. For exact per-shard search, local top-k is sufficient; ANN candidate overfetch is a tunable approximation. No silent successful response on missing shards: default fail closed, optional explicitly partial diagnostic mode excluded from headline recall.

Build HNSW independently on shards. For IVF-PQ, train a shared coarse quantizer and codebook using a representative deterministic corpus-only sample and distribute the trained artifact before adding shard vectors. Record all training parameters and checksums. Quantized score error remains even with shared training; evaluate optional exact reranking as a separately budgeted configuration.

Publish a manifest only after all shard artifacts validate. Servers load new generations before coordinator cutover; retain the old generation until in-flight requests drain. Local multi-process sharding validates routing, not multi-host performance.
