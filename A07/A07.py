import numpy as np
import matplotlib.pyplot as plt
from collections import deque


tMax = 1200000

s = 1
t = 0

sxt = deque()
sxt.append([t, s])

ts1 = 0
ts2 = 0
ts3 = 0
ts4 = 0
tc = 0

RTT = deque()
curRTT = 0

def calc_cost():
    u = np.random.rand()
    if u < 0.9:
        return 2.5
    elif u < 0.96:
        return 4.0
    else:
        return 6.0


while t < tMax:
    dt = 0
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
        
        p1h = 0.8
        l1h = 0.4
        l2h = 0.1
        
        if u1<p1h:
            dt=-np.log(u2)/l1h
        else:
            dt=-np.log(u2)/l2h
            
        ts1 = ts1 + dt
        curRTT = curRTT + dt
        
    # Cash Payment
    if s == 2:
        dt = -np.log(1-np.random.rand())/0.4
        ts2 = ts2 + dt
        curRTT = curRTT + dt
        ns = 4
        tc = tc + calc_cost()
        
    # Electronic Payment
    if s == 3:
        for i in range (0,4):
            dt = dt - np.log(np.random.rand())/2
        ts3 = ts3 + dt
        curRTT = curRTT + dt
        ns = 4
    
    # Printing
    
    if s == 4:
             
        p1h = 0.95
        
        if u1<p1h:
            kh = 2
            lh = 10
        else:
            kh = 1
            lh = 0.1
            
        u = np.random.rand(kh)
        dt = -np.sum(np.log(u))/lh
        ts4 = ts4 + dt
        curRTT = curRTT + dt
        ns = 1
        
    t = t + dt
    s = ns

    sxt.append([t, s])
    
#print(sxt)
sxtA = np.array(list(sxt))

#plt.stairs(sxtA[0:-1,1], sxtA[:,0])
#plt.show()

print("Prob. Task 1: ", ts1 / t)
print("Prob. Task 2: ", ts2 / t)
print("Prob. Task 3: ", ts3 / t)
print("Prob. Task 4: ", ts4 / t)
print("Average time between two executions of the same task: ", np.mean(list(RTT)))
print(f"Average cash collected by the machine in 20 hours of operation: {tc/(tMax/1200)}")