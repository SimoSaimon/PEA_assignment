import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

N = 10000

t = np.r_[1:N+1]/N
xp = np.r_[1.:N+1]/50
u1 = np.random.rand(N)
u2 = np.random.rand(N)

# exponential

lexp=0.25

Xexp = -np.log(1-u1)/lexp
Xexp.sort(0)

Fexp = 1 - np.exp(-lexp * xp)

plt.plot(Xexp, t, ".", label = "Real")
plt.plot (xp, Fexp, label= "Empiric")
plt.legend()
plt.title('Exponential')
plt.show()

# Pareto

a = 2.5
m = 3

XPar= m / (1 - u1) ** (1 / a)
XPar.sort(0)

FPar = np.where(xp >= m, 1 - (m / xp) ** a, 0)

plt.plot(XPar, t, ".", label = "Real")
plt.plot (xp, FPar, label= "Empiric")
plt.legend()
plt.title('Pareto')
plt.show()

# Erlang

kerl = 8
lerl = 0.8

XErl = [0.]*N
ue = np.random.rand(N, kerl)

XErl = (- np.sum(np.log(ue), axis = 1))/lerl
XErl.sort()

Ferl = 1 - np.sum([(lerl * xp)**n / sp.factorial(n) for n in range(int(kerl))], axis=0) * np.exp(-lerl * xp)

plt.plot(XErl, t, ".", label = "Real")
plt.plot (xp, Ferl, label= "Empiric")
plt.title('Erlang')
plt.legend()
plt.show()

# Hypo

l1d = 0.25
l2d = 0.4

XHypo= -np.log(u1)/l1d - np.log(u2)/l2d
XHypo.sort(0)

FHypo = 1 - 1 / (l2d - l1d) * (l2d * np.exp(-l1d * xp) - l1d * np.exp(-l2d * xp))

plt.plot(XHypo, t, ".", label = "Real")
plt.plot (xp, FHypo, label= "Empiric")
plt.legend()
plt.title('Hypo-exponential')
plt.show()

# Hyper

l1 = 1
l2 = 0.05
p1 = 0.75
p2 = 1 - p1

XHyper=[0.]*N
for i in range(0,N):
    if u1[i]<p1:
        XHyper[i]=-np.log(u2[i])/l1
    else:
        XHyper[i]=-np.log(u2[i])/l2

XHyper.sort()

FHyper = 1 - p1 * np.exp(-xp * l1) - p2 * np.exp(-xp * l2)

plt.plot(XHyper, t, ".", label = "Real")
plt.plot (xp, FHyper, label= "Empiric")
plt.title('Erlang')
plt.title('Hyper-exponential')
plt.show()
