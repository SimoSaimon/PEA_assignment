import numpy as np
import math

D = 0.2
K = 16

def calc_mmck(c, lam, K, D):
    """
    Calculate: 
        1. The total and average utilization of the system 
        2. The loss probability 
        3. The average number of jobs in the system 
        4. The drop rate 
        6. The average response time 
        7. The average time spent in the queue (waiting for service) 
    """
    rho = (lam * D)/c
    sum = 0

    for i in range(c):
        sum = sum + ((c*rho)**i)/math.factorial(i)

    n = K+1
    p = np.zeros(n)
    p[0] = (((c * rho)**c / math.factorial(c))* ((1-rho**(K-c+1))/(1-rho))+ sum)**(-1)

    for i in range (1,n):
        if i < c:
            p[i] = (p[0]/math.factorial(i)) * ((c*rho)**i)
        else: 
            p[i]= (p[0] * (c**c) * (rho**i))/math.factorial(c)
    
    U = 0
    for i in range(1,c+1):
        U = U + i * p[i]

    for i in range(c+1,n):
        U = U + c * p[i]

    print(f"\tThe utilization of the system: {U}")
    if c > 1:
        print(f"\tThe average utilization of the system: {U/c}")
    lossProb = p[K]
    print(f"\tThe loss probability: {lossProb}")

    N = 0
    for i in range (1,n):
        N = N + i * p[i]
    print(f"\tThe average number of jobs in the system: {N}")

    dropRate = lam * p[K]
    print(f"\tThe drop rate: {dropRate*60} req/min")

    R = N/(lam * (1-p[K]))
    print(f"\tThe average response time: {R*1000} ms")

    qw = R - D
    print(f"\tThe average response time spent in the queue: {qw*1000} ms")


print("Scenario I:")
c = 1
lam = 4
calc_mmck(c, lam, K, D)

print("Scenario II:")
c = 2
lam = 6
calc_mmck(c, lam, K, D)

print("Scenario III:")
c=1
lam = 16

while True:
    rho = (lam * D)/c
    sum = 0
    n = K+1
    p = np.zeros(n)
    for i in range(c):
        sum = sum + ((c*rho)**i)/math.factorial(i)

    p[0] = (((c * rho)**c / math.factorial(c))* ((1-rho**(K-c+1))/(1-rho))+ sum)**(-1)
    prod = p[0]

    for i in range (1,n):
        p[i]= (p[0] * (c**c) * (rho**i))/math.factorial(c)

    lossProb = p[K]
    
    if lossProb < 0.01:
        break
    c = c+1
    rho = (lam * D)/c

print(f"\tMinimum servers to achieve a loss probability less than 1%: {c}")

calc_mmck(c, lam, K, D)
