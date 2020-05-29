import numpy as np 
from matplotlib import pyplot as plt
from polygon_generator import polygon2D
from triangulation import convex_polygon_triangulation
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
import random
import math
random.seed(42)


polygon_obj = polygon2D(8,10) # n= number of corner, r = distance from (0,0)
#returs a shapely.geometry.polygon.Polygon

corners = np.array(polygon_obj.exterior) # for plotting
#print(corners)

tri = convex_polygon_triangulation(corners)
#####################################################################
triangles = np.asarray(corners[tri.simplices])
#print(triangles)
num_triangles = np.shape(triangles)[0]
num_dim = 2

#print(np.shape(triangles)[0])

edgelength = np.zeros([num_triangles,3,3])
max_edgelength_indices = np.zeros([num_triangles,1,2])
for i in range(num_triangles):
    max_j = 0
    max_k = 0
    max_length = 0
    for j in range(3):
        for k in range(3):
            edgelength[i,j,k] = np.linalg.norm(triangles[i,j]-triangles[i,k])
            if edgelength[i,j,k] > max_length:
                max_edgelength_indices[i] = [j,k]
                max_length = edgelength[i,j,k]

#print(edgelength)
#print(max_edgelength_indices)
#print(triangles)

points_longest_edges = np.zeros([num_triangles,2,num_dim])
edge_vectors = np.zeros([num_triangles,1,num_dim])
for i in range(num_triangles):
    for j in range(2):
        points_longest_edges[i,j,:] = triangles[i,int(max_edgelength_indices[i,0,j])]
    edge_vectors[i,0] = (points_longest_edges[i,0,:]-points_longest_edges[i,1,:])#/ \
        #(np.sqrt(np.square(points_longest_edges[i,0,0]-points_longest_edges[i,1,0])+ \
            #np.square(points_longest_edges[i,0,1]-points_longest_edges[i,1,1])))


#print(points_longest_edges)
#print(edge_vectors)

def orthogonal_projection(P1,P2,vec):
    #P1 and vec form the base line (in this case the longest side of the triangle)
    #P2 is the third corner of the triangle not on the straigth P1+x*vec
    S = P1+vec*(np.dot((P2-P1),vec)/np.square(np.linalg.norm(vec)))
    return S 

base_points = np.zeros([num_triangles,1,num_dim])
vertices = np.zeros([num_triangles,1,num_dim])

for i in range(num_triangles):
    #workaround because I am bad at indexing -> what are the coordinates of the third point of the triangle?
    vertices[i] = sum(triangles[i])- \
        triangles[i,int(max_edgelength_indices[i,0,0])]- \
            triangles[i,int(max_edgelength_indices[i,0,1])]
    base_points[i] = orthogonal_projection(points_longest_edges[i,0],vertices[i],edge_vectors[i,0])

#print(sum(triangles[0]))
#print(sum(triangles[0])-triangles[0,0])
#print(base_points)

""" print(base_points)
print(points_longest_edges)
print(vertices) """

#print(np.shape(base_points))
#print(np.shape(points_longest_edges))
#print(np.shape(vertices))
#print(np.shape(triangles))
#print(triangles)


triangles_right = np.zeros([2*num_triangles,3,num_dim])

""" print(np.shape(triangles_right))
print(np.shape(base_points))
print(np.shape(vertices))
print(np.shape(points_longest_edges))

print(triangles_right[0])
print(base_points[0,0])
print(vertices[0,0])
print(points_longest_edges[0,0]) """

for i in range(num_triangles):
    #print([2*i,2*i+1])
    triangles_right[2*i] = np.vstack((base_points[i,0],vertices[i,0],points_longest_edges[i,0]))
    triangles_right[2*i+1] = np.vstack((base_points[i],vertices[i],points_longest_edges[i,1]))

print(type(triangles_right))




#plotting
fig1, axs1 = plt.subplots()
axs1.plot(*polygon_obj.exterior.xy)
axs1.axis('equal')

fig2, axs2 = plt.subplots()
axs2.triplot(corners[:,0],corners[:,1],tri.simplices)
axs2.scatter(corners[:,0],corners[:,1],c='r')
axs2.scatter(base_points[:,0,0],base_points[:,0,1],c='k')
axs2.axis('equal')
plt.show()


fig3, axs3 = plt.subplots()
for i in range(2*num_triangles):
    axs3.plot(triangles_right[i,:,0],triangles_right[i,:,1])

axs3.axis('equal')
plt.show()
