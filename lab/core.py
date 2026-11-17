import numpy as np

def normalize(values):
    x = np.array(values, dtype=np.float32, copy=True)
    if x.ndim != 2 or not x.shape[0] or not x.shape[1] or not np.isfinite(x).all():
        raise ValueError('Expected a nonempty finite matrix')
    norms = np.linalg.norm(x, axis=1, keepdims=True)
    if (norms == 0).any():
        raise ValueError('Zero-norm vectors are not valid')
    return np.ascontiguousarray(x / norms)

def exact_neighbors(corpus, queries, k):
    if not 0 < k <= len(corpus):
        raise ValueError('k must fit corpus')
    # One query at a time bounds score workspace; mergesort preserves ID tie order.
    return np.array([np.argsort(-(corpus @ q), kind='stable')[:k] for q in queries])

def recall(expected, actual):
    if len(expected) == 0:
        raise ValueError('Empty ground truth')
    return len(set(map(int, expected)) & set(map(int, actual))) / len(expected)
