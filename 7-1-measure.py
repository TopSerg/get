import RPi.GPIO as gpio
import time
import matplotlib.pyplot as plt

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17

gpio.setup(dac, gpio.OUT)
gpio.setup(leds, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def binu(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def val():
    return gpio.input(comp)

#Подсветка
def svet(i):
    n = int(i*9/256)
    for j in range(8):
        if j < n:
            gpio.output(leds[j], 1)
        else:
            gpio.output(leds[j], 0)

#АЦП
def adc():
    left = -1
    right = 256
    while right - left > 1:
        mid = int((left + right)/2)

        value = binu(mid)
        gpio.output(dac, value)

        time.sleep(0.0005)

        compvalue = val()

        if compvalue == 0:
            right = mid
        else:
            left = mid
    return mid

#Функция визуализации
def vizulaz(x, y):
    plt.plot(x, y)
    plt.show()
        

try:
    #инициализация переменных
    value = []
    timebefore = time.clock()
    gpio.output(troyka, 1)
    U = adc()

    #Зарядка конденсатора
    while U < 62:
        U = adc()
        value.append(U)
        print(U)
        svet(U)
    gpio.output(troyka, 0)
    while U < 224:
        U = adc()
        value.append(U)
        print(U)
        svet(U)
    
    
    #Разрядка конденсатора
    gpio.output(troyka, 1)
    while U < 224:
        U = adc()
        value.append(U)
        print(U)
        svet(U)

    #Вычисление шага
    timeafter = time.clock()
    long = timeafter - timebefore
    mas = list(range(len(value)))
    print(mas)
    vizulaz(mas, value)

    #Запись в файлы
    data = open('data.txt', 'w')
    settings = open('settings.txt', 'w')

    for i in value:
        data.write(str(i) + '\n')

    data.close()

    ch = len(mas)/long
    print('2 ' + str(ch))
    settings.write('2 ' + str(ch))
    
    settings.close()

        
finally:
    gpio.output(dac, 0)
    gpio.output(leds, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()