import numpy as np
from scipy import linalg

# lam (parts/min)
lA = 1.5 / 60 
lB = 2.5 / 60
lC = 2 / 60

XA = lA
XB = lB
XC = lC

# Service times (Production)
S1A = 8
S1B = 3
S1C = 4

# Service times (Packaging)
S2A = 10
S2B = 2
S2C = 7

p21A = 0.1
p21B = 0.08
p21C = 0.12

t = [0, 1]

PA = np.array([t, [p21A, 0]])
PB = np.array([t, [p21B, 0]])
PC = np.array([t, [p21C, 0]])

t = np.array([1, 0])

pA = linalg.solve((np.eye(2) - PA.T), t)
pB = linalg.solve((np.eye(2) - PB.T), t)
pC = linalg.solve((np.eye(2) - PC.T), t)

D1A = pA[0] * S1A
D1B = pB[0] * S1B
D1C = pC[0] * S1C
D2A = pA[1] * S2A
D2B = pB[1] * S2B
D2C = pC[1] * S2C

U1 = lA * D1A + lB * D1B + lC * D1C
U2 = lA * D2A + lB * D2B + lC * D2C
print(f"The utilization of the production station: {U1}")
print(f"The utilization of the packaging station: {U2}")

R1A = D1A / (1 - U1)
R1B = D1B / (1 - U1)
R1C = D1C / (1 - U1)
R2A = D2A / (1 - U2)
R2B = D2B / (1 - U2)
R2C = D2C / (1 - U2)
RA = R1A + R2A
RB = R1B + R2B
RC = R1C + R2C
print(f"The average system response time for Class A - RA: {RA} min") 
print(f"The average system response time for Class B - RB: {RB} min")
print(f"The average system response time for Class C - RC: {RC} min")

NA = lA * RA
NB = lB * RB
NC = lC * RC
print(f"The average number of jobs in the system for Class A - NA: {NA}")
print(f"The average number of jobs in the system for Class B - NB: {NB}")
print(f"The average number of jobs in the system for Class C - NC: {NC}")

N1 = XA * R1A + XB * R1B + XC * R1C
N2 = XA * R2A + XB * R2B + XC * R2C
N = N1 + N2
print(f"The class-independent average number of jobs in the system (N): {N}")

X = XA + XB + XC
R = (XA * RA + XB * RB + XC * RC) / X
print(f"The class-independent average system response time (R): {R}")