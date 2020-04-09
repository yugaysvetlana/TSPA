from math import *
import matplotlib.pyplot as plt

def nearest_neighbor(x_i, i, m):
    index = N + 1
    value = N + 1
    for ind in range(i + 1, N - m):
        x_ind = ts[ind : ind + m]
        if (distance(x_i, x_ind, m) < value):
            index = ind
            value = distance(x_i, x_ind, m)
    return index, value

def distance(w_i, w_j, m):
    sum = 0
    for i in range(m):
        sum += ((w_i[i][0] - w_j[i][0])**2 + (w_i[i][1] - w_j[i][1])**2)/m
    return sqrt(sum)

N = 10000
dt = 1.334
t = 0.01
ts = [[cos(dt * i + t), sin(dt * i + t)] for i in range(1, N + 2)]
m = 1
G = {}

for m in range (1, 20):
    neighbor = 0
    for i in range(N - m - 1):
        x_i_cur = ts[i : i + m]
        ind, nearest = nearest_neighbor(x_i_cur, i, m)
        x_ind_cur = ts[ind : ind + m]
        cur_dist = distance(x_i_cur, x_ind_cur, m)
        x_i_next = ts[i : i + m + 1]
        x_ind_next = ts[ind : ind + m + 1]
        next_dist = distance(x_i_next, x_ind_next, m + 1)
        if (next_dist / cur_dist) > (m / (m + 1)) * nearest:
            neighbor += 1
    G[m] = neighbor
    print(G[m])
    
L = list(G.items())
x, y = zip(*L)
plt.plot(x, y)
plt.show()
