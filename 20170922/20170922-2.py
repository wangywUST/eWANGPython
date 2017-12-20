from cvxpy import *
from numpy import *
import matplotlib.pyplot as plt
# Problem data.

xc = Variable(2)
r = Variable(1)
x1 = array([0.55, 0])
x2 = array([0.25, 0.35])
x3 = array([-0.2, 0.2])
x4 = array([-0.25, -0.1])
x5 = array([0, -0.3])
x6 = array([0.4, -0.2])
x7 = array([0.2, 0.4])
x8 = array([0.2, 0.2])
x9 = array([-1, -1])

objective = Minimize(r)
constraints = [norm(x1 - xc, 2) <= r,
               norm(x2 - xc, 2) <= r,
               norm(x3 - xc, 2) <= r,
               norm(x4 - xc, 2) <= r,
               norm(x5 - xc, 2) <= r,
               norm(x6 - xc, 2) <= r,
               norm(x7 - xc, 2) <= r,
               norm(x8 - xc, 2) <= r,
               norm(x9 - xc, 2) <= r]
prob = Problem(objective, constraints)
prob.solve()

print(xc.value)

u1 = r.value * 0.01 * array(range(-100, 101))
u2 = sqrt(r.value * r.value - u1**2)

u3 = r.value * 0.01 * array(range(-100, 101))
u4 = -sqrt(r.value * r.value - u3**2)

r1 = zeros(201)
r2 = zeros(201)
r3 = zeros(201)
r4 = zeros(201)

for i in range(0, 201):
    r1[i] = xc.value[0] + u1[i]
    r2[i] = xc.value[1] + u2[i]
    r3[i] = xc.value[0] + u3[i]
    r4[i] = xc.value[1] + u4[i]

plt.plot(x1[0], x1[1], 'ro')
plt.plot(x2[0], x2[1], 'ro')
plt.plot(x3[0], x3[1], 'ro')
plt.plot(x4[0], x4[1], 'ro')
plt.plot(x5[0], x5[1], 'ro')
plt.plot(x6[0], x6[1], 'ro')
plt.plot(x7[0], x7[1], 'ro')
plt.plot(x8[0], x8[1], 'ro', label = 'point sets need to be covered')
plt.plot(x9[0], x9[1], 'ro', label = 'point sets need to be covered')
plt.plot(xc.value[0], xc.value[1], 'yo', label = 'the closest point')
plt.plot(r1, r2, 'b-')
plt.plot(r3, r4, 'b-', label = "the circle")
plt.legend(loc='lower right')
plt.show()

