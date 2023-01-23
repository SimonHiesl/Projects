from mpmath import mp
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

mp.dps = 1+1000000
pi = str(mp.pi)[2:]

#Distribution of two digit (PAO) pairs in Pi

pi_pairs = []
i=0
while i < 1014:
    pi_pairs.append(str(pi[i])+str(pi[i+1]))
    i+=2

count_pairs = np.zeros(100)
for n in pi_pairs:
    count_pairs[int(n)] += 1
count_pairs = list(count_pairs.astype(int))

print("Number of pairs:")
print(count_pairs)

print("\nMost common pair:")
print(count_pairs.index(max(count_pairs)))

print("\nDistribution:")
list_hist = []
for i in range(max(count_pairs)+1):
    list_hist.append(count_pairs.count(i))
print(list_hist)

print("\nAverage:")

print(round(np.average(np.average(list_hist)),2), "+/-", np.round(np.std(list_hist),2))

plt.bar(np.arange(max(count_pairs)+1),list_hist)
plt.show()

#Distribution of the digits in Pi

pi_vec = []
for i in range(1014):
    pi_vec.append(int(pi[i]))

count = []
for i in range(10):
    count.append(np.count_nonzero(np.array(pi_vec) == i))

print("Distribution:")
print(count)

print("\nAverage:")

print(round(np.average(np.average(count)),2), "+/-", np.round(np.std(count),2))

plt.bar(np.arange(10),count)
plt.show()