import numpy as np 
import matplotlib.pyplot as plt

def f(x,y): return 0.5*np.sin(x**3) + 0.25*np.sin((y + np.pi)**2)

def my_mg(x,y):
    X = [x] * len(y)
    Y = np.array([y]*len(x))
    return X, Y.T

n = 100
x = np.linspace(-np.pi/2,np.pi/2,n)
y = np.linspace(-np.pi,np.pi/2,n)

X,Y = np.meshgrid(x,y)

Z = f(X,Y)

plt.contourf(X,Y,Z,cmap='jet', alpha=0.5)
plt.contour(X,Y,Z,  colors='black', linewidths=1.2)

plt.show()




