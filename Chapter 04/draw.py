from teapot import load_triangles
from draw_model import draw_model

from vectors import *

def scale2(v):
    return scale(2.0,v)

def tranlate_left(v):
    return add((-1,0,0),v)

#Composite function
# def scale_to_translate(v):
#     return tranlate_left(scale2(v))

def compose(f1,f2):
    def new_function(input):
        return f1(f2(input))
    return new_function

scale2_then_translate_left = compose(tranlate_left,scale2)

regular_triangles = load_triangles()
scaled_triangles = [
    [scale2_then_translate_left(vertex) for vertex in triangle]
    for triangle in regular_triangles
]



draw_model(scaled_triangles)