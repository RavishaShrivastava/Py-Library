import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.colors as colors

fig=plt.figure()
ax=plt.axes(projection='3d')

#3D line graph plotting code
z=np.linspace(0,15,1000)
x=np.sin(z)
y=np.cos(z)

ax.plot3D(x,y,z,'green')

#title of the graph
ax.set_title("3D line graph plotting")
plt.show()

#scatter plot graph code
fig=plt.figure()
ax=plt.axes(projection='3d')

a=15*np.random.rand(100)
b=15*np.random.rand(100)
d=15*np.random.rand(100)
c=np.random.rand(100)

ax.scatter3D(a,b,d,c=c)
ax.set_title("3D scatter plot graph")
plt.show()


#wireframe graph code
fig=plt.figure()
ax=plt.axes(projection='3d')

def f(x,y):
  return np.sin(np.sqrt((x**2)+(y**2)))

x=np.linspace(-2,-5,100)
y=np.linspace(-2,5,100)
X,Y=np.meshgrid(x,y)
Z=f(X,Y)

ax.plot_wireframe(X,Y,Z,cmap="binary")
ax.set_title("3D wiresframe graph using maatplotlib")
plt.show()

