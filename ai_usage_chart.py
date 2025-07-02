import matplotlib.pyplot as plt
import numpy as np

# Data for the bar chart
labels = ['Ideal (Pareto)', 'John Ko\'s Study (Low AI)', 'John Ko\'s Study (High AI)']
ai_usage = [20, 20, 40]  # AI usage percentages
independent_thinking = [80, 80, 60]  # Independent thinking percentages

# Set up the bar chart
x = np.arange(len(labels))  # Label locations
width = 0.35  # Width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars
bars1 = ax.bar(x - width/2, ai_usage, width, label='AI Usage', color='red')
bars2 = ax.bar(x + width/2, independent_thinking, width, label='Independent Thinking', color='blue')

# Customize the chart
ax.set_ylabel('Percentage (%)')
ax.set_title('John Ko\'s Study Time: AI Usage vs Independent Thinking')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# Add percentage labels on top of bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}%', 
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
