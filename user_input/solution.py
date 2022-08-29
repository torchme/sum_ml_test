"""
Author: Kartushov Danil

"""
from typing import Union, List
import numpy as np

def cumulative_gain(rel: Union[float, int], k: int = None) -> float:
    """
    Score is cumulative gain at k (CG@k)

    Parameters
    ----------
    rel:  numpy array
        Ground truth (true relevance labels).
    k : int
        Rank.

    Returns
    -------
    score : float
    """

    if k is None:
        k = len(rel)
    if (len(rel) >= k )and (k > 0):
        rel = np.asfarray(rel)
        return np.sum(rel[:k])
    else:
        raise ValueError(f"Argument k must be less then rel size: {len(rel)} and more then 0")


def discounted_cumulative_gain(rel: Union[float, int], k: int = None, method=0) -> float:
    """
    Score is discounted cumulative gain at k (DCG@k)

    Parameters
    ----------
    rel:  numpy array
        Ground truth (true relevance labels).
    k : int
        Rank.
    method: bool

        0 - linear, accumulated at a particular rank position p is given by
        sum((rel_i)/log_2(i+1))

        1 - exponential, stronger emphasis on retrieving relevant documents is given by
        sum((2**rel_i -1)/log_2(i+1))

    Returns
    -------
    score : float
    """

    if k is None:
        k = len(rel)

    if (len(rel) >= k) and (k > 0):
        rel = np.asfarray(rel[:k])
        if method == 0:
            return np.sum(rel / np.log2(np.arange(2, rel.size + 2)))
        elif method == 1:
            return np.sum((2**rel - 1) / np.log2(np.arange(2, rel.size + 2)))
        else:
            raise ValueError("Method must be bool 0 or 1 / False or True")
    else:
        raise ValueError(f"Argument k must be less then rel size: {len(rel)} and more then 0")


def ideal_discounted_cumulative_gain(rel: Union[float, int], k: int = None, method=0) -> float:
    """
    Score is ideal discounted cumulative gain at k (IDCG@k)

    Parameters
    ----------
    rel:  numpy array
        Ground truth (true relevance labels).
    k : int
        Rank.
    method: bool

        0 - linear, accumulated at a particular rank position p is given by
        sum((rel_i)/log_2(i+1))

        1 - exponential, stronger emphasis on retrieving relevant documents is given by
        sum((2**rel_i -1)/log_2(i+1))

    Returns
    -------
    score : float
    """

    return discounted_cumulative_gain(
        sorted(np.asfarray(rel), reverse=True), k=k, method=method
    )


def normalized_discounted_cumulative_gain(rel: Union[float, int], k: int = None, method=0) -> float:



    """
    Score is normalized discounted cumulative gain at k (NDCG@k)

    Parameters
    ----------
    rel:  numpy array
        Ground truth (true relevance labels).
    k : int
        Rank.
    method: bool

        0 - Linear, accumulated at a particular rank position p is given by
        DCG=sum((rel_i)/log_2(i+1))

        1 - Exponential, stronger emphasis on retrieving relevant documents is given by
        DCG=sum((2**rel_i -1)/log_2(i+1))

    Returns
    -------
    score : float
    """
    dcg = discounted_cumulative_gain(rel=rel, k=k, method=method)
    idcg = ideal_discounted_cumulative_gain(rel=rel, k=k, method=method)
    return dcg / idcg

def average_ndcg_across_users(quary_scores: List[Union[float, int]], k: int = None, method=0) -> float:
    """
    Score is average normalized discounted cumulative gain at k (NDCG@k) across_users

    Parameters
    ----------
    rel:  numpy array
        Ground truth (true relevance labels).

    Returns
    -------
    score : float
    """

    return np.mean(list(map(lambda quary: normalized_discounted_cumulative_gain(quary, k=k, method=method), quary_scores)))

if __name__ == '__main__':
    pass