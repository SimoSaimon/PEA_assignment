import numpy as np
import matplotlib.pyplot as plt


def trace_stat(trace, trace_name):
    
    """
    Calculate the statistics for a csv in input.

    Args:
        trace (ndarray): Array of inter-arrival times
        trace_name (str): Name of the csv file
    
    """
    
    n = trace.shape[0]
    yp = np.r_[1.:n+1]/n
    
    print(f"\n\n{trace_name} results: \n")
    # moment

    ex1 = trace.sum()/n
    print(f"    Mean: {ex1}\n")

    ex2 = (trace**2).sum()/n
    print(f"    Second moment: {ex2}")

    ex3 = (trace**3).sum()/n
    print(f"    Third moment: {ex3}")

    ex4 = (trace**4).sum()/n
    print(f"    Fourth moment: {ex4}\n")

    cx2 = ((trace-ex1)**2).sum()/n
    print(f"    Variance: {cx2}")

    cx3 = ((trace-ex1)**3).sum()/n
    print(f"    Third centered moment: {cx3}")

    cx4 = ((trace-ex1)**4).sum()/n
    print(f"    Fourth centered moment: {cx4}\n")

    std = np.sqrt(cx2)
    print(f"    Standard deviation: {std}")

    skewness = np.mean(((trace - ex1) / std) ** 3)
    print(f"    Skewness: {skewness}")

    std4 = np.mean(((trace - ex1) / std) ** 4)
    print(f"    Fourth standardized moment: {std4}")

    coeff_var = std / ex1
    print(f"    Coefficent of variance: {coeff_var}")

    excess_kurtosis = std4 - 3
    print(f"    Excess kurtosis: {excess_kurtosis}")

    sTrace = trace.copy()
    sTrace.sort()

    q_1 = np.percentile(sTrace, 25)
    print(f"    First quartile: {q_1}\n")

    median = np.median(sTrace)
    print(f"    Median: {median}")

    q_3 = np.percentile(sTrace, 75)
    print(f"    Third quartile: {q_3}\n")

    p05= np.percentile(sTrace, 5)
    print(f"    5th percentile: {p05}")
    p90= np.percentile(sTrace, 90)
    print(f"    90th percentile: {p90}\n")

    # The minimum value for Lag
    min_lag = 1
    # The maximum value for Lag
    max_lag = 100
    correlations = []

    for m in range(min_lag, max_lag + 1):
        correlations.append(((trace[m:] - ex1) * (trace[:-m] - ex1)).sum() / ((n - m) * cx2))

    # Plot of the Pearson Correlation Coefficients for Lags from 1 to 100
    lags = np.arange(min_lag, max_lag + 1)
    plt.plot(lags, correlations, linestyle='-', color='blue')
    plt.title(f'Pearson Correlation Coefficient for Lags - 1 to 100 - ({trace_name})')
    plt.xlabel('Lag')
    plt.ylabel('Pearson Correlation Coefficient')
    plt.grid(True)
    plt.show()


    # Plot the distribution
    plt.plot(sTrace,yp, linestyle='-', color='blue')
    plt.title(f'Approximated CDF ({trace_name})')
    plt.xlabel('Values')
    plt.ylabel('CDF approximated value')
    #plt.xticks(sTrace)
    plt.grid(True)
    plt.show()


# Names of csv
csv=["Trace1","Trace2","Trace3"]

for i in csv:
    trace_stat(np.loadtxt(i+".csv", delimiter=";"),i)

