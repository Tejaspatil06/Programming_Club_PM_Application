import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from hatch import get_path

def plot_hatch_patterns(hatchpattern, density, thickness):
    fig, ax = plt.subplots()
    path = get_path(hatchpattern, density, thickness)
    patch = PathPatch(path, facecolor='none', edgecolor='blue')

    ax.add_patch(patch)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal', adjustable='box')
    plt.title(f'Hatch: "{hatchpattern}", Density: {density}, Thickness: {thickness}')
    plt.show()

# Test different thicknesses
plot_hatch_patterns('|', density=5, thickness=0.2)
plot_hatch_patterns('|', density=10, thickness=0.1)
plot_hatch_patterns('|', density=100, thickness=0.01)
