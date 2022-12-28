import json

from flask import Flask, request, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from plot_spider_graph import plot_spider_graph

app = Flask(__name__)

@app.route('/spider_plot', methods=['POST'])
def spider_plot():
    # Parse the JSON data from the request
    data = request.get_json()
    categories = data['categories']
    values = data['values']

    # Create the spider plot
    plot_spider_graph(categories, values, 'spider_plot.png')

    # Return the plot as a PNG file
    return send_file(
        'spider_plot.png',
        mimetype='image/png',
        as_attachment=True,
        attachment_filename='spider_plot.png'
    )

if __name__ == "__main__":
    app.run()
