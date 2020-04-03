import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import csv
import random

time = 0.1

dpi = 50
fig = plt.figure(dpi = dpi, figsize = (640 / dpi, 360 / dpi))

plt.axis([0, time , -1, 1])

plt.title('Шум')
plt.xlabel('t, с')
plt.ylabel('U, В')

xs = []
noise_list = []

x = 0.0

csvdata = [[]]
while x <= time :
    noise = random.uniform(-1, 1)
    noise_list.append(noise)
    csvdata.append([x, noise])
    xs += [x]
    x += math.pow(100000, -1)

discretePoints = open('report/noise.csv', 'w')
with discretePoints:
    writer = csv.writer(discretePoints)
    writer.writerows(csvdata)

plt.plot(xs, noise_list, '.', label = 'Шум')
fig.savefig('report/noise_full.png')
plt.axis([0.05, 0.055, -1, 1])
plt.legend(loc = 'upper right')
fig.savefig('report/noise_5.png')

av = sum(noise_list)/len(noise_list)
print('Среднее значение: %s' % av)
disp = 0
for i in noise_list:
  disp = disp + pow((i - av), 2)
disp = disp / (len(noise_list) - 1)
print('Дисперсия: %s' % disp)
