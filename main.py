from ConjugateGradient import ConjugateGradientMethod
from Marquardt import MarquardtMethod


print("Метод сопряженных градиентов:")
x1, x2, k = ConjugateGradientMethod()
print(f"Solution at step {k}: ({round(x1, 2)}, {round(x2, 2)})")

print("\n\nМетод Марквардта:")
x1, x2, k = MarquardtMethod([0, 0])
print(f"Solution at step {k}: ({round(x1, 2)}, {round(x2, 2)})")