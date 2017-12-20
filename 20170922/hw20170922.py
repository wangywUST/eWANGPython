from cvxpy import *
from numpy import *
import matplotlib.pyplot as plt
# Problem data.

A = semidefinite(2)
b = Variable(2)
x1 = array([0.55, 0])
x2 = array([0.25, 0.35])
x3 = array([-0.2, 0.2])
x4 = array([-0.25, -0.1])
x5 = array([0, -0.3])
x6 = array([0.4, -0.2])
x7 = array([0.2, 0.4])
x8 = array([0.2, 0.2])
x9 = array([-1, -1])


objective = Minimize(-log_det(A))
constraints = [norm(A * (x1) - b , 2) <= 1,
               norm(A * (x2) - b , 2) <= 1,
               norm(A * (x3) - b , 2) <= 1,
               norm(A * (x4) - b , 2) <= 1,
               norm(A * (x5) - b , 2) <= 1,
               norm(A * (x6) - b , 2) <= 1,
               norm(A * (x7) - b , 2) <= 1,
               norm(A * (x8) - b , 2) <= 1,
               norm(A * (x9) - b, 2) <= 1]
prob = Problem(objective, constraints)
prob.solve()

A = A.value.I
xc = A * b.value

u1 = 0.01 * array(range(-100, 101))
u2 = sqrt(1 - u1**2)

u3 = 0.01 * array(range(-100, 101))
u4 = -sqrt(1 - u3**2)

r1 = zeros(201)
r2 = zeros(201)
r3 = zeros(201)
r4 = zeros(201)

print(A.shape)
print(xc + dot(A, array([u1[0], u2[0]])).T)
for i in range(0, 201):
    r1[i] = (xc + dot(A, array([u1[i], u2[i]])).T)[0]
    r2[i] = (xc + dot(A, array([u1[i], u2[i]])).T)[1]
    r3[i] = (xc + dot(A, array([u3[i], u4[i]])).T)[0]
    r4[i] = (xc + dot(A, array([u3[i], u4[i]])).T)[1]

print(u3)
print(r4)

plt.plot(x1[0], x1[1], 'ro')
plt.plot(x2[0], x2[1], 'ro')
plt.plot(x3[0], x3[1], 'ro')
plt.plot(x4[0], x4[1], 'ro')
plt.plot(x5[0], x5[1], 'ro')
plt.plot(x6[0], x6[1], 'ro')
plt.plot(x7[0], x7[1], 'ro')
plt.plot(x8[0], x8[1], 'ro', label = 'point sets need to be covered')
plt.plot(x9[0], x9[1], 'ro')
plt.plot(xc[0], xc[1], 'yo', label = 'the closest point')
plt.plot(r1, r2, 'b-')
plt.plot(r3, r4, 'b-', label = "the ellipsoid")
plt.legend(loc='lower right')
plt.show()