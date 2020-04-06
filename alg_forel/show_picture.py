import matplotlib.pyplot as plt
from matplotlib.patches import Circle

class Picture:
    '''
    Данный класс реализует вывод графика с исследуемыми точками (в виде кружков), центроидов (в виде крестика или буквы "х")
    и окружностей (гиперсфер) кластеров с центром в точках центров масс (центроидов).
    '''
    def __init__(self, centroids, points, radius):
        '''
        Иинициализация.
        :param centroids: список массивов
        :param points:  список массивов
        :param radius: челое или дробное число
        '''
        self.centroids = centroids
        self.data = points
        self.radius = radius


    def display(self):
        '''
        Метод обрабатывает данные и возвращает картинку (график).
        :return: картинка в виде графика
        '''
        self.data_x = []    # точки по оси х
        self.data_y = []    # точки по оси у
        self.centroids_x = []       # центры масс (центроиды) по оси х
        self.centroids_y = []       # центры масс (центроиды) по оси у
        fig = plt.figure()          # создание фигуры
        pic = fig.add_subplot(111)
        for point in self.data:     #наполняем координатами массивы точек
            for item in point:
                self.data_x.append(item[0])
                self.data_y.append(item[1])
        pic.scatter(self.data_x, self.data_y)       #вывод исследуемых точек
        for point in self.centroids:        #наполняем координатами массивы ценров масс и сразу выводим окружности (гиперсферы)
            self.centroids_x.append(point[0])
            self.centroids_y.append(point[1])
            self.circle = Circle((point[0], point[1]), self.radius, fill=False,  edgecolor='b')
            pic.add_artist(self.circle)
        pic.scatter(self.centroids_x, self.centroids_y, marker='x')         #вывод центров масс
        plt.show()          # показ рисунка