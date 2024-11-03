import numpy as np
import matplotlib.pyplot as plt

N = 5000

K0 = 10
DeltaK = 10
MaxK = 100000

conf_int = 1.96
maxRelErr = 0.02

U1 = U2 = X1 = X2 = N1 = N2 = R1 = R2 = 0

K = K0
Krange = K

# Parameters Scenario I
l1h = 0.025
l2h = 0.1
p1h = 0.35

kwb = 0.333
lwb = 2.5 

# Parameters Scenario II
kerl = 8
lerl = 1.25

a = 1
b = 10

def hyper_exp_distr():
    u1 = np.random.rand(N)
    u2 = np.random.rand(N)
    XHyper=[0.]*N
    for i in range(0,N):
        if u1[i]<p1h:
            XHyper[i]=-np.log(u2[i])/l1h
        else:
            XHyper[i]=-np.log(u2[i])/l2h
    return XHyper

def weibull_distr():
    u_wb = np.random.rand(N)
    return lwb * (-np.log(u_wb)) ** (1 / kwb)
    
def erlang_distr():
    u_erl = np.random.rand(N, kerl)
    return (- np.sum(np.log(u_erl), axis = 1))/lerl

def uniform_distr():
    u_unif = np.random.rand(N)
    return a + (b - a) * u_unif

def calc_conf(U1, U2, K):
    EU     = U1 / K
    EU2    = U2 / K
    VarU   = EU2 - EU*EU
    DeltaU  = conf_int * np.sqrt(VarU / K)
    Ul = EU - DeltaU
    Uu = EU + DeltaU
    RelErrU = 2 * (Uu - Ul) / (Uu + Ul)
    return Ul, Uu, RelErrU

# Scenario I
while K < MaxK:
    for k in range(0, Krange):
        Xarr = hyper_exp_distr()
        Xsrv = weibull_distr()

        A = np.zeros(N)
        C = np.zeros(N)

        A[0] = Xarr[0]
        C[0] = Xarr[0] + Xsrv[0]

        for i in range(1, N):
            A[i] = A[i-1] + Xarr[i]
            C[i] = max(A[i], C[i-1]) + Xsrv[i]
            
        T = C[N-1]
        B = np.sum(Xsrv)
        
        # Utilization
        Uk = B / T
        U1 = U1 + Uk
        U2 = U2 + Uk*Uk
        
        # Throughput
        Xk = len(A) / T
        X1 = X1 + Xk
        X2 = X2 + (Xk ** 2)
        
        # Average number of jobs in the system
        Rk = np.mean(C - A)
        Nk = Xk * Rk
        N1 = N1 + Nk
        N2 = N2 + (Nk ** 2)

        # Average response time
        R1 = R1 + Rk
        R2 = R2 + (Rk ** 2)

    Ul, Uu, RelErrU = calc_conf(U1, U2, K)
    Xl, Xu, RelErrX= calc_conf(X1, X2, K)
    Nl, Nu, RelErrN = calc_conf(N1, N2, K)
    Rl, Ru, RelErrR = calc_conf(R1, R2, K)
    
    if RelErrU < maxRelErr and RelErrX < maxRelErr and RelErrN < maxRelErr and RelErrR < maxRelErr:
        break
        
    K = K + DeltaK
    Krange = DeltaK

print("\nScenario I:")
print("\t95% confidence interval of U: ", Ul, Uu)
print("\tRelative error of U: ", RelErrU)

print("\t95% confidence interval of X: ", Xl, Xu)
print("\tRelative error of X: ", RelErrX)

print("\t95% confidence interval of N: ", Nl, Nu)
print("\tRelative error of N: ", RelErrN)

print("\t95% confidence interval of R: ", Rl, Ru)
print("\tRelative error of R: ", RelErrR)

print(f"\tSolution obtained in {K} iterations\n")

K0 = 10
DeltaK = 10
MaxK = 100000
K = K0
Krange = K

U1 = U2 = X1 = X2 = N1 = N2 = R1 = R2 = 0

# Scenario II
while K < MaxK:
    for k in range(0, Krange):
        Xarr = erlang_distr()
        Xsrv = uniform_distr()

        A = np.zeros(N)
        C = np.zeros(N)

        A[0] = Xarr[0]
        C[0] = Xarr[0] + Xsrv[0]

        for i in range(1, N):
            A[i] = A[i-1] + Xarr[i]
            C[i] = max(A[i], C[i-1]) + Xsrv[i]
            
        T = C[N-1]
        B = np.sum(Xsrv)
        
        # Utilization
        Uk = B / T
        U1 = U1 + Uk
        U2 = U2 + Uk*Uk
        
        # Throughput
        Xk = len(A) / T
        X1 = X1 + Xk
        X2 = X2 + (Xk ** 2)
        
        # Average number of jobs in the system
        Rk = np.mean(C - A)
        Nk = Xk * Rk
        N1 = N1 + Nk
        N2 = N2 + (Nk ** 2)

        # Average response time
        R1 = R1 + Rk
        R2 = R2 + (Rk ** 2)

    Ul, Uu, RelErrU = calc_conf(U1, U2, K)
    Xl, Xu, RelErrX= calc_conf(X1, X2, K)
    Nl, Nu, RelErrN = calc_conf(N1, N2, K)
    Rl, Ru, RelErrR = calc_conf(R1, R2, K)
    
    if RelErrU < maxRelErr and RelErrX < maxRelErr and RelErrN < maxRelErr and RelErrR < maxRelErr:
        break
        
    K = K + DeltaK
    Krange = DeltaK

print("Scenario II:")
print("\t95% confidence interval of U: ", Ul, Uu)
print("\tRelative error of U: ", RelErrU)

print("\t95% confidence interval of X: ", Xl, Xu)
print("\tRelative error of X: ", RelErrX)

print("\t95% confidence interval of N: ", Nl, Nu)
print("\tRelative error of N: ", RelErrN)

print("\t95% confidence interval of R: ", Rl, Ru)
print("\tRelative error of R: ", RelErrR)

print(f"\tSolution obtained in {K} iterations\n")