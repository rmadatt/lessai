import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
labels = ['Daily (20 min)', 'Twice Weekly (180 min)']
ai_usage = [36, 36]  # Assuming 20% of 3-hour (180 min) daily study time = 36 min
puzzle_time = [20, 180]  # Puzzle time: 20 min daily or 180 min twice weekly

# Set up the bar chart
x = np.arange(len(labels))  # Label locations
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
bars1 = ax.bar(x - width/2, ai_usage, width, label='AI Usage', color='red')
bars2 = ax.bar(x + width/2, puzzle_time, width, label='Challenging Puzzles', color='yellow')

# Customize the chart
ax.set_ylabel('Time (Minutes)')
ax.set_title('John Ko\'s Study Time: AI Usage vs Challenging Brain Puzzles')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Add time labels on top of bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)} min', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()
