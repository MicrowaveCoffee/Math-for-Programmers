from teapot import load_triangles
from draw_model import draw_model
from math import *
from vectors import *

def scale2(v):
    return scale(2.0,v)

def tranlate_left(v):
    return add((-1,0,0),v)

# compose with only two functions
# def compose(f1,f2):
#     def new_function(input):
#         return f1(f2(input))
#     return new_function

#Exercise 4.6 composes a lot of functions
def compose(*args):
    def new_function(input):
        state = input
        for f in reversed(args):
            state = f(state)
        return state
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

# def translate_by(vector):
#     def new_function(v):
#         return add(vector,v)
#     return new_function


def rotate2d(angle,vector):
    l,a = to_polar(vector)
    return to_cartesian((l,a+angle))

def rotate_z(angle,vector):
    x,y,z = vector
    new_x,new_y = rotate2d(angle,(x,y))
    return new_x,new_y,z


def rotate_z_by(angle):
    def new_function(v):
        return rotate_z(angle,v)
    return new_function


def rotate_y(angle,vector):
    x,y,z = vector
    new_x,new_z = rotate2d(angle,(x,z))
    return new_x,y,new_z

def rotate_y_by(angle):
    def new_function(v):
        return rotate_y(angle,v)
    return new_function


def rotate_x(angle,vector):
    x,y,z = vector
    new_y,new_z = rotate2d(angle,(y,z))
    return x,new_y,new_z


def rotate_x_by(angle):
    def new_function(v):
        return rotate_x(angle,v)
    return new_function


def stretch_x(vector):
    x,y,z = vector
    return (4.*x,y,z)

def stretch_y(vector):
    x,y,z = vector
    return(x,2.*y,z)

def stretch_z(vector):
    x,y,z = vector
    return(x,y,4.*z)

def cube_stretch_y(vector):
    x,y,z = vector
    return(x,y**3,z)

def cube_stretch_x(vector):
    x,y,z = vector
    return(x**3,y,z)

def cube_stretch_z(vector):
    x,y,z = vector
    return(x,y,z**3)


def slant_xy(vector):
    x,y,z = vector
    return(x+y,y,z)

def slant_xz(vector):
    x,y,z = vector
    return (x+z,y,z)

def slant_yz(vector):
    x,y,z = vector
    return (x,y+z,z)


#Exercise 4.1 
def translate_by_x(value):
    def new_function(vector):
        x,y,z = vector
        return (x+value,y,z)
    return new_function

#The Code the book Gave
def translate_by(translation):
    def new_function(v):
        return add(translation,v)
    return new_function

#my implementation is just for the x coord where the authors implementation is universal as you plug in the value that you want changed with a vector.



scale2_then_translate_left = compose(tranlate_left,scale2)

regular_triangles = load_triangles()
scaled_triangles = [
    [scale2_then_translate_left(vertex) for vertex in triangle]
    for triangle in regular_triangles
]



# draw_model(polygon_map(translate_by((1,0,0)), load_triangles()))
# draw_model(polygon_map(rotate_x_by(pi/2), load_triangles()))
# draw_model(polygon_map(translate_by((0,0,-10)),load_triangles()))

# Exercise 4.4
#This is an example of sequential composition (manual chaining)
triangles = load_triangles()
step1 = polygon_map(tranlate_left,triangles)
step2 = polygon_map(scale2,step1)

# draw_model(step2)

step3 = polygon_map(scale2,triangles)
step4 = polygon_map(tranlate_left,step3)
# draw_model(step4)

# This is the answer the author came up with 
# draw_model(polygon_map(compose(scale2,tranlate_left),load_triangles()))

#Exercise 4.5
draw_model(polygon_map(compose(scale_by(0.4),scale_by(1.5)),triangles))

