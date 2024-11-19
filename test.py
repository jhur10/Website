#If we list all the natural numbers below 10
# that are multiples of 3 or 5, we get 3, 5, 6, and 9.
# The sum of these multiples is 23.
# Fnd the sum of all the multiples
# of 3 or 5 below 1000.
# (Correct answer: 233168)
import math as Math
def multiples(x, y, max):
    m = []
    xi = Math.floor(max / x)
    yi = Math.floor(max / y)
    for i in range(1, xi):
        m.append(i*x)
        print(i)
    for j in range (1, yi):
        if (j % x) != 0:
            m.append(j*y)
    return m
def main():
    m = multiples(3, 5, 1000)
    print ("Sum: ", sum(m))
main()