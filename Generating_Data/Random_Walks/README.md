Here, we use python to generate data for a path that has no clear direction but is determined by a series of random decision(random walk), each of wich is left entirely to chance.

This file 0-random_walk.py, defines a class RandomWalk that generates a random walk with a specified number of points. The __init__ method initializes the walk with (0,0) as starting point and a specified number of points. The fill_walk method calculates the random steps in x and y directions and adds them to the walk until the desired number of points is reached.After which, it creates an instance of RandomWalk, fills it with points, and plots the walk using matplotlib.

This file 1-random_walk.py, generates a random walk plot where the points are colored according to their order in the walk using a colormap and removes the black outline from each dot. The colormap gives a visual representation of the order of the points in the walk, with lighter colors indicating earlier points and darker colors indicating later points

This file 3-random_walk.py, generate and plot random walks, emphasizing the starting point in green and the ending point in red.
