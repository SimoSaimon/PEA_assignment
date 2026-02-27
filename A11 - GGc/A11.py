import numpy as np
import math

# Scenario I
print("Scenario I:")

# Parameters
lerl = 100
kerl = 4
lam = 20

D = kerl/lerl
rho = lam * D

U = rho
print(f"\tThe utilization of the system: {U}")

m_2 = (kerl/lerl**2) + D**2
w = lam * m_2/2

R = D + w / (1 - rho)
print(f"\tThe (exact) average response time: {R*1000} ms")

N = lam * R
print (f"\tThe (exact) average number of jobs in the system: {N}")

# Scenario II
print("Scenario II:")

# Parameters
p1 = 0.8
p2 = 1-p1
l1 = 40
l2 = 240

T = ((p1 / l1) + (p2/l2)) # average inter-arrival time
lam = 1/T

c = int(np.ceil(lam * D))
print(f"\tThe minimum number of servers: {c}")

rho = D/(c*(T)) 

U = rho
print(f"\tThe average utilization of the system: {U}")

m_1 = (p1/l1)+(p2/l2)
m_2 = 2*((p1/l1**2)+(p2/l2**2))
cv = math.sqrt(m_2 - m_1**2)/m_1 
ca = 1/math.sqrt(kerl) 

R = D + ((cv**2+ca**2)/2) * ((rho**c)*D) / (1-rho**c)
print(f"\tThe approximate average response time: {R*1000} ms")

N = lam * R
print(f"\tThe approximate average number of jobs in the system: {N}")
