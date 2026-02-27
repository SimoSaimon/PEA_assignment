# X and R calculated thanks to jvma

X = 0.3755294792806878
XA = 0.03666758853682677
XB = 0.0055285574105277055
XC = 0.3333333333333333

RA = 535.4408320283504
RB = 540.6370348053684
RC = 243.21709383252212

R = (XA * RA + XB * RB + XC * RC)/X

print(f" The class-independent average system response time (R), excluding the think-time: {R}")