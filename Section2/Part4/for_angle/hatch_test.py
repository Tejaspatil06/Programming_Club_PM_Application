import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from hatch import VerticalHatch,get_path
from matplotlib.path import Path


# Function to plot hatch patterns
def plot_hatch_patterns(hatchpattern, density, thickness, angle):
    fig, ax = plt.subplots()
    path = get_path(hatchpattern, density, thickness, angle)
    patch = PathPatch(path, facecolor='none', edgecolor='black')

    ax.add_patch(patch)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', adjustable='box')
    plt.title(f'Hatch: "{hatchpattern}", Density: {density}, Thickness: {thickness}, Angle: {angle}')
    plt.show()

# Test different angles
angles = [0, 30, 45, 60, 90]
for angle in angles:
    plot_hatch_patterns('|', density=5, thickness=0.02, angle=angle)
