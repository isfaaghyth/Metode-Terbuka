# Muh Isfahani Ghiyath
# func : 3 - (6 * x) / x^2
import math

def g(x):
    return (3 - (6 * float(x))) / (float(x) * float(x))
    # return (3 - (float(x) * float(x))) / 2

xi = input("x : ")
xi_temp = 0

for x in range(0, 1000):
    print "i = ", x, " xi = ", xi, " g(xi) = ", g(xi)
    xi = g(xi)

# nothing to lus
# while True:
#     xi_temp = xi
#     print "i = ", i, " xi = ", xi, " g(xi) = ", g(xi), "abs : ", abs(xi_temp - xi)
#     xi = g(xi)
#     i = i + 1
#     if (abs(xi_temp - xi) < (10 ** -16)): break
