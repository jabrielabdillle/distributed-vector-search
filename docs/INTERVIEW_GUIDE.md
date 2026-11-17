# Interview explanation guide

## Thirty-second project pitch (planned, not completed)
I am building an experiment to compare vector search methods. Exact search checks every stored vector and gives the reference neighbors. Approximate indexes search less or compress vectors to save time and memory. I measure what quality is lost, then choose a configuration for a stated performance budget.

## Concepts in plain language
- Embedding: a numerical representation of a document; similar representations can be retrieved by distance or similarity.
- Exact search: compare the query with every vector; our neighbor ground truth.
- HNSW: navigate a graph connecting vectors to find promising neighbors without scanning everything.
- IVF-PQ: search selected clusters and use compressed vector representations, trading accuracy for resource savings.
- Recall@10: how many of the exact top ten neighbors the approximate method returns, averaged over queries.
- p95 latency: the response-time threshold at or below which about 95 percent of measured requests fall.
- Sharding: split the corpus across servers, search each shard and merge results.

## Questions you should be able to answer
Why this baseline? Why this metric? Were every engine's vectors identical? How did you avoid tuning on test queries? What happens when concurrency increases? Did memory measurements include every shard and reranking vectors? What failed? Which conclusion would change on different hardware or data?

## Evidence-based story template
Problem and constraints → simplest baseline → experiment and controls → measured result with uncertainty → trade-off and chosen configuration → limitation and next experiment.

Do not replace placeholders with guessed metrics. Keep actual commands, configs and results in the report. Explain one concrete configuration change before discussing the full architecture. An honest result that compression did not help is still useful if the experiment was sound.
