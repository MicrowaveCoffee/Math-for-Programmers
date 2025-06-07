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

from math import sqrt, sin, cos, pi


#Utility Functions ------------------------------------
def add(*vectors):
    return tuple(map(sum,zip(*vectors)))


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

vector1 = (4,0,3)
vector2 = (-1,0,1)
# Exercise 3.26 ----------------
draw3d(
    Arrow3D(vector1, color = blue),
    Arrow3D(vector2, color= blue),
    Arrow3D(add(vector1,vector2), vector1),
    Arrow3D(add(vector1,vector2), vector2),
    # Arrow3D(vector2, vector1),
    Arrow3D(add(vector1,vector2), color=green)
)


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


vectors = []
for i in range(36):
    angle = pi * i/9
    radius = 0.5 + 0.3 * sin(pi* i/18)
    x = radius * cos(angle)
    y = radius * sin(angle)
    z = 0.1 * i
    vectors.append((x,y,z))

position = (0,0,0)
path_arrows = []
for v in vectors:
    new_position = add(position,v)
    path_arrows.append(Arrow3D(position, new_position))
    position = new_position  
draw3d(*path_arrows)