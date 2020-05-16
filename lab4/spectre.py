import numpy as np
import matplotlib.pyplot as plt
import timeit
import csv


def read_csv(data, path_to_file, key):
    with open(path_to_file, "r") as f:
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            k = {}
            k["t"] = line["t"]
            k[key] = line[key]
            data.append(k)
        return data

data_signal = []
data_noise = []
data_sn = []

data_signal = [(i["Us"]) for i in read_csv(data_signal, "lab1/discretePoints.csv", "Us")]
data_noise = [(i["Un"]) for i in read_csv(data_noise, "lab2/report/noise.csv", "Un")]
data_sn = [(i["Usn"]) for i in read_csv(data_sn, "lab3/report/9_sn.csv", "Usn")]

fft_signal = np.fft.fft(data_signal)
freq = np.fft.fftfreq(10000, 0.00001)
freq2 = np.fft.fftfreq(8192, 0.00001)
data_noise = np.fft.fft(data_noise)
data_sn = np.fft.fft(data_sn)

for i in range(len(freq)):
    if freq[i] == 21970:
        print(f"Номер отсчета +w: {i}")
    if freq[i] == -21970:
        print(f"Номер отсчета -w: {i}")

power_signal = (np.abs(data_sn[2197]) ** 2 + np.abs(data_sn[7803]) ** 2)
snr = power_signal / (sum([i ** 2 for i in np.abs(data_sn)]) - power_signal)
print(f"Практическое отношение SNR: {snr}")

fig = plt.figure(dpi = 100, figsize = (1280 / 100, 720 / 100))
plt.plot(freq, np.abs(fft_signal) / 10000, color = 'red', linestyle = 'solid', label = 'Амплитудный спектр сигнала')
plt.title('Амплитудный спектр сигнала')
plt.xlabel('Частота, Гц')
plt.ylabel('Напряжение Us, В')
plt.grid()
fig.savefig('lab4/Reports/spectre_signal.png')
plt.axis([20973, 22973, - 0.02, 0.55])
fig.savefig('lab4/Reports/spectre_signal_5.png')
plt.close()
fig = plt.figure(dpi = 100, figsize = (1280 / 100, 720 / 100))
plt.plot(freq, np.abs(data_noise) / 10000, color = 'red', linestyle = 'solid', label = 'Амплитудный спектр шума')
plt.title('Амплитудный спектр шума')
plt.xlabel('Частота, Гц')
plt.ylabel('Напряжение Un, В')
plt.grid()
fig.savefig('lab4/Reports/noise.png')
plt.close()
fig = plt.figure(dpi = 100, figsize = (1280 / 100, 720 / 100))
plt.plot(freq, np.abs(data_sn) / 10000, color = 'red', linestyle = 'solid', label = 'Амплитудный спектр смеси')
plt.title('Амплитудный спектр смеси')
plt.xlabel('Частота, Гц')
plt.ylabel('Напряжение Us, В')
plt.grid()
fig.savefig('lab4/Reports/signal_noise.png')
plt.axis([21920, 22020, - 0.02, 0.55])
fig.savefig('lab4/Reports/signal_noise_5.png')
plt.close()