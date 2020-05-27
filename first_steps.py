import numpy as np 
import scipy
from matplotlib import pyplot as plt
from polygon_generator import polygon2D

np.random.seed(5)

polygon_vertices = polygon2D(8,5)
#print(f"Array of vertices: \n {polygon_vertices}")
#print(f"First vertex: \n {polygon_vertices[:,0]}")
#polygon_obj = scipy.spatial.ConvexHull(polygon_vertices)


fig1 = plt.figure()
ax11 = fig1.add_axes()
plt.scatter(polygon_vertices[0,:],polygon_vertices[1,:])
plt.show()







