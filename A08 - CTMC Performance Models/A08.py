import numpy as np
from scipy import linalg

Q = np.zeros((20, 20))

val = np.loadtxt("Data.csv", delimiter=";", encoding="utf-8-sig")

# Create matrix for linalg
for i in range(0, 20, 2):

    k = int(i/2) # number of the song
    ext_prob = val[k,1]/100 # probability of extending the song
    skip_prob = val[k,2]/100 # probability of skipping the song
    skip_prob_ext = val[k,4]/100 # probability of extending the song after extension
    
    # Song k state
    Q[i,i]=-1/(val[k,0]) # t song
    Q[i,(i+1)%20]=-Q[i,i]* ext_prob # extend song 
    Q[i,(i+2)%20]=-Q[i,i]*(1-ext_prob-skip_prob) # next song
    Q[i,(i+4)%20]=-Q[i,i]*skip_prob # skip next song
    j=i+1
    
    # Song k extension state
    Q[j,j]=-1/(val[k,3]) # t song ext
    Q[j,(j+1)%20]=-Q[j,j]*(1-skip_prob_ext) # next song
    Q[j,(j+3)%20]=-Q[j,j]*skip_prob_ext # skip next song

Q_c = np.copy(Q)

Q[:,0]=np.ones(20)
u = np.zeros(20)
u[0]=1

pi = linalg.solve(Q.T,u)

pt = np.zeros(10)

# Probability for each song (including extension)
for i in range (0,20,2):
    pt[int(i/2)]= pi[i]+pi[i+1]
    
print(f"The probability that a patron ears song 1: {pt[0]}")
print(f"The probability that a patron ears song 2: {pt[1]}")
print(f"The probability that a patron ears song 5: {pt[4]}")
print(f"The probability that a patron ears song 9: {pt[8]}")
print(f"The probability that a patron ears song 10: {pt[9]}")

aveCost = pt @ val[:,5]

print(f"Average cost for each song: {aveCost}")

xi0=np.zeros((20,20))
xi0[-1,0]=1
xi0[-2,0]=1

# Number of shows per second
RTLP = ((Q_c*xi0)@np.ones(20))@ pi

print(f"Number of shows per day: {RTLP*3600*24}")
print(f"Average show duration: {1/(RTLP*60)}")