import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

def generate_bar_graph(categories, data, title="Statistics Bar Graph",
                       xlabel="Categories", ylabel="Values",
                       filename="Bar_Graph.png"):
    
    print(f"Generating Bar Graph with {len(categories)} categories and {len(data)} values")
    print(f"Categories: {categories} , Values: {data}")

    fig, ax = plt.subplots()  # Create a figure and a set of subplots
    bars = ax.bar(categories, data)

    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    fig.canvas.draw()  # Draw the figure so we can get info about the objects

    # Get the width of the axes in inches
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    axes_width_inches, axes_height_inches = bbox.width, bbox.height

    # Compute the number of inches available for each category
    inches_per_category = axes_width_inches / len(categories)

    # Compute the width and height required for the longest label
    max_label_width_inches = 0
    max_label_height_inches = 0
    for label in ax.get_xticklabels():
        bbox = label.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        max_label_width_inches = max(max_label_width_inches, bbox.width)
        max_label_height_inches = max(max_label_height_inches, bbox.height)

    # If the max width of the labels is greater than the space available for each category,
    # or the height of the labels when rotated is greater than the height of the axes,
    # rotate the labels
    if max_label_width_inches > inches_per_category or max_label_height_inches > axes_height_inches:
        plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

    plt.tight_layout()  # Adjust the layout to prevent cutting off labels

    fig.savefig(filename, dpi=300)
    plt.close('all')



if __name__ == "__main__":
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
    values = [50, 60, 70, 80, 90]
    filename = "bar_plot.png"
    title = "THE TITLE"
    xlabel = "XCATS"
    ylabel = "YVALS"
    generate_bar_graph(categories, values, title,xlabel,ylabel,filename)