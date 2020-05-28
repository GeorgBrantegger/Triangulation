from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull


def convex_polygon_triangulation(corners):
    tri = Delaunay(corners) # triangulate a convex polygon
    #print(tri.points)
    #print(tri.simplices)
    return tri