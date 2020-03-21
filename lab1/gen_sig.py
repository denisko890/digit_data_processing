import matplotlib as mpl
import matplotlib.pyplot as plt
import math

time = 0.1*0.005
amplitude = 0.9
smeshenie = -0.5
phase = math.pi * 80/180
w = 2 * math.pi * 21972.65625
dpi = 50
fig = plt.figure(dpi = dpi, figsize = (1280 / dpi, 720 / dpi))
mpl.rcParams.update({'font.size': 10})

plt.axis([0, time , -1.5, 0.5])

plt.title('Сигнал')
plt.xlabel('t, с')
plt.ylabel('U, В')

xs = []
cos_vals = []

x = 0.0


while x <= time :
    cos_vals += [ amplitude * math.cos(w * x + phase) + smeshenie ]
    xs += [x]
    x += 0.000001


cos_vals_test = amplitude * math.cos(w * 0.05 + phase) + smeshenie
print (cos_vals_test)
plt.plot(xs, cos_vals, color = 'red', linestyle = 'solid',
         label = 'cos(x)')

plt.legend(loc = 'upper right')
fig.savefig('Reports/cosinus5.png')