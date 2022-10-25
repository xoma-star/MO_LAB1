from scipy.optimize import minimize_scalar
from functions import f, fdx1, fdx2

def ConjugateGradientMethod(M = 1000, e = 1e-3):
  omega = 0.
  k = 1
  x1, x2 = 0., 0.
  lmd_ = 0
  while k <= M:
    lmd = minimize_scalar(lambda l: f(x1 - l * (fdx1(x1, x2) + omega * lmd_), x2 - l * (fdx2(x1, x2) + omega * lmd_)))
    lmd = float(lmd.x)
    x1_new = x1 - lmd * fdx1(x1, x2)
    x2_new = x2 - lmd * fdx2(x1, x2)
    norm = (fdx1(x1, x2) ** 2 + fdx2(x1, x2) **2 ) ** (1/2)

    print(f"Step {k}, x1: {round(x1, 2)}, x2: {round(x2, 2)}, norm: {round(norm, 5)}")
    if norm < e:
        break
    k += 1
    x1_prev = x1
    x2_prev = x2
    x1 = x1_new
    x2 = x2_new
    lmd_ = lmd

    omega=((fdx1(x1, x2) ** 2 + fdx2(x1, x2) ** 2) ** (1/2)) / (fdx1(x1_prev, x2_prev) ** 2 + fdx2(x1_prev, x2_prev) ** 2) ** (1/2)
  return {x1: x1_new, x2: x2_new, k: k}