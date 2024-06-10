import matplotlib.pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path
import numpy as np
import matplotlib.transforms as transforms

class HatchStyle:
    def __init__(self, xy, width, height, symbol='y', spacing=2.0, random_placement=False, random_rotation=False, gradient=False, **kwargs):
        self.xy = xy
        self.width = width
        self.height = height
        self.symbol = symbol
        self.spacing = spacing
        self.random_placement = random_placement
        self.random_rotation = random_rotation
        self.gradient = gradient
        self.kwargs = kwargs
    
    def create_custom_hatch_pattern(self):
        symbol = self.symbol
        spacing = self.spacing
        
        if symbol == "^":
            # caret
            vertices = np.array([[0.0, 0.0], [0.5, 1.0], [1.0, 0.0], [0.0, 0.0]])
        elif symbol == "_":
            # underscore
            vertices = np.array([[0.0, 0.0], [1.0, 0.0]])
        elif symbol == "=":
            # equals
            vertices = np.array([[0.0, 0.2], [1.0, 0.2], [0.0, 0.8], [1.0, 0.8]])
        elif symbol == "x":
            # x
            vertices = np.array([[0.0, 0.0], [1.0, 1.0], [0.5, 0.5], [1.0, 0.0], [0.0, 1.0]])
        elif symbol == "|":
            # vertical bar
            vertices = np.array([[0.5, 0.0], [0.5, 1.0]])
        elif symbol == ".":
            # dot
            vertices = np.array([[0.5, 0.5]])
        elif symbol == "o":
            # circle
            t = np.linspace(0, 2 * np.pi, 100)
            vertices = np.vstack([np.cos(t) * 0.5 + 0.5, np.sin(t) * 0.5 + 0.5]).T
        elif symbol == "*":
            # star
            vertices = np.array([[0.5, 1.0], [0.6, 0.6], [1.0, 0.5], [0.6, 0.4], [0.5, 0.0], [0.4, 0.4], [0.0, 0.5], [0.4, 0.6], [0.5, 1.0]])
        elif symbol == "t":
            # triangle
            vertices = np.array([[0.0, 0.0], [0.5, 1.0], [1.0, 0.0], [0.0, 0.0]])
        elif symbol == "y":
            # 1
            vertices = np.array([[0.5, 0.0], [0.5, 1.0], [0.3, 0.8], [0.5, 1.0], [0.7, 0.8]])
        elif symbol == "s":
            # square
            vertices = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0], [0.0, 0.0]])
        elif symbol == "5":
            # pentagon
            t = np.linspace(0, 2 * np.pi, 5, endpoint=False)
            vertices = np.vstack([np.cos(t) * 0.5 + 0.5, np.sin(t) * 0.5 + 0.5]).T
            vertices = np.concatenate([vertices, [vertices[0]]])
        elif symbol == "6":
            # hexagon
            t = np.linspace(0, 2 * np.pi, 6, endpoint=False)
            vertices = np.vstack([np.cos(t) * 0.5 + 0.5, np.sin(t) * 0.5 + 0.5]).T
            vertices = np.concatenate([vertices, [vertices[0]]])
        elif symbol == "8":
            # octagon
            t = np.linspace(0, 2 * np.pi, 8, endpoint=False)
            vertices = np.vstack([np.cos(t) * 0.5 + 0.5, np.sin(t) * 0.5 + 0.5]).T
            vertices = np.concatenate([vertices, [vertices[0]]])
        elif symbol == "+":
            # plus
            vertices = np.array([[0.5, 0.0], [0.5, 1.0], [0.0, 0.5], [1.0, 0.5]])
        elif symbol == "P":
            # P
            vertices = np.array([[0.0, 0.0], [0.0, 1.0], [0.5, 1.0], [0.5, 0.5], [0.0, 0.5]])
        else:
            raise ValueError(f"Unsupported symbol: {symbol}")

        codes = [Path.MOVETO] + [Path.LINETO] * (len(vertices) - 1)
        
        hatch_pattern_vertices = []
        hatch_pattern_codes = []
        
        for x in range(10):
            for y in range(10):
                offset = np.array([x * spacing, y * spacing])
                if self.random_placement:
                    offset += np.random.uniform(-0.5, 0.5, 2) * spacing
                hatch_pattern_vertices.extend(vertices + offset)
                hatch_pattern_codes.extend(codes)
        
        return Path(hatch_pattern_vertices, hatch_pattern_codes)



    def plot_hatch(self, ax):
        custom_hatch = self.create_custom_hatch_pattern()
        kwargs = self.kwargs.copy()
        kwargs.pop('edgecolor', None)
        patch = PathPatch(custom_hatch, fill=False, edgecolor='red', linewidth=1.5, **kwargs)
    
        if self.random_rotation:
            rotation_angle = np.random.uniform(0, 10)
            rotation_transform = transforms.Affine2D().rotate_deg(rotation_angle)
            patch.set_transform(ax.transData + rotation_transform)
    
        ax.add_patch(patch)
    
fig, axs = plt.subplots(4, 4, figsize=(10, 10))

symbols = ['^', '_', '=', 'x', '|', '.', 'o', '*', 't', 'y', 's', '5', '6', '8', '+', 'P']

for i in range(4):
    for j in range(4):
        symbol_index = i * 4 + j
        hatch_style = HatchStyle((0, 0), 10, 10, symbol=symbols[symbol_index], spacing=2.0,
                                 edgecolor='red', facecolor='white', random_placement=False, random_rotation=True)
        hatch_style.plot_hatch(axs[i, j])
        
        axs[i, j].set_xlim(-1, 11)
        axs[i, j].set_ylim(-1, 11)
        axs[i, j].set_aspect('equal', adjustable='box')
        axs[i, j].set_title(f"Symbol: {symbols[symbol_index]}")

plt.tight_layout()
plt.show()
