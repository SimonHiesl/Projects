import numpy as np
import secrets

def give_rd_centers():
    rd_centers = []
    centers = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
    for i in range(24):
        color = secrets.choice(centers)
        rd_centers.append(color)
        centers.remove(color)
    return rd_centers

def check_no_bars(sample_size=100000):
    count = 0
    for i in range(sample_size):
        scramble = give_rd_centers()
        x = 0
        for i in [0, 4, 8, 12, 16, 20]:
            if len(set(scramble[0+i:4+i])) == 4:
                x += 1
        if x == 6:
            count += 1
    return count/sample_size*100

print(check_no_bars())
