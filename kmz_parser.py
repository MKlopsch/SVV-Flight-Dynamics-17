import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as md

time1 = np.genfromtxt("time1.txt", dtype=None)
time1_datetime = []
for i in range(len(time1)):
    time1_datetime.append(datetime.strptime(time1[i], '<when>%Y-%m-%dT%H:%M:%SZ</when>'))

f = open("coord1.txt")
data = f.readlines()
f.close()
for i in range(len(data)):
    if i == len(data) - 1:
        data[i] = (data[i][10:])[:-11]
    else:
        data[i] = (data[i][10:])[:-12]

coord1 = np.genfromtxt(data)

time2 = np.genfromtxt("time2.txt", dtype=None)
for i in range(len(time2)):
    time2[i] = datetime.strptime(time2[i], '<when>%Y-%m-%dT%H:%M:%SZ</when>')

f = open("coord2.txt")
data = f.readlines()
f.close()
for i in range(len(data)):
    if i == len(data) - 1:
        data[i] = (data[i][10:])[:-11]
    else:
        data[i] = (data[i][10:])[:-12]

coord2 = np.genfromtxt(data)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot_date(time1_datetime, coord1[:, 2], linestyle="solid", marker=None)
xfmt = md.DateFormatter('%H:%M')
ax.xaxis.set_major_formatter(xfmt)
plt.show()
