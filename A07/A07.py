import numpy as np
import matplotlib.pyplot as plt
from collections import deque


tMax = 12000000
t = ts1 = ts2 = ts3 = ts4 = tc = curRTT = 0
s = 1

# GUI Time parameters
p1g = 0.8
l1g = 0.4
l2g = 0.1

# Cash Payment parameters
lec = 0.4

# Electronic payment parameters
lee = 2
kee = 4

# Printing parameters
p1p = 0.95
k1p = 2 
l1p = 10
k2p = 1
l2p = 0.1

tot = 0
RTT = deque()

def calc_cost():
    u = np.random.rand()
    if u < 0.9:
        return 2.5
    elif u < 0.96:
        return 4.0
    else:
        return 6.0


while t < tMax:
    
    # Waiting Input
    if s == 1:
        
        if t != 0:
            RTT.append(curRTT)
            curRTT = 0
        
        u = np.random.rand()
        
        if u < 0.2:
            ns = 1
        elif u < 0.48:
            ns = 2
        else:
            ns = 3
        
        u1 = np.random.rand()
        u2 = np.random.rand()
        
        if u1<p1g:
            dt=-np.log(u2)/l1g
        else:
            dt=-np.log(u2)/l2g
            
        ts1 = ts1 + dt
        curRTT = curRTT + dt
        
    # Cash Payment
    if s == 2:
        dt = -np.log(1-np.random.rand())/lec
        ts2 = ts2 + dt
        curRTT = curRTT + dt
        ns = 4
        tc = tc + calc_cost()
        
    # Electronic Payment
    if s == 3:
        u = np.random.rand(kee)
        dt = -np.sum(np.log(u))/lee
        ts3 = ts3 + dt
        curRTT = curRTT + dt
        ns = 4
    
    # Printing
    if s == 4:
        
        if u1<p1p:
            k = k1p
            l = l1p
        else:
            k = k2p
            l = l2p
            
        u = np.random.rand(k)
        dt = -np.sum(np.log(u))/l
        ts4 = ts4 + dt
        curRTT = curRTT + dt
        ns = 1
        tot = tot + 1
    t = t + dt
    s = ns


print("Prob. Task 1: ", ts1 / t)
print("Prob. Task 2: ", ts2 / t)
print("Prob. Task 3: ", ts3 / t)
print("Prob. Task 4: ", ts4 / t)
print(f"Total cycle (including people who don't buy ticket): {len(RTT)}")
print(f"Total cycle from first to last task: {tot}")
print("Average time between two executions of the same task: ", np.mean(list(RTT)))
print(f"Average cash collected by the machine in 20 hours of operation: {tc/(tMax/1200)}")