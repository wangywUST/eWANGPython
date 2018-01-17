import datetime
import sys
sys.path.append("Functions")
from cvxForGraphLearning import *
from objValue import *
from ADMMSolver import *
import numpy as np

#Random Seed
np.random.seed(3)

#Variable Dimension
N = 500

#Penalty Weight
a = 0.3

#Generate binary symmetric off-diagonal random matrix A
A = np.random.randint(low = 0, high = 2, size = (N, N))
A[np.tril_indices(N)] = np.transpose(A)[np.tril_indices(N)]
A[np.diag_indices(N)] = 0

#Generate parameter K = S + H with S being sample covariance matrix and H being transform matrix
S = np.identity(N)
H = a * (2 * np.identity(N) - np.ones((N, N)))
K = S + H

#ThetaCVX
# CVXa = datetime.datetime.now()
# ThetaCVX = cvxSolver(A, K)
# CVXb = datetime.datetime.now()
# objValueCVX = objValue(ThetaCVX, K)

#ADMM
rho = 1
ADMMa = datetime.datetime.now()
ThetaADMM = ADMMSolver(A, K, rho)
ADMMb = datetime.datetime.now()
objValueADMM = objValue(ThetaADMM, K)

# print(CVXb - CVXa)
print(ADMMb - ADMMa)
# print(objValueCVX)
print(objValueADMM)