from vector_drawing import *
from math import sqrt

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

def translate(translation, vectors):  # Fixed typo: was "tranlate"
    """Translate a list of vectors by a given translation vector."""
    return [add(translation, vector) for vector in vectors]  # Using add() function

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
    print("Testing translate function:")
    print(translate((11, 0), dino_vectors))
    
    # Draw single dino comparison
    draw_single_dino()
    
    # Draw 100 dinos
    hundred_dinos()