import numpy as np 
from matplotlib import pyplot as plt
from polygon_generator import polygon2D
from triangulation import convex_polygon_triangulation
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
import random
random.seed(0)


polygon_obj = polygon2D(5,5) # n= number of corner, r = distance from (0,0)
#returs a shapely.geometry.polygon.Polygon

corners = np.array(polygon_obj.exterior) # for plotting
#print(corners)

tri = convex_polygon_triangulation(corners)

#plotting
fig1 = plt.figure()
fig1.add_subplot(211)
plt.plot(*polygon_obj.exterior.xy)

fig1.add_subplot(212)
plt.triplot(corners[:,0],corners[:,1],tri.simplices)
plt.scatter(corners[:,0],corners[:,1],c='r')
plt.show()

