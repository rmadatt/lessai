import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Data for radar chart
categories = ['Art & Creativity', 'Outdoor Play', 'Friend Time', 'Nature Exploration']
n = len(categories)

# Check for empty categories to avoid division by zero
if n == 0:
    raise ValueError("No categories provided for the radar chart")

# Engagement scores (0-10)
current_scores = [3, 2, 4, 3]  # Current: AI-heavy, less outdoor fun
ideal_scores = [9, 8, 9, 10]   # Ideal: More grass, high engagement

# Close the circle
current_scores += current_scores[:1]
ideal_scores += ideal_scores[:1]

# Compute angles
angles = [i / float(n) * 2 * pi for i in range(n + 1)]  # +1 to close the loop

# Initialize radar chart
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

# Set up axes
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
plt.xticks(angles[:-1], categories, size=12)

# Set y-axis
ax.set_rlabel_position(0)
plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="black", size=10)
plt.ylim(0, 10)

# Plot data
ax.plot(angles, current_scores, linewidth=2, linestyle='solid', label='Current (AI-Heavy)', color='gray')
ax.fill(angles, current_scores, 'gray', alpha=0.3)
ax.plot(angles, ideal_scores, linewidth=2, linestyle='solid', label='Ideal (Grass-Focused)', color='#00FF00')
ax.fill(angles, ideal_scores, '#00FF00', alpha=0.3)

# Add title and legend
plt.title("John Ko’s Play Time: Less AI, More Grass", size=16, color='darkgreen', y=1.1)
ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), fontsize=10)

# Show plot
plt.tight_layout()
plt.show()
