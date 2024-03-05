Data-Visualization

This Project is an introduction to data visualization through a variety of visualization techniques. The data sets are generate through code, downloaded from online sources, and some data sets the programs download automatically.This project is a replica of programs that sift through large data sets and make visual representations of that stored information.


The file mpl_squares.py uses matplotlib to create a plot of the squares of numbers. It difines the data (squares),creates a figure and axis, plots the data with markers, colors, and line styles, adds labels and a title, adds gridlines, and customizes the x-axis and y-axis ticks

The file scatter_squares.py, uses matplotlib to create a scatter plot with a single pointat coordinates (2, 4) and a point size of 200. The plot is then customized with a title, axis labels, and tick label sizes before being displayed.

The file 0-scatter_squares.py, the x_values list contains the numbers to be squared, and y_values contains the square of each number. When these lists are passed to scatter(),
matplotlib reads one value from each list as it plots each point. The points
to be plotted are (1, 1), (2, 4), (3, 9), (4, 16), and (5, 25);

This file 1-scatter_squares.py, generates a scatter plot of the squares of numbers from 1 to 1000. It starts by creating a list of x-values from 1 to 1000. Then a list comprehension is used to calculate the y-values, which are the squares of the x-values. The plt.scatter function is used to create the scatter plot, and the plt.axis function is used to suet the range for each axis. Finally, the plot is displayed with a title and labeled axes.

matplotlib can color points individually in a scatter plot, this file , 2-scatter_squares.py will create a scatter plot with markers that have no outlines. Thiscan be useful for creating a cleaner, more minimalist look in the plots

This file 3-scatter_squares.py, colormap are used to represent the y_values as colors, providing a visual representation of the data. The points with lower y-values are coloured light blue while the points with larger y-values dark blue.
