import numpy as np
import matplotlib.pyplot as plt
import math
from collections import deque


def scenario_M_M_c(lam, c = None):

    if c is None:
        c= int(np.ceil(lam * D))
        print(f"\tMinimum number of servers = {c}")
    
    rho = lam*D/c 
    pi = np.zeros(6)
    pNlei = np.zeros(6)

    pi[0]= (c * rho) ** c / math.factorial(c)*1/(1-rho)

    for k in range (0,c):
        pi[0]= pi[0]+(c * rho) ** k / math.factorial(k)

    pi[0] = 1 / pi[0]
    pNlei[0] = pi[0]

    for n in range (1,5):
        if n < c:   
            pi[n] = pi[n-1] * (c * rho) / n
        else:
            pi[n] = pi[n-1] * rho
            
        pNlei[n] = pNlei[n-1] + pi[n]

    print(f"\tp (N = 2) = {pi[2]}") # Probability to have 2 jobs in the system
    print(f"\tp (N < 5) = {pNlei[4]}") # Probability to have less than 5 jobs in the system

    Ub = rho
    U = Ub * c # Utilization

    print(f"\tTotal utilization = {U}")
    print(f"\tAverage utilization = {Ub}")

    NdenSum = 1

    for k in range (1,c):
        NdenSum = NdenSum + (c * rho) ** k / math.factorial(k)
        
    N = c * rho + (rho/(1-rho)) / (1 + (1-rho) * (math.factorial(c) / ((c*rho)**c))* NdenSum)

    Nq = N - U # Number of jobs in the queue
    print(f"\tNumber of jobs in the queue = {Nq}")

    R = N / lam # response time 
    print(f"\tResponse time  = {R}")
    
    pRgt2 = np.exp(-2/R) # probability that response time is greater than 2
    print(f"\tp(R>2) = {pRgt2}")

    perc95 = -np.log(1- 95/100)* R
    print(f"\tperc 95th = {perc95}")

D = 1.6 

print("\nScenario I:")
scenario_M_M_c(1/2, 1)

print("\nScenario II:")
scenario_M_M_c(1, 2)

print("\nScenario III:")
scenario_M_M_c(4)

print("\nScenatio IV:")

lam = 10

rho = lam * D

pi = np.zeros(6)
pNlei = np.zeros(6)

pi[0]= np.exp(-rho)
pNlei[0] = pi[0]
for n in range (1,5):
    pi[n] = pi[n-1] * rho / n
    pNlei[n] = pNlei[n-1] + pi[n]

print(f"\tp (N = 2) = {pi[2]}") # Probability to have 2 jobs in the system
print(f"\tp (N < 5) = {pNlei[4]}") # Probability to have less than 5 jobs in the system

U = rho
print(f"\tUtilization = {U}")

R = U / lam # response time 
print(f"\tResponse time  = {R}")