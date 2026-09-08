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
        sd_list.append(np.std(a[:,i]))
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
print(data[20])
data = rescale(data)


va_index = 46
va = data[va_index]
n_row = data.shape[0]
max_similar = -1
index = 0
sim_arr = []
for i in range(n_row):
    if i != va_index:
        sim = similarity(data[i],va)
        sim_arr.append(sim)
        if sim > max_similar:
            max_similar = sim
            index = i

print(max_similar)
print(index) #The state most similar to Virginia is Maryland
