import numpy as np


class Forel:
    '''
    Этот класс реализует алгорим FOREL(Formal element), придуманный
    товарищем Загоруйко Н.Г. и его командой в 60-х годах 20-го столетия.

    Использование:
    - создать класс, передав ему первым аргументом позиции точек в виде массива numpy,
        состоящего списка кортежей, в каждом кортеже - одна точка с координатами х и у
        ( Пример: points = np.array([(7, 9), (6, 9), (6, 8), (2, 3), (1, 3), (1, 2)]) ),
        а вторым аргументом передать радиус кластера (гиперсферы) в виде целого или дробного числа.
    - вызвать метод cluster, который вернет координаты цетроидов всех кластеров, которые образовал алгоритм,
        т.е. точки центров всех кластеров (гиперсфер).
    '''
    def __init__(self, points, radius):
        '''
        Инициализация.
        :param points:  Пример: points = np.array([(7, 9), (6, 9), (6, 8), (2, 3), (1, 3), (1, 2)])
        :param radius:  целочисленное или дробное число
        '''
        self.points = points
        self.radius = radius

    def cluster(self):
        '''
        Основной метод, который работает с остальными методами
        :return:  список из массивов np.array с координатами центроидов найденных кластеров и массив np.array с точками отдельных кластеров
        '''
        self.centroids = []    #Массив центроидов
        self.clusters = []      #Массив точек кластеров
        while len(self.points) != 0:     #выполнять поиск кластеров, пока в массиве присутствуют точки
            self.current_point = self.get_random_point(self.points)      #Взять случайную точку из имеющихся
            self.neighbors = self.get_neighbors(self.current_point, self.radius, self.points)           #взять соседей выбранной точки, которые входят в гиперсферу
            self.centroid = self.get_centroid(self.neighbors)           #определить центр тяжести (центроид) точек, которые находятся в гиперсфере
            while np.linalg.norm(self.current_point - self.centroid) > 0:       #выполнять поиск центра тяжести (центроида), пока его координаты не перестанут меняться (разность первого и второго не будет равна нулю)
                self.current_point = self.centroid
                self.neighbors = self.get_neighbors(self.current_point, self.radius, self.points)
                self.centroid = self.get_centroid(self.neighbors)
            self.points = self.remove_points(self.neighbors, self.points)           #удалить точки кластера из общей выборки
            self.centroids.append(self.current_point)           #занести координаты найденного центра тяжести в массив цетроидов
        return self.centroids, self.clusters            #Возврат массива центра масс (центроидов) и массива с точками кластеров (отдельными списками в общем списке)

    def get_centroid(self, points_loc):         #метод поиска центра тяжести (цетроида)
        self.centroid_loc = np.array([np.mean(points_loc[:, 0]), np.mean(points_loc[:, 1])])        #np.mean() высчитывает среднее значение в координатах точек
        return self.centroid_loc

    def get_random_point(self, points_loc):     #метод выбора случайной точки
        self.random_index = np.random.choice(len(points_loc), 1)[0]
        return points_loc[self.random_index]

    def get_neighbors(self, c_p, radius, points):       #метод взятия всех соседей исследуемой точки, входящие в заданный радиус
        self.neighbors = []
        for point in points:
            if np.linalg.norm(c_p - point) < radius:        #np.linalg.norm() каким-то образом связано с Эвклидовым расстоянием (наверно), не разобрался еще, но у пиндоса работал, и у меня сработало
                self.neighbors.append(point)
        return np.array(self.neighbors)

    def remove_points(self, neighbors_curr, points_cur):      #метод удаления точек образованного кластера из общей выборки и возвращает точки кластера в массив точек кластеров
        self.points = []
        self.cls = []
        for self.point in points_cur:
            if self.point not in neighbors_curr:
                self.points.append(self.point)
            else:
                self.cls.append(self.point)
        self.clusters.append(self.cls)
        return self.points