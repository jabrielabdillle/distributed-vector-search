# Distributed Vector Search Lab

An agent-ready blueprint for batch embedding generation with Spark and GPU workers, sharded approximate nearest-neighbor search, and reproducible comparisons against pgvector and OpenSearch.

Status: design only. No pipeline, GPU run, benchmark result or deployed service is claimed.

## Work backwards from the deliverable
The final artifact is a reproducible report showing recall–latency–memory Pareto frontiers for identical vectors, queries, hardware budgets and retrieval semantics. Every plotted point links to raw measurements, configuration, code revision and dataset checksums. An operator can rebuild a generation, query it across shards, reproduce a benchmark and roll back safely.

## Proposed stack
Python, PySpark, PyTorch/Sentence Transformers, Parquet, Faiss, FastAPI, PostgreSQL/pgvector, OpenSearch, Docker Compose and pytest. Pin versions only after M0 compatibility checks. Start with CPU HNSW; add IVF-PQ and CUDA embedding workers as independently validated paths.

Read [agent instructions](AGENTS.md), [memory](MEMORY.md), [architecture](docs/ARCHITECTURE.md), [benchmark protocol](docs/BENCHMARKS.md) and [milestones](docs/BACKLOG.md). All design defaults are revisable through a recorded decision.

No paid infrastructure is authorized. Local execution is the default. Static reports may later be hosted free; Spark, GPU workers and database services cannot run on GitHub Pages.
