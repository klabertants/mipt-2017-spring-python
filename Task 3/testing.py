import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
from statsmodels.nonparametric.kde import KDEUnivariate

sample = np.array([1, 2, 3])

ecdf = ECDF(sample)
grid = np.linspace(0, 3, 3)

print(ecdf(grid))
