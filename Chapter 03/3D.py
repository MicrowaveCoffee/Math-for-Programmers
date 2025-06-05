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

vector = (-1,-2,2)

draw3d(
    Arrow3D(vector),
    Points3D(vector)
)