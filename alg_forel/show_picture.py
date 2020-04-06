import matplotlib.pyplot as plt
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
            self.circle = Circle((point[0], point[1]), self.radius, fill=False,  edgecolor='b')
            pic.add_artist(self.circle)
        pic.scatter(self.centroids_x, self.centroids_y, marker='x')
        plt.show()