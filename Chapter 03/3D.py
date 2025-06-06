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

from math import sqrt


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

vectors = ((4,0,3),(-1,0,1))
# Exercise 3.26 ----------------
draw3d(
    Points3D(*vectors),
    Points3D(add(*vectors)),
    Arrow3D(*vectors)
)


    