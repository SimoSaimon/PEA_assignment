import numpy as np
from scipy import linalg

N = 100 # Number of employers in the system
Z = 40 # think time 

# Probability 
P = np.array([[0., 1, 0., 0., 0., 0.],
              [0., 0., 0.35, 0.6, 0., 0.],
              [0., 0., 0., 0., 0.65, 0.35],
              [0., 1, 0., 0., 0., 0.],
              [0., 0.9, 0., 0., 0., 0.1],
              [0., 0.1, 0., 0., 0.9, 0.],])

l = np.zeros(6) 
l[0]= 1
I = np.eye(6)
p= linalg.solve((I-P).T, l)
print(f"Visits: {p}")

Sk = [40., 0.05, 0.002, 0.08, 0.08, 0.1] # Average Service Time 
Dk = p * Sk # Demands
print(f"The demand of the disk 1: {Dk[-2]*1000} ms")
print(f"The demand of the disk 2: {Dk[-1]*1000} ms")

Nk = Rk = np.zeros(6) 

for i in range(N+1):
    Rk = Dk * (1 + Nk)
    Rk[0] = 0 # Terminals
    Rsum = sum(Rk)
    X = i /(Rsum + Dk[0])
    Nk = Rk * X

print(f"The throughput of the system (X): {X} job/s")

N = Rk * X
R = N/X - Z
print(f"The average system response time (R): {Rsum*1000} ms")

Uk = Dk * X
print(f"The utilization of the [3] Application Server {Uk[2]}")
print(f"The utilization of the [4] DBMS {Uk[3]}")
print(f"The utilization of the [5] Disk 1 {Uk[4]}")
print(f"The utilization of the [6] Disk 2 {Uk[5]}")

Xk = X * p
print(f"The throughput of the disk 1: {Xk[4]} job/s")
print(f"The throughput of the disk 2: {Xk[5]} job/s")