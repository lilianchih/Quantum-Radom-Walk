import numpy as np
from math import sqrt
import matplotlib.pyplot as plt

mixing_operator = (1/sqrt(2)) * np.array([[1., 1.], [1., -1.]])
initial_state = np.array([1/sqrt(2), -1/sqrt(2)])
initial_position = 0
def U(state, step):
    t = len(state)
    for j in range(t/2-step+1, t/2+step):
        state[j] = np.dot(mixing_operator, state[j])
    temp = np.copy(state)
    for j in range(t/2-step+1, t/2+step):
        state[j-1][1] += temp[j][1]
        state[j][1] -= temp[j][1]
        state[j+1][0] += temp[j][0]
        state[j][0] -= temp[j][0]
total_steps = [10, 50, 100, 500, 1000, 5000, 10000]
distance = []
for ts in total_steps:
    psi = []  # spin states tensor-product spacial states
    for i in range(2 * ts + 1):
        psi.append(np.array([0., 0.]))
    psi[ts] = np.copy(initial_state)

    for i in range(ts):
        U(psi, i + 1)

    x = []
    prob = []
    for i in range(2 * ts + 1):
        p = (psi[i][0]) ** 2 + (psi[i][1]) ** 2
        if p != 0:
            x.append((i - ts)*1000/ts)
            prob.append(p*sqrt(ts))
    plt.plot(x, prob)
    rms = 0
    for i in range(len(x)):
        rms += x[i] ** 2 * prob[i]
    rms = sqrt(rms)
    distance.append(rms)
plt.show()

plt.plot(total_steps, distance)
plt.show()
