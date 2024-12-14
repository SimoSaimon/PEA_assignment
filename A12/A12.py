import numpy as np
from scipy import linalg

l1 = 2.5
l2 = 2
P = np.array([[0., 0.7, 0., 0.],
              [0., 0., 0.25, 0.45],
              [0., 1., 0., 0.],
              [0., 1., 0., 0.]])

l = np.zeros(4) 
l[0]= l1/(l1+l2)
l[1]=l2/(l1+l2)

I = np.eye(4)
p= linalg.solve((I-P).T, l)
print(f"The visits of the application server: {p[1]}")
print(f"The visits of the storage: {p[2]}")
print(f"The visits of the DBMS: {p[3]}")

X = l1+l2
print(f"The throughput of the system (X): {X}")

Sk = np.array([2, 0.02, 0.1, 0.07]) 
Dk = p * Sk
Uk = X*Dk # Utilization

Nk = Uk / (1 - Uk)
Nk[0]= Uk[0]
N = sum(Nk)
print(f"The average number of jobs in the system (N): {N}") # Average Number of jobs

Rk = Dk / (1- Uk) # Residence Time
Rk[0] = Dk[0]
R = sum(Rk)
print(f"The average system response time (R): {R*1000} ms")

MaxLam = 1 / max(Dk)
print(f"The maximum arrival rate the system would be able to handle : {MaxLam}")