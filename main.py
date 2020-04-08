from alg_forel import forel
from alg_forel import show_picture as s_pic
import numpy as np
import PySimpleGUI as sg

layout_num = [[sg.Text('Ввдеите количество исследуемых объектов в выборке:')],
              [sg.Input(key='num', size=(5, 10)), sg.Text('Не более 15 объектов')],
              [sg.Button('Ввести'), sg.Exit('Выход')]]

layout_main = [[sg.Text('Введите координаты исследуемых объектов')],
               [sg.Text('   № \nобъекта'), sg.Text('Координата Х'), sg.Text('Координата У')],
               [sg.Text('')],
               [sg.Text('Введите радиус гиперсферы'), sg.Input(key='radius', size=(7, 3))],
               [sg.Button('Начать исследование'), sg.Exit('Выход')],
               [sg.Output(size=(40, 10))],
               ]

window = sg.Window('Задание количества точек', layout_num)

while True:  # The Event Loop
    event, values = window.read()
    values['num'] = values['num'].replace(',', '.').split()[0]
    if int(values['num']) < 1:
        values['num'] = str(1)
        sg.popup('Вы ввели значение меньше единицы, поэтому выведу я вам всего одну строку!')
    elif int(values['num']) > 15:
        values['num'] = str(15)
        sg.popup('Вы ввели значение больше 15, поэтому выведу я вам 15 строк!')
    i = 0
    while i < int(values['num']):
        string = [sg.Text('', size=(1, 1)), sg.Text(i + 1, size=(4, 1)), sg.Input(key='num_x' + str(i), size=(8, 1)),
                  sg.Text('', size=(2, 1)), sg.Input(key='num_y' + str(i), size=(8, 1))]
        layout_main.insert(i + 2, string)
        i += 1
    if event in (None, 'Выход'):
        break
    break
window.close()

window = sg.Window('Задание координат точек', layout_main)

while True:
    event, values = window.read()
    print(values)
    if event in (None, 'Выход'):
        break

        #TODO: сделать взятие данных из интерфейса, проверка на запятые и отсутствие данных, передача в логические модули




points = np.array([(7, 9), (6, 9), (6, 8), (2, 3), (1, 3), (1, 2)])

radius = 1.5

a = forel.Forel(points, radius)

a = a.cluster()

print(a[0])
print(a[1])

size = [50, 100]

b = s_pic.Picture(a[0], a[1], radius)
b = b.display()
