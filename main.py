from flask import Flask, request, render_template, send_from_directory, jsonify
from flask_cors import CORS
from plot_spider_graph import plot_spider_graph
from plot_bar_graph import generate_bar_graph
from bucket_operations import upload_to_bucket
import tempfile
import os
import yaml
import base64

app = Flask(__name__)
PORT = os.environ.get("PORT", 8080)
CORS(app, origins=[f"https://graph-gpt.fl2f.ca/", "http://localhost:{PORT}", "https://chat.openai.com"])

@app.route('/spider_plot', methods=['POST'])
def spider_plot():
    """
    Generate a spider plot graph based on the provided data.

    This function takes in a JSON request containing categories, data sets, and optional parameters,
    and generates a spider plot graph based on the provided data. The graph is saved as a PNG file
    and the response data includes the URL or base64-encoded image data of the generated graph.

    Returns:
        dict: A dictionary containing the response data, including the URL or base64-encoded image data
              of the generated graph.

    Raises:
        Exception: If an error occurs during the generation of the spider plot graph.

    """
    # Generate a random file name in the temp directory
    file_name = next(tempfile._get_candidate_names())
    file_path = os.path.join(tempfile.gettempdir(), file_name + ".png")

    # Parse the JSON data from the request
    data = request.get_json()
    categories = data['categories']
    data_sets = data['data_sets'] # Replace 'values' with 'data_sets', which is an array of dicts
    max_value = data.get('max_value', None)
    response_type = data.get('response_type', 'bucketurl') # New optional parameter 'response_type'

    # Assemble values and legend into separate lists
    values = []
    legend = []
    for data_set in data_sets:
        values.append(data_set['values'])
        legend.append(data_set['legend'])

    spiderfilename = file_path
    values = [element for sublist in values for element in sublist] # Flatten the list of lists
    try:
        plot_spider_graph(categories, values, spiderfilename, legend, max_value)
    except:
        return "bad spider plot", 400

    if response_type == 'bucketurl':
        # Here you would upload the file to a storage bucket and get its URL.
        # Assuming upload_to_bucket() is a function that handles uploading the image to your storage bucket
        # and returns the URL of the uploaded image.
        # Combining the variables into a dictionary
        metadata = {
            "categories": categories,
            "values": values,
            "legend": legend,
            "max_value": max_value
        }
        bucket_url = upload_to_bucket(spiderfilename,spiderfilename, metadata=metadata)
        response_data = {
            'image': bucket_url
        }
    else:
        with open(spiderfilename, 'rb') as image_file:
            image_data = image_file.read()
            base64_image = base64.b64encode(image_data).decode('utf-8')
            response_data = {
                'image': base64_image
            }
    
    return response_data

@app.route('/bar_graph', methods=['POST'])
def bar_graph():
    """
    Generate a bar graph based on the provided data and return the graph as a response.

    Parameters:
    None

    Returns:
    response_data (dict): A dictionary containing the image data of the generated bar graph or the URL of the graph.

    Raises:
    None
    """
    # Generate a random file name in the temp directory
    file_name = next(tempfile._get_candidate_names())
    file_path = os.path.join(tempfile.gettempdir(), file_name + ".png")

    # Parse the JSON data from the request
    data = request.get_json()
    categories = data['categories']
    values = data['values']
    title = data['title']
    xlabel = data['xlabel']
    ylabel = data['ylabel']
    response_type = data.get('response_type', 'bucketurl')  # New optional parameter 'response_type'

    try:
        generate_bar_graph(categories, values, title, xlabel, ylabel, file_path)
    except:
        return "bad bar graph", 400

    if response_type == 'bucketurl':
        # Here you would upload the file to a storage bucket and get its URL.
        # Assuming upload_to_bucket() is a function that handles uploading the image to your storage bucket
        # and returns the URL of the uploaded image.
        # Combining the variables into a dictionary
        metadata = {
            "categories": categories,
            "values": values,
            "title": title,
            "xlabel": xlabel,
            "ylabel": ylabel
        }
        bucket_url = upload_to_bucket(file_path,file_path, metadata=metadata)
        response_data = {
            'image': bucket_url
        }
    else:
        with open(file_path, 'rb') as image_file:
            image_data = image_file.read()
            base64_image = base64.b64encode(image_data).decode('utf-8')
            response_data = {
                'image': base64_image
            }

    return response_data


@app.route('/ads.txt')
def serve_ads_txt():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ads.txt')

@app.route("/")
def main_page():
    return render_template("home.html")

@app.route('/.well-known/ai-plugin.json')
def serve_manifest():
    return send_from_directory(os.path.join(app.root_path, 'static', '.well-known'), 'ai-plugin.json')

@app.route('/logo.png')
def serve_logo():
    return send_from_directory(os.path.join(app.root_path, 'static'),'logo.png')

@app.route("/legal")
def legal():
    return render_template('legal.html')

@app.route("/termsofservice")
def termsofservice():
    return render_template('terms.html')

@app.route('/openapi.yaml')
def serve_openapi_yaml():
    with open(os.path.join(app.root_path,'static', 'openapi.yaml'), 'r') as f:
        yaml_data = f.read()
    yaml_data = yaml.load(yaml_data, Loader=yaml.FullLoader)
    return jsonify(yaml_data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

#  Windows Powershell Command to test this by creating a basic spider graph
#  Invoke-WebRequest -Method POST -Uri http://localhost:5000/spider_plot -ContentType 'application/json' -Body '{"categories": ["Category 1", "Category 2", "Category 3"], "values": [50, 60, 70]}' -OutFile spider_fffplot.png
# 