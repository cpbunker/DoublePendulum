import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# function that steps forward animation
def update_line(num, data, line):
    '''
    Function to pass to FuncAnimation
    
    Args:
    num:
    data:
    line: a Line2D object to modify be resetting data
    '''
    
    # reset the x-y points of the Line2D object
    # do this by passing 2D array of points to set_data method
    line.set_data(data[..., :num]);
    
    return line, # end update line
 
# create figure to plot on
fig1 = plt.figure()

# Fixing random state for reproducibility
np.random.seed(19680801)

# inputs for animation
n_points = 50; # how many xy points to include in all the data
data = np.random.rand(2, n_points); # 2D array with n_points x, y pairs
l, = plt.plot([], [], 'r-'); # init the Line2D object as red line, empty of points

# format the plot axes
plt.xlim(0, 1);
plt.ylim(0, 1);
plt.xlabel('x');
plt.title('test');

# run the line animation using FuncAnimation function
# syntax is:
# - figure
# - function that takes frame number and *fargs and returns line
# - int number of frames or iterable/generator to produce these numbers
# - fargs = tuple of args to pass to function
# - interval = delay between frames in microseconds
line_ani = animation.FuncAnimation(fig1, update_line, n_points, fargs=(data, l),
                                   interval=50, blit=True)
                                   
# show the plot
plt.show();

# To save the animation, use the command: line_ani.save('lines.mp4')

