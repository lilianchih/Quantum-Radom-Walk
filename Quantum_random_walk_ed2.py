import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

mixing_operator = (1/sqrt(2)) * np.array([[1., 1.], [1., -1.]])
initial_state = np.array([1/(4-2*sqrt(2)), (-1+sqrt(2))/(4-2*sqrt(2))])
initial_position = 0
total_steps = 1000
psi = [] #spin states tensor-product spacial states
for i in range(2*total_steps + 1):
    psi.append(np.array([0., 0.]))
psi[total_steps] = np.copy(initial_state)

def U(state, step):
    """spin-dependent unitary walking operator
    :type state: a list of np arrays
    """
    t = len(state)
    for j in range(t/2-step+1, t/2+step):
        state[j] = np.dot(mixing_operator, state[j])
    temp = np.copy(state)
    for j in range(t/2-step+1, t/2+step):
        state[j-1][1] += temp[j][1]
        state[j][1]  -= temp[j][1]
        state[j+1][0] += temp[j][0]
        state[j][0] -= temp[j][0]

for i in range(total_steps):
    U(psi, i+1)

x = []
prob = []
for i in range(2*total_steps+1):
    x.append(i - total_steps)
    prob.append((psi[i][0])**2 + (psi[i][1])**2)

deviation = 0
mean = 0
rms = 0 #root-mean-square distance
for i in range(2*total_steps+1):
    rms += x[i]**2 * prob[i]
    mean += x[i] * prob[i]
rms = sqrt(rms)

print rms
print mean

plt.plot(x, prob)
plt.show()
