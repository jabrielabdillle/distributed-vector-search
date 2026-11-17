# ML systems trade-off study

## Question and tangible example
A search service must return similar documents quickly without using excessive RAM. When is it worth sacrificing some nearest-neighbor accuracy to reduce latency or memory? The deliverable is a reproducible recommendation for a stated workload and hardware budget, not a universal winning engine.

Use one redistributable text corpus selected and pinned in M0. Encode it with one fixed model. A small interactive document search can make the result tangible; the experimental report remains the primary deliverable. Synthetic vectors are correctness fixtures, not substitutes for the real-data result.

## Work backwards
Final decision: identify configurations satisfying a declared minimum recall and maximum p95 latency/memory budget. Report no feasible configuration when appropriate. Among feasible configurations compare throughput, memory, build cost and operational complexity. Declare budgets after hardware inventory but before test results; record them in versioned experiment configs.

Evidence required: per-query measurements, exhaustive nearest-neighbor ground truth, repeated runs, resource accounting and plots tied to immutable manifests. See BENCHMARKS.md for the binding measurement protocol.

1. Establish exact search as the quality reference and measure its cost.
2. Test HNSW search effort at a fixed build configuration: does extra work improve recall, and what latency does it cost?
3. Test IVF-PQ compression and search effort: how much memory is saved, and what recall is lost? Measure optional exact reranking and include retained-vector memory.
4. Compare engines at matched recall and equal resource limits. Record backend-specific knobs rather than pretending settings are equivalent.
5. Increase corpus size, concurrency and shards in separate controlled experiments. Measure coordinator overhead and tail latency.
6. Evaluate Spark/GPU embedding throughput separately from retrieval. GPU embedding does not imply GPU search.

## Main outputs
Recall versus p95 latency scatter plot; recall versus total serving memory; throughput versus concurrency; build time/index bytes; resource-constrained recommendation table. Include uncertainty, timeouts and failed configurations. A Pareto-efficient point has no measured alternative at least as good on every chosen metric and strictly better on one; uncertainty may prevent declaring dominance.

## Scope boundaries
First implementation is a CPU baseline and small real corpus. GPU and multi-host results require actual hardware evidence. ANN recall measures agreement with exact neighbors; human usefulness needs separate relevance judgments. No evidence yet supports a speedup, savings or accuracy claim.
