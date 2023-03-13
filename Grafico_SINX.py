from matplotlib import legend
#Grafico del Seno trigonometrico
import math
import matplotlib.pyplot as plt

incr=-5
x=[]
y=[]
z=[]
while incr<5:
  x.append(incr)
  incr+=0.1

for i in x:
  y.append(math.sin(i))
  z.append(math.cos(i))


plt.plot(x,y,'--')
plt.plot(x,z,'*')
plt.legend(["Sin(x)", "Cos(x)"])
plt.grid()
plt.show()