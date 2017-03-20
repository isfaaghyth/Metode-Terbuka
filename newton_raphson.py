# Muh Isfahani Ghiyath
# func : x^2 - 2x - 3

def fungsi(x):
    return (float(x) * float(x)) - (2 * float(x)) - 3

def turunanFungsi(x):
    return (2 * float(x)) - 2

def newton(x):
    return x - (fungsi(float(x)) / turunanFungsi(float(x)))

x0 = input("x : ")

for i in range(0, 10):
    print "i : ", i, " newton : ", newton(x0)
    x0 = newton(x0)
