# defining custom colors

import matplotlib.pyplot as plt

x_values = list(range(0, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='red', edgecolor='none', s=40)
plt.show()
