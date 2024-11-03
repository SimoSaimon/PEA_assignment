import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import scipy.special as sp
from scipy.special import gamma

def trace_stat(trace, trace_name):
    
    """
    Calculate different fitting parameters for a csv in input.

    Args:
        trace (ndarray): Array of inter-arrival times
        trace_name (str): Name of the csv file
    
    """
    
    print(f"\n\n{trace_name} results:")
    
    N = trace.shape[0]

    probV = np.r_[1.:N+1] / N

    srt = trace.copy()
    srt.sort(0)
    
    M1t = np.sum(srt) / N
    M2t = np.sum(srt**2) / N
    M3t = np.sum(srt**3) / N
    
    # Variance
    var=np.var(trace)
    
    # Coefficient of Variation
    cv = np.sqrt(var) / M1t
    
    print(f"\tFirst moment: {M1t}")
    print(f"\tSecond moment: {M2t}")
    print(f"\tThird moment: {M3t}")
    

    # Exponential
    print("\tExponential:")
    l1d = 0.2
    l2d = 0.3
    
    t = np.r_[1.:N+1]/50
    
    lexp = 1/M1t
    
    print(f"\t\tRate (lambda): {lexp}\n")
    
    Fexp = 1 - np.exp(-lexp * t)
    
    plt.plot(srt, probV, ".",label=trace_name)
    plt.plot(t, Fexp, label= "Exponential")
    plt.title(f'{trace_name} fitting')
    
    # Uniform
    print("\tUniform:")
    
    a = M1t - 0.5 * np.sqrt(12 * (M2t - M1t*M1t))
    b = M1t + 0.5 * np.sqrt(12 * (M2t-M1t*M1t))
    
    print(f"\t\tMinimum (a): {a}")
    print(f"\t\tMaximum (b): {b}\n")
    
    Funif = (t - a) / (b - a)
    
    for i in range (0, len(Funif)):
        if Funif[i] > 1:
            Funif[i]=1
    
    plt.plot (t, Funif, label= "Uniform")
    
    
    # Erlang
    print("\tErlang:")
    if cv>1:
        print("\t\t Coefficient of Variation > 1, can't use Erlang")
    else:
        kerl = np.round((M1t ** 2) / var)
        lerl = kerl / M1t
        
        print(f"\t\tStages (k): {kerl}")
        print(f"\t\tRate (lambda): {lerl}\n")

        Ferl = 1 - np.sum([(lerl * t)**n / sp.factorial(n) for n in range(int(kerl))], axis=0) * np.exp(-lerl * t)

        plt.plot (t, Ferl, label= "Erlang")
                    
    # Weibull
    print("\tWeibull:")
    
    def fun(x):
        l1 = x[0]
        k = x[1]

        M1d = l1 * gamma(1 + 1 / k)
        M2d = l1 ** 2 * gamma(1 + 2 / k)
        return np.abs(M1d / M1t - 1) ** 2 + np.abs(M2d / M2t - 1) ** 2


    result = opt.minimize(fun, np.array([0.001, 0.001]), bounds=((0.001, 100), (0.1, 100)))

    l1d = result.x[0]
    kd = result.x[1]
    
    print(f"\t\tScale (lambda): {l1d}")
    print(f"\t\tShape (k): {kd}\n")
    
    FWei = 1 - np.exp(-(t / l1d) ** kd)
    plt.plot(t, FWei, label= "Weibull")

    # Pareto with method of moments
    print("\tPareto:")
    
    def fun(x):
        a = x[0]
        m = x[1]

        M1d = a * m / (a - 1)
        M2d = a * m ** 2 / (a - 2)

        return np.abs(M1d / M1t - 1) ** 2 + np.abs(M2d / M2t - 1) ** 2
    
    result = opt.minimize(fun, np.array([3, 1]), bounds=((1.1, 100.0), (0.001, 100.0)),constraints = {'type': 'ineq','fun': lambda x: x[1] - x[0] - 0.001})

    ad = result.x[0]
    md = result.x[1]
    
    print(f"\t\tShape (a): {ad}")
    print(f"\t\tScale (m): {md}\n")
    
    Fpar = np.where(t >= md, 1 - (md / t) ** ad, 0)
    
    plt.plot(t, Fpar, label= "Pareto")

    # Hyper/Hypo - exponential
    if cv >= 1:
        print("\tHyper-exponential:")

        def fun(x):
            l1 = x[0]
            l2 = x[1]
            p1 = x[2]
            p2 = 1-p1
            
            return -np.sum(np.log(p1*l1*np.exp(-l1*srt) + p2*l2*np.exp(-l2*srt)))

        sx = opt.minimize(fun, np.array([0.8/M1t,1.2/M1t,0.4]), bounds=((0.001, 100.0), (0.001, 100.0), (0.001, 0.999)), constraints=[{'type': 'ineq', 'fun': lambda x:  x[1] - x[0] - 0.001}])
        l1d = sx.x[0]
        l2d = sx.x[1]
        p1d = sx.x[2]
        p2d = 1 - p1d

        print(f"\t\tMinimum rate: {l1d}")
        print(f"\t\tMaximum rate: {l2d}")
        print(f"\t\tProbability of first branch: {p1d}\n")

        t = np.r_[1.:N+1] / 50

        Fhype = 1 - p1d * np.exp(-t * l1d) - p2d * np.exp(-t * l2d)

        plt.plot(t, Fhype, label= "Hyper")
        plt.legend()
        plt.show()
        
        print("\tHypo-exponential:")
        print("\t\t Coefficient of Variation > 1, can't use Hypo-exponential")
    else: 
        # Hypo-exponential
        
        print("\tHypo-exponential:")
        
        def fun(x):
            l1 = x[0]
            l2 = x[1]
        
            if l1 == l2:
                return -1000000-l1-l2
            else:
                return -np.sum(np.log(l1*l2/(l1-l2)*(np.exp(-l2*srt) - np.exp(-l1*srt))))




        sx = opt.minimize(fun, np.array([1/(0.7*M1t),1/(0.3*M1t)]), bounds=((0.001, 100.0), (0.001, 100.0)), constraints=[{'type': 'ineq', 'fun': lambda x:  x[1] - x[0] - 0.001}])
        l1d = sx.x[0]
        l2d = sx.x[1]

        print(f"\t\tMinimum rate: {l1d}")
        print(f"\t\tMaximum rate: {l2d}")

        M1d = 1 / l1d + 1 / l2d
        M2d = 2 * (1 / (l1d**2) + 1 / (l1d * l2d) + 1 / (l2d**2))


        t = np.r_[1.:N+1] / 50

        Fhypo = 1 - 1 / (l2d - l1d) * (l2d * np.exp(-l1d * t) - l1d * np.exp(-l2d * t))

        plt.plot(t, Fhypo, label= "Hypo")
        plt.legend()
        plt.show()

        print("\tHyper-exponential:")
        print("\t\t Coefficient of Variation < 1, can't use Hyper-exponential")

# Names of csv
csv=["Trace1","Trace2"]

for i in csv:
    trace_stat(np.loadtxt(i+".csv", delimiter=";"),i)