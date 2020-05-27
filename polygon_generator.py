import numpy as np 
import scipy

def polygon2D(n,r):
    # n = number of vertices
    # r = range = max distance from (0,0,0)
    vertices = r*np.round(np.random.rand(2,n),2)
    return vertices

