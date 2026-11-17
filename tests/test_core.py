import numpy as np
import pytest
from lab.core import normalize, exact_neighbors, recall

@pytest.mark.parametrize('value', [[[0,0]],[[float('nan'),1]],[],[1,2]])
def test_bad_vectors(value):
    with pytest.raises(ValueError): normalize(value)

def test_exact_hand_computed_and_ties():
    x=normalize([[1,0],[1,0],[0,1],[-1,0]])
    assert exact_neighbors(x,normalize([[1,0]]),3).tolist()==[[0,1,2]]

def test_duplicate_results_do_not_inflate_recall():
    assert recall([1,2,3],[1,1,1])==pytest.approx(1/3)

def test_normalization_does_not_mutate():
    x=np.array([[3,4]],dtype=np.float32);y=normalize(x)
    assert np.allclose(y,[[.6,.8]]) and np.array_equal(x,[[3,4]])
