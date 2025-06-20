from teapot import load_triangles
from draw_model import draw_model

from vectors import *

def scale2(v):
    return scale(2.0,v)

def tranlate_left(v):
    return add((-1,0,0),v)



def compose(f1,f2):
    def new_function(input):
        return f1(f2(input))
    return new_function

def polygon_map(transformation,polygons):
    return [
        [transformation(vertex) for vertex in triangle]
        for triangle in polygons
    ]



def scale_by(scalar):
    def new_function(v):
        return scale(scalar,v)
    return new_function

def translate_by(vector):
    def new_function(v):
        return add(vector,v)
    return new_function


def rotate2d(angle,vector):
    l,a = to_polar(vector)
    return to_cartesian((l,a+angle))

def rotate_z(angle,vector):
    x,y,z = vector
    new_x,new_y = rotate2d(angle,(x,y))
    return new_x,new_y,z

scale2_then_translate_left = compose(tranlate_left,scale2)

regular_triangles = load_triangles()
scaled_triangles = [
    [scale2_then_translate_left(vertex) for vertex in triangle]
    for triangle in regular_triangles
]



draw_model(polygon_map(translate_by((1,0,0)), load_triangles()))