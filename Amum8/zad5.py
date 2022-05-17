import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

sc = ax.scatter([1,2,1,2],[1,2,3,3])

def fun(ev):
    print(sc.contains(ev))

fig.canvas.mpl_connect('motion_notify_event',fun)
plt.show()