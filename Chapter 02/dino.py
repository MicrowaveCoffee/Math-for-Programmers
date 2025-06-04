from vector_drawing import *
from math import sqrt, tan, pi, sin , cos, asin, acos, atan2
from random import uniform

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def length(v):
    """Calculate the length (magnitude) of a vector."""
    return sqrt(v[0]**2 + v[1]**2)

def add(*vectors):
    """Add multiple vectors together."""
    x_sum = sum(v[0] for v in vectors)
    y_sum = sum(v[1] for v in vectors)
    return (x_sum, y_sum)

def subtract(v1,v2):
    return (v1[0] - v2[0], v1[1] - v2[1])


def translate(translation, vectors):
    return [add(translation, v) for v in vectors]


def distance(v1,v2):
    return length(subtract(v1,v2))

def perimeter(vectors):
    distances = [distance(vectors[i], vectors[(i+1)%len(vectors)])
                 for i in range(0,len(vectors))]
    return sum(distances)

def scale(scalar,v):
    return (scalar * v[0],scalar * v[1])

def uni_scale(u,v):
    def r_scale():
        r = uniform(-3,3)
        return r
    def s_scale():
        s = uniform(-1,1)
        return s
    
    posibilities = [add(scale(r_scale(),u),scale(s_scale(),v))for i in range(0,500)]
    draw (
        Points(*posibilities)
    )

def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length*cos(angle), length*sin(angle))


def to_polar(vector):
    x , y = vector[0], vector[1]
    angle = atan2(y,x)
    return(length(vector),angle)

def rotate(angle, vectors):
    polars = [to polar(v) for v in vectors]
    return [to_cartesian((l, a+angle)) for l,a in polars]




# ============================================================================
# VECTOR DATA
# ============================================================================

dino_vectors = [
    (6,4), (3,1), (1,2), (-1,5), (-2,5), (-3,4), (-4,4),
    (-5,3), (-5,2), (-2,2), (-5,1), (-4,0), (-2,1), (-1,0), (0,-3),
    (-1,-4), (1,-4), (2,-3), (1,-2), (3,-1), (5,1)
]

smooth_heart_vectors = [
    (0, -20), (-4, -18), (-8, -15), (-12, -10), (-16, -5), (-19, 0),
    (-21, 5), (-22, 10), (-23, 15), (-23, 20), (-22, 24), (-20, 27),
    (-17, 29), (-14, 30), (-11, 30), (-8, 29), (-5, 27), (-2, 23),
    (0, 10), (2, 23), (5, 27), (8, 29), (11, 30), (14, 30),
    (17, 29), (20, 27), (22, 24), (23, 20), (23, 15), (22, 10),
    (21, 5), (19, 0), (16, -5), (12, -10), (8, -15), (4, -18), (0, -20)
]

# ============================================================================
# DRAWING FUNCTIONS
# ============================================================================

def draw_single_dino():
    """Draw original dino and translated version for comparison."""
    dino_vectors2 = translate((-1.5, -2.5), dino_vectors)
    
    draw(
        Points(*dino_vectors, color=blue),
        Polygon(*dino_vectors, color=blue),
        Points(*dino_vectors2, color=red),
        Polygon(*dino_vectors2, color=red)
    )

def draw_hearts():
    """Draw original heart and translated version for comparison."""
    translate_heart = translate((1, 2), smooth_heart_vectors)
    
    draw(
        Points(*smooth_heart_vectors, color=blue),
        Polygon(*smooth_heart_vectors, color=blue),
        Points(*translate_heart, color=red),
        Polygon(*translate_heart, color=red)
    )

def hundred_dinos():
    """Create and draw 100 dinos in a 10x10 grid."""
    # Generate translation vectors for a 10x10 grid
    translations = [(12*x, 10*y) for x in range(-5, 5) for y in range(-5, 5)]
    
    # Create dino polygons at each translation
    dinos = [Polygon(*translate(t, dino_vectors), color=blue) for t in translations]
    
    # Draw all dinos
    draw(*dinos, grid=None, axes=None, origin=None)

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    # Test the translate function
    # print("Testing translate function:")
    # print(translate((11, 0), dino_vectors))
    
    # Draw single dino comparison
    # draw_single_dino()
    
    # Draw 100 dinos
    # hundred_dinos()

    # uni_scale((-1,1),(1,1))

    # print(perimeter(dino_vectors))
    # print(length((-1.34,2.68)))

    # angle = 37*pi/180
    # print(to_cartesian((5,angle)))

    # print(tan(pi/4))
    # print(to_cartesian((15,37)))

    # print(length((-1/2,sqrt(3)/2)))

    # print(length((sin(50*pi/180), cos(50*pi/180))), tan(50*pi/180))

    # print(tan(2.035))

    # print(cos(10*pi/6 * pi/180))
    # print(cos(10*pi/6))

    # print(sin(10*pi/6 * pi/180))
    # print(sin(10*pi/6))

    # polar_vectors = [(cos(5*x*pi/500.0), 2*pi*x/1000.0) for x in range(0,1000)]
    # coords = [to_cartesian(p) for p in polar_vectors]
    # draw(
    #     Polygon(*coords,color=green)
    # )

    # polar_coords = [(cos(x*pi/100.0), 2*pi*x/1000.0) for x in range(0,1000)]
    # vectors = [to_cartesian(p) for p in polar_coords]
    # draw(Polygon(*vectors, color=green))

    # print(sin(1))


    # print(asin(3/sqrt(13)))
    # print(atan2(3,-2)* 57.29)

    # print(to_polar((1,1)))
    # print(116.57/57.29)

    # rotation_angle = pi/4
    # dino_to_polar = [to_polar(p) for p in dino_vectors]
    # dino_polar_rotation = [(l,angle + rotation_angle) for l,angle in dino_to_polar]
    # back_to_cartesian = [to_cartesian(p) for p in dino_polar_rotation]
    # draw(
    #     Polygon(*dino_vectors, color = red),
    #     Polygon(*back_to_cartesian, color = blue)
    # )

    rotation_angle = pi/4
    dino_polar = [to_polar(v) for v in dino_vectors]
    dino_rotated_polar = [(l,angle + rotation_angle) for l,angle in dino_polar]
    dino_rotated = [to_cartesian(p) for p in dino_rotated_polar]
    draw(
        Polygon(*dino_vectors, color=gray),
        Polygon(*dino_rotated, color=red)
    )