
from fractions import Fraction

x1, y1, x2, y2, x3, y3, type1 = input().split(',')
x1, y1, x2, y2, x3, y3 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3)


if type1 == "3": # парабола
	p = Fraction((y1**2)/(2*x1))
	print("y^2 = 2*"+ str(p) + "*x")

if type1 == "1": # эллипс
	a_sqr = Fraction((x2**2 * y1**2 - x1**2 * y2**2)/(y1**2 - y2**2))
	b_sqr = Fraction(y2**2/(1 - x2**2/a_sqr))
	print(str(1/a_sqr) + "* x^2 + y^2 *"+ str(1/b_sqr) + "=1")

if type1 == "2": # гипербола
	a_sqr = Fraction((-x1**2 * y2**2 + x2**2 * y1**2)/(y1**2 - y2**2))
	b_sqr = Fraction(y2**2/((x2**2/a_sqr)-1))
	print(str(1/a_sqr) + "* x^2 - y^2 *"+ str(1/b_sqr) + "=1")