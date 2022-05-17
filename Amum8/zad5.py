import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,AnnotationBbox)

with open('animals.npz', 'rb') as f:
  animals = np.load(f)['animals']

images = [matplotlib.image.imread(file) for file in glob.glob("animals/*.jpg")]

fig, ax = plt.subplots()

imgboxs = []
for i in range(len(images)):
    imgboxs.append(OffsetImage(images[i], zoom=0.2))
    imgboxs[i].image.axes = ax

points =[]
for i in range(len(images)):
    points.append(AnnotationBbox(
        imgboxs[i], [1,1],
        xycoords='data',
        xybox=(float(animals[i,2]),float(animals[i,3])),
        boxcoords="offset points",
        arrowprops=dict(arrowstyle="->"))
        )

for i in range(len(images)):
    ax.add_artist(points[i])
    points[i].set_visible(False)

sc = ax.scatter(animals[:,2],animals[:,3])

def fun(ev):
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