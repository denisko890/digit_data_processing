import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import csv

time = 0.1
amplitude = 0.9
smeshenie = -0.5
phase = math.pi * 80/180
w = 2 * math.pi * 21972.65625
dpi = 50
fig = plt.figure(dpi = dpi, figsize = (1280 / dpi, 720 / dpi))

plt.axis([0, time , -1.5, 0.5])

plt.title('Дискретный')
plt.xlabel('t, с')
plt.ylabel('U, В')

xs = []
cos_vals = []

x = 0.0

csvdata = [[]]
while x <= time :
    cos_vals_point = amplitude * math.cos(w * x + phase) + smeshenie
    cos_vals.append(cos_vals_point)
    csvdata.append([x, cos_vals_point])
    xs += [x]
    x += math.pow(100000, -1)

discretePoints = open('discretePoints.csv', 'w')
with discretePoints:
    writer = csv.writer(discretePoints)
    writer.writerows(csvdata)

plt.plot(xs, cos_vals, '.', label = 'Discrete cos(x)')

plt.legend(loc = 'upper right')
fig.savefig('discrete.png')