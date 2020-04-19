import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import csv

SIGNAL_DATA = []
NOISE_DATA = []
SIG_NOI = []
av = -0.5000865523263179
A_NOISE = 0.9 / (10 ** (1 / 20))
print("Амплитуда шума: %s" % A_NOISE)

def read_csv(data, path_to_file, key):
    with open(path_to_file, "r") as f:
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            k = {}
            k["t"] = line["t"]
            k[key] = line[key]
            data.append(k)
        return data


def main():
    read_csv(SIGNAL_DATA, "lab1/discretePoints.csv", "Us")
    read_csv(NOISE_DATA, "lab2/report/noise.csv", "Un")
    for i in range(len(SIGNAL_DATA)):
        s_n = {}
        s_n["t"] = SIGNAL_DATA[i]["t"]
        s_n["Usn"] = (float(SIGNAL_DATA[i]["Us"]) + (A_NOISE * float(NOISE_DATA[i]["Un"])) - float(av))
        SIG_NOI.append(s_n)
    with open("lab3/report/9_sn.csv", "w", newline="") as sn_csv:
        writer = csv.DictWriter(sn_csv, fieldnames=["t", "Usn"])
        writer.writeheader()
        writer.writerows(SIG_NOI)
    time = 0.1

    dpi = 100
    fig = plt.figure(dpi = dpi, figsize = (1920 / dpi, 1080 / dpi))

    plt.axis([0, time , -2, 2])

    plt.title('Сигнал + Шум')
    plt.xlabel('t, с')
    plt.ylabel('U, В')

    xs = []
    sn_list = []
    for n in SIG_NOI:
        xs.append(float(n["t"]))
        sn_list.append(float(n["Usn"]))
    plt.plot(xs, sn_list, '.', label = 'Сигнал + Шум')
    plt.legend(loc = 'upper right')
    fig.savefig('lab3/report/noise_full.png')
    plt.axis([0.05, 0.055, -2, 2])
    plt.legend(loc = 'upper right')
    fig.savefig('lab3/report/noise_5.png')

if __name__ == "__main__":
    main()