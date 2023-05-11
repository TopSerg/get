import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

data = open('data.txt', 'r')
settings = open('settings.txt', 'r')

datastr = data.read()
datamas = datastr.split('\n')
mas = list(range(len(datamas)))
for i in range(len(datamas)):
    datamas[i] = float(datamas[i])
for i in range(len(mas)):
    mas[i] = float(mas[i])

settingsmas = settings.read().split(' ')

datamas = np.array(datamas)
mas = np.array(mas)

print (datamas)

datamas *= float(settingsmas[0])
mas /= float(settingsmas[1])

figure, axis = plt.subplots(figsize = (150, 40))

axis.set_title("Процесс заряда и разряда конденсатора в RC-цепочке", \
               loc = "center", fontsize = 20)

axis.set_xlabel("Время $\\tau$, с",  fontsize = 20)
axis.set_ylabel("Напряжение $U$, В", fontsize = 20)


axis.set_xlim(0, len(mas)/float(settingsmas[1]) + 1)
axis.xaxis.set_minor_locator(tkr.MultipleLocator(0.5))
axis.xaxis.set_major_locator(tkr.MultipleLocator(2))

axis.set_ylim(datamas.min(), datamas.max()+0.2)
axis.yaxis.set_minor_locator(tkr.MultipleLocator(0.1))
axis.yaxis.set_major_locator(tkr.MultipleLocator(0.5))

axis.minorticks_on()


axis.plot(mas, datamas, color = 'b',ls = '-', lw = 0.3, markevery=500, label=r'$U(t)$', marker = 's', mfc = 'r')


axis.grid(which = "minor", color = "gray", linestyle = "--")
axis.grid(which = "major", color = "k",    linestyle = "-")

chargeTime = mas[np.argmax(datamas)]

axis.text(20, 2,   "Время зарядки:  " + \
          str(round(chargeTime, 3)), fontsize = 10)

axis.text(20, 1.5, "Время разрядки: " + \
          str(round(mas.max() - chargeTime, 3)), fontsize = 10)


plt.show()

figure.savefig("plot.svg")