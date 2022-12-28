import json

from flask import Flask, request, send_file
from plot_spider_graph import plot_spider_graph
import tempfile
import os

app = Flask(__name__)

@app.route('/spider_plot', methods=['POST'])
def spider_plot():

    # Generate a random file name in the temp directory
    file_name = next(tempfile._get_candidate_names())
    file_path = os.path.join(tempfile.gettempdir(), file_name + ".png")
    
    # Parse the JSON data from the request
    data = request.get_json()
    categories = data['categories']
    values = data['values']

    spiderfilename = file_path
    # Create the spider plot
    try:
        plot_spider_graph(categories, values, spiderfilename )
    except:
        spiderfilename= "bad_spider_plot.png"
    # Return the plot as a PNG file
    #return send_file('spider_plot.png',download_name='spider_plot.png')
    response = send_file(
        spiderfilename,
        mimetype='image/png',
        as_attachment=True,
        download_name='spider_plot.png'
    )

    return response
if __name__ == "__main__":
    app.run()
