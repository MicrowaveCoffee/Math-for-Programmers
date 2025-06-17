import math
import matplotlib
from draw3d import *
from draw2d import *
from colors import *
import os
from matplotlib.patches import Polygon, FancyArrowPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from math import sqrt, sin, cos, pi, atan2, acos
from random import random


#Utility Functions ------------------------------------
def add(*vectors):
    return tuple(map(sum,zip(*vectors)))

def subtract(v1,v2):
    return tuple(v1-v2 for (v1,v2) in zip(v1,v2))

def length(v):
    return sqrt(sum([coord ** 2 for coord in v]))

def scale(s,vector):
    return tuple(s * v for v in vector)

def dot(u,v):
    return sum([coord_1*coord_2 for coord_1,coord_2 in zip(u,v)])

def cross_product(u,v):
    ux,uy,uz = u
    vx,vy,vz = v

    return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)


def angle_between(v1,v2):
    return acos (
        dot(v1,v2) /
        (length(v1) * length(v2))
    )


def to_cartesian(polar_vector):
    distance, angle = polar_vector[0],polar_vector[1]
    return (distance*cos(angle),distance*sin(angle))


# vector = (-1,-2,2)

# draw3d(
#     Arrow3D(vector),
#     Points3D(vector),
#     Box3D(vector)
# )

# pm1 =  [1,-1]
# vertices = [(x,y,z) for x in pm1 for y in pm1 for z in pm1]
# edges = [((-1,y,z),(1,y,z)) for y in pm1 for z in pm1] +\
#             [((x,-1,z),(x,1,z)) for x in pm1 for z in pm1] +\
#             [((x,y,-1),(x,y,1)) for x in pm1 for y in pm1]

# draw3d(
#     Points3D(*vertices, color=blue),
#     *[Segment3D(*edge) for edge in edges]
# )

# vector1 = (4,0,3)
# vector2 = (-1,0,1)
# # Exercise 3.26 ----------------
# draw3d(
#     Arrow3D(vector1, color = blue),
#     Arrow3D(vector2, color= blue),
#     Arrow3D(add(vector1,vector2), vector1),
#     Arrow3D(add(vector1,vector2), vector2),
#     # Arrow3D(vector2, vector1),
#     Arrow3D(add(vector1,vector2), color=green)
# )


# Exercise 3.5 Mini Project

# vs = [(sin(pi*t/6),cos(pi*t/6),1.0/3)for t in range(0,24)]

# total_sum = (0,0,0)
# arrows = []
# for v in vs:
#     next_sum = add(total_sum,v)
#     arrows.append(Arrow3D(next_sum, total_sum))
#     total_sum = next_sum


# draw3d(
#     *arrows
# )


# vectors = []
# for i in range(36):
#     angle = pi * i/9
#     radius = 0.5 + 0.3 * sin(pi* i/18)
#     x = radius * cos(angle)
#     y = radius * sin(angle)
#     z = 0.1 * i
#     vectors.append((x,y,z))

# position = (0,0,0)
# path_arrows = []
# for v in vectors:
#     new_position = add(position,v)
#     path_arrows.append(Arrow3D(position, new_position))
#     position = new_position  
# draw3d(*path_arrows)


# def scale(scaler,vector):
#     return tuple(scaler * coord for coord in vector)

#-----Exercise 3.9 
# def vectors_with_whole_number_length(max_coord = 100):
#     for x in range(1,max_coord):
#         for y in range(1, x+1):
#             for z in range(1,y+1):
#                 if length((x,y,z)).is_integer():
#                     yield (x,y,z)

# for vector in vectors_with_whole_number_length(20):  # Using smaller max for testing
#     print(vector)


#Exercise 3.10 Normalizing a vector
# box = length((-1,-1,2))
# s = scale(1/box,(-1,-1,2))
# print(length(s))


# print(dot((3,0,3),(1,2,-1)))

# print(angle_between((1,2,2),(2,2,1)))

# #Exercise 3.11

# print(dot((-4,1),(1,2)))
# print(dot((-4,1),(4,2)))
# print(dot((1,2),(4,2)))

# Exercise 3.12
# print(dot((-1,-1,1),(1,2,1)))


#Exercise 3.13

# def proof(real_num,v1,v2):
#     print(dot((scale(real_num,v1)),v2))
#     print(dot(v1,(scale(real_num,v2))))
#     print(real_num * dot(v1,v2))

# proof(2,(1,1,1),(2,2,2))

#Exercise 3.15
# def find_similar_lengths(l):
#     return to_cartesian((l,2*pi*random()))

# pairs = [(find_similar_lengths(3),find_similar_lengths(7))
#             for i in range(0,3)]

# for u,v in pairs:
#     print("u = %s, v = %s" % (u,v))
#     print("length of u: %f, length of v: %f, dot product: %f"
#             % (length(u),length(v),dot(u,v)))

# #Exercise 3.16
# print(dot((3.61,0),(1.44,0)))


# #Exercise 3.17

# print(atan2(3,4)-atan2(4,3))
# print(dot((1,1,1),(-1,-1,1)))


# Exercise 3.21
# def cross_product(u,v):
#     ux,uy,uz = u
#     vx,vy,vz = v

#     return (uy*vz - uz*vy, uz*vx - ux*vz, ux*vy - uy*vx)




# print(cross_product((1,-2,1),(-6,12,-6)))

# draw3d (
#     Arrow3D((0,0,3), color=red),
#     Arrow3D((3,0,0), color=red),
#     Arrow3D((1,1,0),color=blue),
#     Arrow3D((-2,1,0), color=blue)
# )

# Exercise 3.24
# print(cross_product((1,0,1),(-1,0,0)))

# Exercise 3.25
# print(cross_product((0,0,1),(1,1,1)))
# print(cross_product((0,0,1),(-1,-1,-1)))
# print(cross_product((0,0,1),(1,0,1)))
# print(cross_product((0,0,1),(1,0,0)))

# Exercise 3.26
# print(dot(cross_product((1,1,0),(0,1,0)),(1,1,0)))
# print(dot(cross_product((1,1,0),(0,1,0)),(0,1,0)))

#Exercise 3.27
top = (0,0,1)
bottom = (0,0,-1)
xy_plane = [(1,0,0),(0,1,0),(-1,0,0),(0,-1,0)]
edges = [Segment3D(top,p) for p in xy_plane] +\
        [Segment3D(bottom, p) for p in xy_plane] +\
        [Segment3D(xy_plane[i], xy_plane[(i+1)%4]) for i in range(0,4)]
        

draw3d(*edges)


# def vertices(faces):
#     return list(set([vertex for face in faces for vertex in face]))


# print(vertices(8))





    