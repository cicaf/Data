#RANDOM WALK VISUAL FROM random_walk.py

import matplotlib.pyplot as plt

from random_walk import RandomWalk
rw = RandomWalk(3000)
rw.fill_walk()

#PLOTTING THE WALK POINTS...
plt.style.use('classic')

fig, ax = plt.subplots()

ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()