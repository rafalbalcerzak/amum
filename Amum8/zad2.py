import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation

def f(x, y, t): return 0.5*np.sin(x**3) + 0.25*np.sin((y - t)**2)

n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
y = np.linspace(0,np.pi*1.5,n)

res = [[f(xx, yy, 0) for xx in x] for yy in y]

X,Y = np.meshgrid(x,y)

fig, ax = plt.subplots(figsize=(10,7))

ax.set_xlim(-np.pi/2,np.pi/2)
ax.set_ylim(0,np.pi*1.5)

# uzupełnij (wyświetl obraz za pomocą `contourf` i `contour`).

def animate(i):
    X,Y = np.meshgrid(x,y)
    Z = f(X,Y,i/10)
    plt.clf()
    plt.contourf(X,Y,Z,cmap='jet', alpha=0.5)
    plt.contour(X,Y,Z,  colors='black', linewidths=1.2)

ani = matplotlib.animation.FuncAnimation(fig, animate, frames=80, interval=33, repeat=True) 
plt.show()