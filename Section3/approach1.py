import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

class HatchStyle:
    def __init__(self, symbol='x', density=5, markerfacecolor='black', markeredgecolor='red', 
                 random_rotation=False, staggered=False, random_placement=False, gradient=False):
        self.symbol = symbol
        self.density = density
        self.markerfacecolor = markerfacecolor
        self.markeredgecolor = markeredgecolor
        self.random_rotation = random_rotation
        self.staggered = staggered
        self.random_placement = random_placement
        self.gradient = gradient

    def generate_pattern(self):
        if self.symbol == 'x':
            return self.generate_cross_hatch()
        elif self.symbol == '.':
            return self.generate_dot_hatch()
        elif self.symbol == 'o':
            return self.generate_circle_hatch()
        # Add more symbols as needed
        return []

    def generate_dot_hatch(self):
        dots = []
        for i in range(self.density):
            for j in range(self.density):
                if self.random_placement:
                    x = random.uniform(0, 1)
                    y = random.uniform(0, 1)
                else:
                    x = (i + 0.5) / self.density
                    y = (j + 0.5) / self.density
                if self.staggered and i % 2 == 1:
                    y += 0.5 / self.density
                if self.random_rotation:
                    rotation = random.uniform(0, 360)
                else:
                    rotation = 0
                dots.append((x, y, rotation))
        return dots

    def generate_cross_hatch(self):
        lines = []
        for i in range(self.density):
            offset = i / self.density
            lines.append([(0, offset), (1, offset)])
            lines.append([(offset, 0), (offset, 1)])
        return lines

    def generate_circle_hatch(self):
        circles = []
        for i in range(self.density):
            for j in range(self.density):
                x = (i + 0.5) / self.density
                y = (j + 0.5) / self.density
                r = 0.5 / self.density
                if self.random_rotation:
                    rotation = random.uniform(0, 360)
                else:
                    rotation = 0
                circles.append((x, y, r, rotation))
        return circles

    def apply_hatch(self, ax, rect):
        hatch_pattern = self.generate_pattern()
        for pattern in hatch_pattern:
            if self.symbol == '.':  # Dot 
                x, y, rotation = zip(*hatch_pattern)
                ax.scatter(x, y, color=self.markerfacecolor, edgecolor=self.markeredgecolor, s=10)
            elif self.symbol == 'o':  # Circle 
                for (cx, cy, r, rotation) in hatch_pattern:
                    circle = patches.Circle((cx, cy), r, edgecolor=self.markeredgecolor, facecolor=self.markerfacecolor, fill=True)
                    ax.add_patch(circle)
            elif self.symbol == 'x':  # Line 
                for line in hatch_pattern:
                    x, y = zip(*line)
                    ax.plot(x, y, color=self.markeredgecolor)

        # Apply the rectangle as a base
        ax.add_patch(rect)

fig, ax = plt.subplots()
rect = patches.Rectangle((0, 0), 1, 1, alpha=0.5, facecolor='none')
hatch_style = HatchStyle(symbol='x', density=10, markerfacecolor='black', markeredgecolor='red', 
                         random_rotation=True, staggered=True, random_placement=True, gradient=True)
hatch_style.apply_hatch(ax, rect)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

plt.show()
