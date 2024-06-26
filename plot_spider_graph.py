import matplotlib.pyplot as plt
from math import pi
import colorsys

def color_from_number(max_num, current_num):
    # Normalize the current number to a value between 0 and 1
    norm_num = current_num / max_num

    # Convert the normalized number to HSL color space
    h, s, l = colorsys.hls_to_rgb(norm_num, 0.5, 0.5)

    # Convert the HSL color to RGB and format it as a hex string
    r, g, b = [x for x in (h, s, l)]
    return (r,g,b)

def plot_spider_graph(categories, values, filename, legend = None, max_value = None, tick_spacing = None):
    # Number of variables
    N = len(categories)
    C = len(values)

    print("Graphing {} categories, and {} values".format(N,C))
    print("Categories: {} , Values: {}".format(categories, values))
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    plt.clf()
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='black', size=8)

    # Calculate the max value for y-axis if not provided
    if max_value is None:
        max_value = max(max(values), 5)

    if tick_spacing is None:
        # Determine tick spacing
        tick_spacing = determineTickSpacing(max_value)

    # Draw ylabels
    ax.set_rlabel_position(0)
    y_ticks = [i for i in range(1,int(max_value)+1,tick_spacing)]
    plt.yticks(y_ticks, map(str,y_ticks), color="grey", size=7)
    plt.ylim(0, max_value)

    # Plot data
    for i in range(C//N):
        print("Graphing Loop: ",i)
        #For loop 0 goes from 0 -> N-1
        #For loop 1 goes from N -> 2N-1
        #etc
        #    values = values + values[:1] (Need to repeat the first value in the loop)

        label = None
        if legend is not None:
            len_leg = len(legend)
            print("Labeling Line", i)
            if len_leg >= (C//N):
                label = legend[i]
                
            else:
                print("Incomplete Legend Provided")
        loop_values = values[(i*N):(N*(i+1))] + values[(i*N):(i*N)+1]
        ax.plot(angles,  loop_values, linewidth=1, linestyle='solid',label = label)

        colour = color_from_number((C//N - 1),i)
        # Fill area
        ax.fill(angles, loop_values, colour, alpha=0.3)
    
    if legend is not None: #Enable the legend on the graph
        ax.legend(loc = 'center')

    print("Figure Generated")
    # Save the figure as a PNG file
    plt.savefig(filename, dpi=300)
    plt.close('all')

def determineTickSpacing(max_value):
    if max_value <= 10:
        tick_spacing = 1
    elif max_value <= 50:
        tick_spacing = 5
    elif max_value <= 100:
        tick_spacing = 10
    else:
        tick_spacing = max_value // 10
    return tick_spacing

if __name__ == "__main__":
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
    legend = ['Cat', 'Cat2']
    values = [0,0,2, 3, 4, 5, 5,4,3,1]
    filename = "spider_plot.png"

    plot_spider_graph(categories, values, filename,legend)
