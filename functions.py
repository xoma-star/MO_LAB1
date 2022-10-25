def f(x1, x2):
  return (x1 + x2) ** 2 + (x2 - 1.) ** 2
def fdx1(x1, x2):
  return 2. * (x1 + x2)
def fdx2(x1, x2):
  return 2. * (x1 + 2 * x2 - 1)
def fdx1dx1():
  return 2
def fdx2dx2(): 
  return 4
def fdx1dx2(): 
  return 2