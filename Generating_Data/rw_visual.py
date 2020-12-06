import matplotlib.pyplot as plt
from random_walk import  RandomWalk

# Keeep making new walks as long as the program is active
while True:

    # Make a random walk

    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')

    fig,ax = plt.subplots(figsize=(15,9),dpi=128)
    point_number = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values,c=point_number,cmap=plt.cm.Blues,edgecolors='none',s=15)
    # Emphasize the first and last points
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=1)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.savefig('rv_visual.png',bbox_inches='tight')
    plt.show()

    keep_runnig  = input('Make another walk?(y/n): ')
    if keep_runnig == 'n':
        break