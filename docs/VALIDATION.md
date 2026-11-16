# Validation plan

Unit checks: vector validation, metric conversion, stable ties, ID bijection and exact recall calculation. Property checks: shard partition completeness/disjointness and exact distributed merge equivalence. Integration checks: index persistence, engine parity, retries, generation cutover, rollback, missing shards and deadlines. Spark tests must exercise retried partitions without duplicate committed IDs.

GPU acceptance requires observed assigned-device execution and measured throughput/peak memory; merely importing CUDA libraries does not count. Validate numerical drift and recall before permitting mixed precision. Report deterministic seed control without promising bitwise GPU determinism.

CI should run small CPU fixtures without secrets. Heavy benchmark and GPU jobs are explicit bounded runs, not required on every documentation PR. M0 chooses toolchain versions; lockfiles and container digests follow successful compatibility checks.

Documentation bootstrap checks: required files present, relative markdown links resolve, no claims of measured outcomes, no credentials or generated data included.
