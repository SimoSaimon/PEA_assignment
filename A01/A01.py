import numpy as np
import matplotlib.pyplot as plt

# Loads first column
A = np.loadtxt("Logger1.csv", delimiter=";")

# Loads second column
C = np.loadtxt("Logger2.csv", delimiter=";")

inrows = A.shape[0]

T = C[-1] - A[0] # Defines the total time

print(f"\nTotal time observed: {T:.3f} min\n")

# Busy time
B=C[0]-A[0]
for i in range(1,inrows):
    B= B+ C[i]-max(A[i],C[i-1])
print(f"Busy time: {B} min\n")

# Computes the basic performance indices

U = B / T # Utilization
print(f"Utilization: {U*100}% \n")

X = inrows / T # Throughput 
print(f"Throughput and arrival rate: {X} cars/min \n")

A_i = 1 / X # Utilization
print(f"Average inter-arrival time: {A_i} min \n")

S = U / X # Average Service Time 
print(f"Average service time: {S} min \n")

R = np.mean(C-A) # Average response time
print(f"Average response time: {R} min \n")

N = X * R # The number of jobs is computed using Little's law
print(f"Average number of jobs: {N}  \n")

# Plots the distribution of the number of cars (0 to 25)
ac_t = np.column_stack((np.concatenate((A, C)), np.concatenate((np.ones(inrows), -np.ones(inrows)))))
ac_t= ac_t[ac_t[:,0].argsort()]
ac_t[:,1]=np.cumsum(ac_t[:,1])
ac_t = np.column_stack((
    ac_t[1:, 0] - ac_t[0:-1, 0],  
    ac_t[0:-1, 1]                   
))

pn=[0]*26
pnn=[0]*26

for i in range(0,26):
    pnn[i]=i
    pn[i]=np.sum(ac_t[ac_t[:,1]==i,0])/T

plt.bar(pnn,pn)
plt.title('Distribution of the number of cars (0 to 25)')
plt.xlabel('Number of cars')
plt.ylabel('Probability')
plt.grid(axis='y')
plt.show()

# Plots the response time distribution
PR  = [0]*41
PRT = [0]*41
for i in range(0,41):
    PRT[i] = i
    PR[i] = sum(C-A < i) / inrows

plt.plot(PRT, PR, label="Distribution of response time", linestyle='-',
         color='blue')
plt.title('Distribution of response time')
plt.xlabel('Response time (min)')
plt.ylabel('Probability')
plt.xticks(PRT)
plt.grid(True)
plt.show()


## Plots the service time distribution
PS  = [0]*51
PST = [0]*51

RT=np.zeros(inrows)

for i in range(1,inrows):
   RT[i] =C[i]-max(A[i],C[i-1])


for i in range(0,51):
    PST[i] = i/10
    PS[i] = sum(RT < i/10) / inrows
    

plt.plot(PST, PS, label="Distribution of service time", linestyle='-',
         color='blue')
plt.title('Distribution of service time')
plt.xlabel('Service time (min)')
plt.ylabel('Probability')
plt.xticks(PST)
plt.grid(True)
plt.show()