# Dependency-ordered milestones

M0a CPU synthetic feasibility slice completed; original full M0 and downstream scientific milestones remain pending. W1 free hosted dashboard is an independent usability milestone.

| Milestone | Deliverable and acceptance | Depends on |
|---|---|---|
| M0 | Inventory CPU/RAM/GPU/CUDA/Java/Docker; pin compatible versions and model/dataset revisions; tiny embedding + exact-search proof; document GPU availability | None |
| M1 | Versioned corpus/embedding schemas, checksum manifests, deterministic splits; reject invalid vectors and duplicate IDs | M0 |
| M2 | Spark batch embedding pipeline; bounded worker memory, retry-safe outputs, count reconciliation; CPU and actual GPU evidence separately | M1 |
| M3 | Single-node exact/HNSW/IVF-PQ builders; persistence round trip; held-out recall and artifact memory measurements | M1 |
| M4 | Shard servers/coordinator; global merge correctness, timeout behavior, generation pinning, cutover and rollback | M3 |
| M5 | pgvector/OpenSearch adapters; identical corpus/vector hashes, metric semantics and verified index usage | M3 |
| M6 | Reproducible benchmark harness; raw per-query data, resource measurements, warm/cold distinction, repeated trials | M4,M5 |
| M7 | Bounded Spark/GPU scale experiment and sharding sweep; failure/restart proof; no fabricated distributed/GPU claims | M2,M6 |
| M8 | Reproducible report and optional static explorer; every chart traces to evidence; clean-room reproduction and operations handoff | M7 |

If GPU unavailable, complete CPU-ready tasks while recording M2/M7 GPU acceptance as blocked. A CPU-only report is explicitly partial completion.

## Analytical execution order
Follow docs/STUDY.md: M0 → M1 → M3 → a single-node slice of M6 → M5 → M4 → remaining M6 → M2/M7 → M8. The early M6 slice only measures exact versus HNSW/IVF-PQ and does not mark the full comparative harness complete. Record the research question and interview takeaway at each milestone.
