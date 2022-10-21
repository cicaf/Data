"""
LETS PLOT A SIMPLE LINE GRAPH USING MATPLOTLIB, AND THEN CUSTOMIZE IT TO
CREATE A MORE INFORMATIVE DATA VISUALIZATION. WELL USE THE SQUARE NUMBER
SEQUENCE 1, 4, 9, 16, 25 AS THE DATA FOR THE GRAPH.

"""

import matplotlib.pyplot as plt

squares = [1,4,9,16,25,36,49,64,81,100,121,144.169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961]

fig, ax = plt.subplots()

ax.plot(squares,linewidth=3)
ax.set_title("SQUARE OF VALUE",fontsize=15)
ax.set_xlabel("VALUE",fontsize=15)
ax.set_ylabel("SQUARE OF VALUE",fontsize=14)

plt.show()