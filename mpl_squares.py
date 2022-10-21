"""
LETS PLOT A SIMPLE LINE GRAPH USING MATPLOTLIB, AND THEN CUSTOMIZE IT TO
CREATE A MORE INFORMATIVE DATA VISUALIZATION. WELL USE THE SQUARE NUMBER
SEQUENCE 1, 4, 9, 16, 25 AS THE DATA FOR THE GRAPH.

"""

import matplotlib.pyplot as plt

input_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

squares = [1,4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400,441,484,529,576,625,676,729,784,841,900,961]
plt.style.use('seaborn')

fig, ax = plt.subplots()

ax.plot(input_values,squares,linewidth=3)
ax.set_title("SQUARE OF VALUE",fontsize=15)
ax.set_xlabel("VALUE",fontsize=15)
ax.set_ylabel("SQUARE OF VALUE",fontsize=14)

plt.show()