import glob
from re import X
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,AnnotationBbox)



with open('animals.npz', 'rb') as f:
  animals = np.load(f)['animals']

images = [matplotlib.image.imread(file) for file in glob.glob("animals/*.jpg")]

fig, ax = plt.subplots()

x = animals[:,2].astype(np.float64)
y = animals[:,3].astype(np.float64)
sc = ax.scatter(x,y)


imgboxs = []
for i in range(len(images)):
    imgboxs.append(OffsetImage(images[i], zoom=0.2))
    imgboxs[i].image.axes = ax

points =[]
for i in range(len(images)):
    points.append(AnnotationBbox(
        imgboxs[i],
        xy = (x[i],y[i]),
        xycoords='data',
        xybox=(x[i],y[i]+10),
        boxcoords="offset points")
        )

for i in range(len(images)):
    ax.add_artist(points[i])
    points[i].set_visible(False)


last = 0

def fun(ev):
    global last
    if sc.contains(ev)[0] != last:
        last = sc.contains(ev)[0]
        if sc.contains(ev)[0]:
            print(int(sc.contains(ev)[1]['ind']))
            points[int(sc.contains(ev)[1]['ind'])].set_visible(True)
            plt.show()
            
        else:
            print('f')
            for i in range(len(images)):
                ax.add_artist(points[i])
                points[i].set_visible(False)
            plt.show()

fig.canvas.mpl_connect('motion_notify_event',fun)
plt.show()