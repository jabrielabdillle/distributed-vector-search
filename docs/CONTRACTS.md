# Data and API contracts

All schemas carry schema_version. IDs are stable unique UTF-8 strings; map to collision-free int64 IDs for Faiss with a persisted bijection.

Corpus row: doc_id, text, source, content_sha256, metadata. Embedding row: doc_id, vector float32[d], model_revision, preprocessing_revision, generation_id. Reject null, nonfinite, wrong-dimension and zero-norm vectors. Normalize once for cosine; preserve the same vectors across engines.

Generation manifest: corpus/model/tokenizer/config hashes, dimension, dtype, normalization, count, shard count, partition algorithm, shard artifact URIs/hashes/counts, codebook hash when applicable, code commit and creation UTC. Counts must reconcile and IDs must appear exactly once.

POST /search accepts query vector or text, k, generation_id and deadline_ms; validate size limits. Response includes ranked IDs/scores, generation_id, complete flag, shards_expected/received and timing breakdown. Higher score always means better; adapters convert distance conventions explicitly. Stable ID ordering resolves ties. Do not conflate squared L2, L2, cosine distance and inner product.

Benchmark row: run_id, engine/version, algorithm, config hash, hardware profile, generation, seed, query_id, duration_ns, result IDs, error/timeout and returned count. Summary references raw row checksum and records sample counts, repeats and exclusions. Timeouts remain in error and throughput accounting.
