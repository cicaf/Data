#CLASS FOR THE RANDOM WALK.. CLASSS TO GENERATE RANDOM WALKS...
from random import choice
class RandomWalk:
    def __init__(self,num_points):
        self.num_points = num_points

        #ALL WALKS SHOULD START FROM (0,0)
#
#WE MAKE TWO LISTS TO HANDLE THE TWO SETS OF DATA...
        self.x_values = [0]
        self.y_values = [0]


#IMPLEMENT THE FILL_WALK METHOD TO FILL OUR WALKING LISTS...
    def fill_walk(self):
        """calculate all the points in the walk"""

        #KEEP TAKING STEPS TILL THE WALK REACHES OUR DESIRED VALUE
        
        while len(self.x_values) < self.num_points:
            #THE DIRECTION TOWARDS WHICH WE WILL WALK TOWARDS...
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            #FOR THE Y DIRECTION NOW...

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #REJECTING MOVES THAT WONT LEAD TO ANYWHERE...
            if x_step == 0 and y_step == 0:
                continue

            #NEW POSITION CALCULATION

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

##CHECK RW_VISUAL FOR VISUALS...
