import matplotlib.pyplot as plt
import numpy as np

def c(x,t):
 z=np.exp(-t)
 chi=(np.exp(-(x**2)/(1-z**2)))/((1-z**2)**(1/2)) -np.exp(-x**2)
 return chi


plt.axis([0,5,-0.4,0.3])
t1=np.arange(0.001, 5.0, 0.001)
plt.title('nature of $\hat{\chi}$ for m=1, $\omega$=1')
plt.ylabel('$\hat{\chi}(0, x,t)$')
plt.xlabel('$t$')
chip2,=plt.plot(t1, c(2,t1),'r-',lw =1.5,label='x=2')
#chim2,=plt.plot(t1,c(-2,t1),'b-', lw=1.5,label='x=-2')
chip1,=plt.plot(t1, c(1,t1),'b-',lw =2,label='x=1')
#chim1,=plt.plot(t1,c(-1,t1),'b.', lw=2,label='x=-1')
plt.legend([chip2,chip1],["$x$ = 2","$x$ = 1"])
plt.savefig('chi.png')
plt.show()