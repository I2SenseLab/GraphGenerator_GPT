import matplotlib.pyplot as plt
from math import pi

def plot_spider_graph(categories, values, filename):
    # Number of variables
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    values = values + values[:1]
    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='black', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=7)
    plt.ylim(0, 100)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    # Save the figure as a PNG file
    plt.savefig(filename, dpi=300)

if __name__ == "__main__":
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
    values = [50, 60, 70, 80, 90]
    filename = "spider_plot.png"

    plot_spider_graph(categories, values, filename)
