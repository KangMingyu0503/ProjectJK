# 모듈을 사용하여 제작
from sympy import symbols, Eq, solve
import sympy
a, b, c, d, e, f = map(int, input().split())
x, y = sympy.symbols('x y')
eq1 = Eq((a*x) + (b*y), c)
eq2 = Eq((d*x) + (e*y), f)
solution = solve((eq1, eq2), (x, y))
x_solution = int(solution[x])
y_solution = int(solution[y])
print(x_solution,y_solution)
