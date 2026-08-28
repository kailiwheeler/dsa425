import numpy as np
import math

def rescale(a):
    a_scaled = a
    n_row = a.shape[0]
    n_col = a.shape[1]
    mean_list = []
    sd_list = []

    for i in range(n_col):
        mean_list.append(np.mean(a[:,i]))
        sd_list.append(np.mean(a[:,i]))
    for c in range(n_col):
        for r in range(n_row):
            a_scaled[r,c] = (a[r,c]-mean_list[c])/sd_list[c]
            

    return a_scaled

def similarity(u,v):
    d = dot(u,v)
    mag_u = mag(u)
    mag_v = mag(v)
    return d/(mag_u * mag_v)

def dot(u,v):
    d = 0
    
    for i in range(len(u)):
        d = d + ( u[i] * v[i] ) 
    return d

def mag(x):
    m = 0
    for i in x:
        m = m + (i**2)
    return math.sqrt(m)

data = np.genfromtxt('state_facts-1.csv', delimiter = ',' ,  skip_header=1)
data = data[:,1:]
data = rescale(data)

va = data[46]
n_row = data.shape[0]
max = -1
index = 0
sim_arr = []
for i in range(n_row):
    if i != 46:
        sim = similarity(data[i],va)
        sim_arr.append(sim)
        if sim > max:
            max = sim
            index = i

print(max)
print(index) #The state most similar to Virginia is North Carolina

