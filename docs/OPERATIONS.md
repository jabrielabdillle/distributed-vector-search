# Operations and recovery

Local development first; container services bind localhost. Resource limits must leave host headroom. Benchmark one engine at a time. Download only allowlisted model/data artifacts with pinned revisions and licenses; do not execute unreviewed remote model code.

For Spark retry/speculation: write attempt-specific outputs, then atomically select committed partitions into the generation manifest. Never append repeated task outputs into the final generation. Validate uniqueness and checksums before indexing.

For worker OOM: preserve failure evidence, lower bounded batch size, rerun under a new configuration identity. For corrupt shard: reject load and retain prior healthy generation. For missing shard: fail the complete-search request within deadline. Use bounded retries within the total deadline, not per-shard deadlines multiplied together.

Retain raw experiment logs and manifests outside Git; commit small summaries and checksums. Delete only explicitly disposable scratch outputs. Do not upload datasets to public hosting without license review. No automatically billed cloud GPU or managed database enrollment.
