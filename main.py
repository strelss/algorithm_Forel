from alg_forel import forel
from alg_forel import show_picture as s_pic
import numpy as np
import PySimpleGUI as sg

layout_num = [[sg.Text('Ввдеите количество исследуемых объектов в выборке:')],
              [sg.Input(key='num', size=(5, 10)), sg.Text('Не более 15 объектов')],
              [sg.Button('Ввести'), sg.Exit('Выход')]
              ]

layout_main = [[sg.Text('Введите координаты исследуемых объектов')],
               [sg.Text('   № \nобъекта'), sg.Text('Координата Х'), sg.Text('Координата У')],
               [sg.Text('')],
               [sg.Text('Введите радиус гиперсферы'), sg.Input(key='radius', size=(7, 3))],
               [sg.Button('Начать исследование'), sg.Submit('Справка'), sg.Exit('Выход')],
               [sg.Output(size=(40, 10))],
               ]

window = sg.Window('Задание количества точек', layout_num)

sg.popup('Запущена программа кластеризации объектов, использующая алгорим "ФОРЕЛЬ-I".\n'
         'Подробная информация содержится в справке.\n'
         '\n'
         'dndia v.1.0')
exit = False
while True:  # The Event Loop
    event, values = window.read()
    if event in (None, 'Выход'):
        exit = True
        break
    if values['num'] == '':
        sg.popup('Введите число объектов!')
    else:
        values['num'] = values['num'].replace(',', '.').split()[0]
        obj_num = round(float(values['num']))
        if round(float(values['num'])) < 1:
            values['num'] = str(1)
            sg.popup('Вы ввели значение меньше единицы, поэтому выведу я вам всего одну строку!')
        elif round(float(values['num'])) > 15:
            values['num'] = str(15)
            sg.popup('Вы ввели значение больше 15, поэтому выведу я вам 15 строк!')
        i = 0
        while i < round(float(values['num'])):
            string = [sg.Text('', size=(1, 1)), sg.Text(i + 1, size=(4, 1)),
                      sg.Input(key='num_x' + str(i), size=(8, 1)),
                      sg.Text('', size=(2, 1)), sg.Input(key='num_y' + str(i), size=(8, 1))]
            layout_main.insert(i + 2, string)
            i += 1
        break
window.close()

window = sg.Window('Задание координат точек', layout_main)

while True:

    if exit:
        sg.popup('Программа закрыта из-за отсутствия даных.')
        break

    event, values = window.read()


    if event == 'Начать исследование':
        def main():
            print('Начало исследования:')
            print('Обработка введенных данных.')
            points = []
            i = 0
            tech = []
            for key in values.keys():
                if values[key] == '':
                    tech.append(values[key])
            if '' in tech:
                sg.popup('Введите все данные в значениях!')
                print('Данные не корректны.')
            else:
                while i < len(values) / 2 - 1:
                    a = (float(values['num_x' + str(i)].replace(',', '.').split()[0]),
                         float(values['num_y' + str(i)].replace(',', '.').split()[0]))
                    points.append(a)
                    i += 1
                points = np.array(points)       #Выходной массив точек
                radius = float(values['radius'].replace(',', '.').split()[0])       #Выходной радиус
                print()
                print('Массив координат объектов: ' + str(points))
                print('Радиус гиперсфер: ' + str(radius))
                print()
                print('Обработка данных завершена.')
                print('____________________________')
                print()

                print('Инициализация первого модуля.')
                print()
                first_module = forel.Forel(points, radius)
                first_module = first_module.cluster()
                print()
                print('Первый модуль расчетов завершен.')
                print('____________________________')
                print()

                print('Инициализация второго модуля.')
                print()
                second_module = s_pic.Picture(first_module[0], first_module[1], radius)
                print('Вывод изображения.')
                print()
                second_module = second_module.display()
                print('Второй модуль расчетов завершен.')
                print('____________________________')
                print()

        main()

    if event == 'Справка':
        sg.popup(
            'Данная программа разбивает на кластеры введенную выборку из объектов используя алгоритм кластеризации "ФОРЕЛЬ-I".\n'
            'Алгоритм не совершенен, и будет еще дорабатываться.\n'
            'Метод расчета был позаимствован из книги "Методы распознавания и их применение" автора д.т.н., профессора Н.Г.Загоруйко. \n'
            'Издательство "Советское радио", Москва 1972, стр. 96, 100-103.\n'
            '\n'
            'dndia v.1.0')

    if event in (None, 'Выход'):
        break


# points_exemple = np.array([(7, 9), (6, 9), (6, 8), (2, 3), (1, 3), (1, 2)])

