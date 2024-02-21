import matplotlib.pyplot as plt

# Define the data
squares = [1, 4, 9, 16, 25]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(squares, marker='o', color='b', linestyle='-', linewidth=2, markersize=8)

# Add labels and title
ax.set_xlabel('Index')
ax.set_ylabel('Square')
ax.set_title('Square Numbers')

# Add gridlines
ax.grid(True)

# Customize the x-axis and y-axis ticks
ax.set_xticks(range(len(squares)))
ax.set_xticklabels([str(i+1) for i in range(len(squares))])
ax.set_yticks([0, 5, 10, 15, 20, 25])
ax.set_yticklabels(['0', '5', '10', '15', '20', '25'])

# Show the plot
plt.show()
