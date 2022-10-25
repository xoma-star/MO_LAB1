import numpy as np
from functions import fdx1dx1, fdx1dx2, fdx2dx2, fdx1, fdx2, f


def nabla(x1, x2):
  return np.array([fdx1(x1, x2), fdx2(x1, x2)])


def hess():
  return np.array([[fdx1dx1(), fdx1dx2()], [fdx1dx2(), fdx2dx2()]])


def MarquardtMethod(x_0, lambda_0=10e4, e=1e-3, M=1000):
  k = 0
  x1_prev = x_0[0]
  x2_prev = x_0[1]
  x1 = x1_prev
  x2 = x2_prev
  lambda_k = lambda_0
  norm = np.linalg.norm(nabla(x1, x2), ord=2)
  while k <= M:
    k += 1
    d_k = np.dot(-np.linalg.inv(hess() + lambda_k * np.eye(2)), nabla(x1_prev, x2_prev))
    x1 = x1_prev + d_k[0]
    x2 = x2_prev + d_k[1]
    norm = np.linalg.norm(nabla(x1, x2), ord=2)

    print(f"Step {k}, x1: {round(x1, 2)}, x2: {round(x2, 2)}, norm: {round(norm, 5)}")
    
    if norm < e:
      break

    if f(x1, x2) < f(x1_prev, x2_prev):
      lambda_k *= 0.5
    else:
      lambda_k *= 2
  return {x1, x2, k}
