import matplotlib.pyplot as plt



def display(data, centroids):
    data_x = []
    data_y = []
    centroids_x = []
    centroids_y = []
    for point in data:
        data_x.append(point[0])
        data_y.append(point[1])
    for point in centroids:
        centroids_x.append(point[0])
        centroids_y.append(point[1])
    plt.plot(data_x, data_y)
    plt.show()