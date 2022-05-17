import numpy as np 
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3

def f(x,y): return 0.5*np.sin(x**3) + 0.25*np.sin((y + np.pi)**2)

def my_mg(x,y):
    X = [x] * len(y)
    Y = np.array([y]*len(x))
    return X, Y.T

n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
y = np.linspace(-np.pi,np.pi/2,n)
#y = np.linspace(0,np.pi*1.5,n)

X,Y = np.meshgrid(x,y)

fig = plt.figure()

ax = p3.Axes3D(fig)
ax.set_xlim3d([-np.pi/2,np.pi/2])
# ax.set_ylim3d([0,np.pi*1.5])
ax.set_ylim3d([-np.pi,np.pi/2])
zs = np.array(f(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)
ax.plot_surface(X,Y,Z,cmap="gist_ncar")
plt.show()