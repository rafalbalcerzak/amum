import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation
import mpl_toolkits.mplot3d.axes3d as p3

def f(x, y, t): return 0.5*np.sin(x**3) + 0.25*np.sin((y - t)**2)

def my_mg(x,y):
    X = [x] * len(y)
    Y = np.array([y]*len(x))
    return X, Y.T

n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
# y = np.linspace(-np.pi,np.pi/2,n)
y = np.linspace(0,4,n)

X,Y = np.meshgrid(x,y)

fig = plt.figure()
ax = p3.Axes3D(fig)
# ax.set_ylim3d([-np.pi,np.pi/2])
ax.set_ylim3d([0,4])
ax.set_zlim3d([-0.6,0.6])


def animate(i):
    X,Y = np.meshgrid(x,y)
    zs = np.array(f(np.ravel(X), np.ravel(Y),i/10))
    Z = zs.reshape(X.shape)
    plt.clf()
    ax = p3.Axes3D(fig)
    ax.plot_surface(X,Y,Z,cmap="gist_ncar")
    


ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=33, repeat=False) 

ani.save('3d.gif', writer='imagemagick', fps=22)
plt.show()