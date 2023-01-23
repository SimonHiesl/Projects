import numpy as np
import matplotlib.pyplot as plt

data1 = np.genfromtxt("./Schafkopf/Abend1.csv", dtype = int, delimiter = ",")
data2 = np.genfromtxt("./Schafkopf/Abend2.csv", dtype = int, delimiter = ",")
data3 = np.genfromtxt("./Schafkopf/Abend3.csv", dtype = int, delimiter = ",")
data4 = np.genfromtxt("./Schafkopf/Abend4.csv", dtype = int, delimiter = ",")

l1 = data1[:,0]
d1 = data1[:,1]
s1 = data1[:,2]
t1 = data1[:,3]

l2 = data2[:,0]
d2 = data2[:,1]
s2 = data2[:,2]
t2 = data2[:,3]

l3 = data3[:,0]
d3 = data3[:,1]
s3 = data3[:,2]
t3 = data3[:,3]

l4 = data4[:,0]
d4 = data4[:,1]
s4 = data4[:,2]
t4 = data4[:,3]

r = np.arange(193)

l = np.concatenate((l1, l2-130, l3-610, l4-230))
d = np.concatenate((d1, d2-310, d3-1310, d4-1990))
s = np.concatenate((s1, s2-50, s3-390, s4-410))
t = np.concatenate((t1, t2+490, t3+2310, t4+2630))

plt.plot(r, l, label = "Lea", color = "orange")
plt.plot(r, d, label = "Domi", color = "red")
plt.plot(r, s, label = "Simon", color = "blue")
plt.plot(r, t, label = "Thomas", color = "green")
plt.plot(r, l + d + s + t, color = "black")
plt.xlabel("Spiele")
plt.ylabel("Gewinne/Verluste in Cent")
fig1 = plt.gcf()
plt.legend()
plt.show()
fig1.savefig("./Schafkopf/Schafkopf_Plot.png", dpi = 500, facecolor = "w", edgecolor = "w", bbox_inches = "tight")