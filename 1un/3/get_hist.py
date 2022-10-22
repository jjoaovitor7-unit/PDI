import numpy as np

def get_hist(img, limit):
    arr = img.flatten()
    hist = np.zeros(limit,dtype='int')
    for i in range(0, len(arr)):
        hist[arr[i]] +=1
    return hist