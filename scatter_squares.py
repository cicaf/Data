import matplotlib.pyplot as plt
from pexpect import which

plt.style.use('seaborn')

fig, ax = plt.subplots()
#WE CAN DECLARER THE VALUES FOR SCATTER...
"""
x_values = [1,2,3,4,5,6,7,8,9,10]
y_values = [1,4,9,16,25,36,49,64,81,100]
"""
#WE CAN AUTOMATE THE GENERATION OF X AND Y,USING A LOOP
x_values = range(1,1001)
y_values = [x**2 for x in x_values]

#ax.scatter(2, 4)
#plt.show()
#ADD SYTLING
#THE S = 200 ARGUEMENT IS FOR STATING THE SIZE OF THE DOTS.
#ax.scatter(2, 4, s=200)

#ax.scatter(x_values,y_values,c=(0.2,0.3,0.4), s = 10)

#WE USE SCATTER TO MAKE THE LINE FADE LIKE...HEHE FADE AWAY JUMPSHOT...
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Greens,s=10)
#SET THE RANGE FOR EACH AXIS
ax.axis([0,1001, 0,1100000])

#SET CHAT LABEL AND STYLING
ax.set_ylabel('Square of Value' ,fontsize = 14)
ax.set_xlabel('Value', fontsize = 14)
ax.set_title('Square Number',fontsize = 24)

#SET SIZE OF TICK LABELS

ax.tick_params(axis='both',which='major',labelsize=14)

plt.show()