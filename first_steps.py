import numpy as np 
import scipy
import scipy.spatial as spat
from matplotlib import pyplot as plt
from polygon_generator import polygon2D
from scipy.spatial import Delaunay
np.random.seed(5)


polygon_obj = polygon2D() # hardcoded for the moment
#returs a shapely.geometry.polygon.Polygon
print(type(polygon_obj))


corners = np.array(polygon_obj.exterior)




