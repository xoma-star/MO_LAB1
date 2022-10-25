from scipy.optimize import minimize_scalar
from functions import f, fdx1, fdx2

k = 0
M = 1000
e = 0.01
x1, x2 = 0., 0.
lmd_ = 0
x1_new, x2_new = 0., 0.
x11_new, x21_new = 0., 0.
x1_prev, x2_prev=0.,0.

omega=0.
while k + 1 <= M:
    lmd = minimize_scalar(lambda l: f(x1 - l * (fdx1(x1, x2) + omega * lmd_), x2 - l * (fdx2(x1, x2) + omega * lmd_)))
    lmd = float(lmd.x)
    x1_new = x1 - lmd * fdx1(x1, x2)
    x2_new = x2 - lmd * fdx2(x1, x2)
    norm = (fdx1(x1, x2) ** 2 + fdx2(x1, x2) **2 ) ** (1/2)

    if norm < e:
        break

    k += 1
    x1_prev = x1
    x2_prev = x2
    x1 = x1_new
    x2 = x2_new
    lmd_=lmd

    omega=((fdx1(x1, x2) ** 2 + fdx2(x1, x2) ** 2) ** (1/2)) / (fdx1(x1_prev, x2_prev) ** 2 + fdx2(x1_prev, x2_prev) ** 2) ** (1/2)
print("Метод сопряженных градиентов:")
print(round(x1_new, 3), round(x2_new, 3))
print("k = ",k)
