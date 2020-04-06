from alg_forel import forel
import numpy as np


import matplotlib.pyplot as plt
import pylab
from matplotlib.patches import Circle

class Picture:
    def __init__(self, centroids, points, radius):
        self.centroids = centroids
        self.data = points
        self.radius = radius


    def display(self):
        self.data_x = []
        self.data_y = []
        self.centroids_x = []
        self.centroids_y = []
        fig = plt.figure()
        pic = fig.add_subplot(111)
        for point in self.data:
            for item in point:
                self.data_x.append(item[0])
                self.data_y.append(item[1])
        pic.scatter(self.data_x, self.data_y)
        for point in self.centroids:
            self.centroids_x.append(point[0])
            self.centroids_y.append(point[1])
            self.circle = Circle((point[0], point[1]), self.radius, fill=False)
            pic.add_artist(self.circle)
        pic.scatter(self.centroids_x, self.centroids_y, marker='x')

        # circle = Circle((5, 5), self.radius, fill=False)

        plt.show()



        print('---------')
        print(self.data_x, self.data_y)















points = np.array([(7, 9), (6, 9), (6, 8), (2, 3), (1, 3), (1, 2)])

radius = 2

a = forel.Forel(points, radius)

a = a.cluster()


print(a[0])
print(a[1])

size = [50, 100]

b = Picture(a[0], a[1], radius)
b = b.display()