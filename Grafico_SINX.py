from matplotlib import legend
#Grafico del Seno trigonometrico
import math
import matplotlib.pyplot as plt

incr=-5
x=[]
y=[]
z=[]
r=[]
while incr<5:
  x.append(incr)
  incr+=0.1

for i in x:
  y.append(math.sin(i))
  z.append(math.cos(i))
  r.append(math.tanh(i))


plt.plot(x,y,'--')
plt.plot(x,z,'*')
plt.plot(x,r)
plt.legend(["Sin(x)", "Cos(x)","Tan(x)"])
plt.grid()
plt.show()