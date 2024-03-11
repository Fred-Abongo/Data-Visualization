# ploting the start and end points

import matplotlib.pyplot as plt

while True:
    # Generate random walk data (rw.x_values, rw.y_values)
    # Assuming rw is the random walk object

    plt.scatter(rw.x_values, rw.y_values, c='blue', edgecolor='none', s=10)
    
    # Emphasize the first point (green, larger)
    plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolor='none', s=100)
    
    # Emphasize the last point (red, larger)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)
    
    plt.show()
