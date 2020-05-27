import numpy as np 
import scipy
import scipy.spatial as spat
from scipy.spatial import ConvexHull
from matplotlib import pyplot as plt
from polygon_generator import polygon2D
np.random.seed(5)

points = polygon2D(100,50)
#print(np.shape(points))
#print(f"Array of vertices: \n {points}")
#print(f"First vertex: \n {points[:,0]}")
polygon = ConvexHull(np.transpose(points))

fig1 = plt.figure()
ax11 = fig1.add_axes()
plt.scatter(points[0,:],points[1,:])
for simplex in polygon.simplices:
    plt.plot(points[0,simplex], points[1,simplex], 'k-')
plt.show()


