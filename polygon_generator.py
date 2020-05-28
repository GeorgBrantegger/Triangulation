from shapely.geometry import Polygon
import random
import math

def polygon2D(n,r):
    corners = []
    for i in range(n):
        rand_var = random.random()
        x = round(r*math.cos((1+0.15*rand_var)*(i/n)*2*math.pi),2)
        y = round(r*math.sin((1+0.15*rand_var)*(i/n)*2*math.pi),2)
        corners.append([x,y])

    polygon_obj = Polygon(corners)
    return polygon_obj