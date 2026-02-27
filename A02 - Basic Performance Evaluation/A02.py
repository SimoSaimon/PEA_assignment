import numpy as np
import matplotlib.pyplot as plt

# Loads first column
I = np.loadtxt("Logger1.csv", delimiter=";") # inter-arrival time

# Loads second column
S = np.loadtxt("Logger2.csv", delimiter=";") # service time

inrows = I.shape[0]

C_T = np.zeros(inrows)

# Find alpha
for alpha in np.arange(0.1, 1.0, 0.0001):

    I_s=I*alpha
    
    A_T = np.cumsum(I_s)  

    C_T[0] = S[0] + A_T[0]
    
    for i in range(1, inrows):
        C_T[i] = max(C_T[i-1], A_T[i]) + S[i]

    T= C_T[-1]-A_T[0]

    a_r= inrows/T 

    R = np.mean(C_T - A_T)
    
    if R<=20:
        break

print(f"Alpha = {alpha}")
print(f"For R = {R}")
print(f"Arrival rate = {a_r}\n")

# second task

a_r_new = 1.2

alpha= 1/(np.mean(I)*a_r_new)

print(f"New alpha = {alpha}")

# Find beta
for beta in np.arange(1.0, 0.1, -0.0001):

    I_s=I*alpha
    S_s=S*beta
    A_T = np.cumsum(I_s)  

    C_T[0] = S_s[0] + A_T[0]
    
    for i in range(1, inrows):
        C_T[i] = max(C_T[i-1], A_T[i]) + S_s[i]

    R = np.mean(C_T - A_T) 
    if R<=15:
        break

print(f"Beta <= {beta}")
print(f"For R <= {R}")

