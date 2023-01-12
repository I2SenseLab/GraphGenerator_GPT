import matplotlib.pyplot as plt
from datetime import datetime
import tempfile
import os 
def generate_bar_graph(categories,data,title = "Statistics Bar Graph",xlabel = "Categories",ylabel = "Values", filename = "Bar_Graph.png"):
    plt.bar(categories, data)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.savefig(filename,dpi=300)
    plt.close('all')


if __name__ == "__main__":
    categories = ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5']
    values = [50, 60, 70, 80, 90]
    filename = "bar_plot.png"
    title = "THE TITLE"
    xlabel = "XCATS"
    ylabel = "YVALS"
    generate_bar_graph(categories, values, title,xlabel,ylabel,filename)