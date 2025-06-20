from teapot import load_triangles
from draw_model import draw_model

from vectors import *

def scale2(v):
    return scale(2.0,v)

def tranlate_left(v):
    return add((-1,0,0),v)

#Composite function
def scale_to_translate(v):
    return tranlate_left(scale2(v))

regular_triangles = load_triangles()
scaled_triangles = [
    [scale_to_translate(vertex) for vertex in triangle]
    for triangle in regular_triangles
]



draw_model(scaled_triangles)