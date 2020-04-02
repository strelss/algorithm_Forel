import numpy as np

points = np.array([(7, 9), (6, 9), (6, 8), (2, 3), (1, 3), (1, 2)])
radius = 10



def cluster(points, radius):
    centroids = []
    while len(points) != 0:
        current_point = get_random_point(points)
        neighbors = get_neighbors(current_point, radius, points)
        centroid = get_centroid(neighbors)
        while np.linalg.norm(current_point - centroid) > 0:
            current_point = centroid
            neighbors = get_neighbors(current_point, radius, points)
            centroid = get_centroid(neighbors)
        points = remove_points(neighbors, points)
        centroids.append(current_point)
    return centroids


def get_centroid(points):
    return np.array([np.mean(points[:, 0]), np.mean(points[:, 1])])


def get_random_point(points_loc):
    random_index = np.random.choice(len(points_loc), 1)[0]
    return points_loc[random_index]

def get_neighbors(c_p, radius, points):
    neighbors = []
    for point in  points:
        if np.linalg.norm(c_p - point) < radius:
            neighbors.append(point)
    return np.array(neighbors)

def remove_points(neighbors_curr, points_cur):
    points = []
    for point in points_cur:
        if point not in neighbors_curr:
            points.append(point)
    return points


print(cluster(points, radius))
