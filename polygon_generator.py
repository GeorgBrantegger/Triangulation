import numpy as np
import shapely
import shapely.geometry
from shapely.geometry import Polygon

def polygon2D():
    polygon_obj = Polygon([[0,0],[1,0],[1,1],[0,1]])
    return polygon_obj