from skmultiflow.clustering.sphere_cluster import SphereCluster
from abc import ABCMeta, abstractmethod


class CFCluster(SphereCluster, metaclass=ABCMeta):
    """CFCluster

    Cluster feature is a triple summarizing, which is maintained
    about a cluster.
    It is a triple  vector, which  include the number of the data
    points, the linear sum of data points, and  the  squared  sum
    of them [1]_.
                CF = (N,:math:`\vect(LS)`, SS)
    * N is the number of data points in a cluster
    * :math:`\vect(LS) = \sum^{N}_{i=1} \vect(X_i)` is the linear
      sum of the N data points
    * SS = :math:`\sum^{N}_{i=1} X_i ^ 2` is the square sum of
      data points

    References
    ----------
    .. [1] A. Amini, T. Ying Wah. Density Micro-Clustering Algorithms on Data
       Streams: A Review.


    """

    def __init__(self, X=None, weight=None, dimensions=None, cluster=None):
        super().__init__()

        if X is None and weight is None and cluster is None and dimensions is not None:
            self.N = 0
            self.LS = [0.0] * dimensions
            self.SS = [0.0] * dimensions
        elif X is not None and weight is not None and dimensions is not None:
            self.N = 1
            self.LS = []
            self.SS = []
            for i in range(len(X)):
                self.LS.append(X[i]*weight)
                self.SS.append(X[i]*X[i]*weight)
        elif cluster is not None:
            self.N = cluster.N
            self.LS = cluster.LS.copy()
            self.SS = cluster.SS.copy()

    def add(self, cluster):
        self.N += cluster.N
        self.add_vectors(self.LS, cluster.LS)
        self.add_vectors(self.SS, cluster.SS)

    @abstractmethod
    def get_CF(self):

        raise NotImplementedError

    def get_inclusion_probability(self, X, weight):

        raise NotImplementedError

    def get_radius(self):

        raise NotImplementedError

    def get_weight(self):
        return self.N

    @staticmethod
    def add_vectors(v1, v2):
        assert v1 is not None
        assert v2 is not None
        assert len(v1) == len(v2)
        for i in range(len(v1)):
            v1[i] += v2[i]




