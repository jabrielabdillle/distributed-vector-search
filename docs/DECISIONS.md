# Decision log

2026-11-16 — Initial design defaults, pending feasibility validation:
- Faiss HNSW first, IVF-PQ second: establish an uncompressed reference before compression tradeoffs.
- Shared IVF/PQ training artifact across shards: prevent independently trained incompatible quantization spaces from silently changing comparisons.
- Immutable generations: reproducible measurements and atomic rollback.
- Cosine through normalized float32 vectors and inner product: one canonical geometry with explicit adapter conversions.
- Local open-source execution: no paid infrastructure authorization; GPU access is a measured prerequisite.
- Private bootstrap repository: publication audience can be changed by explicit user direction.

Record future decisions with context, alternatives, consequences and evidence; do not silently rewrite historical benchmark conditions.

2026-11-16 — User selected ML systems trade-off analysis. Start with a comprehensible single-machine benchmark, then scale. Preserve Spark/GPU and sharding as later milestones. Optimize the explanation and evidence quality, not the number of technologies.
