from flask import Flask
from flask import send_from_directory
from flask import render_template

from hardware_interfaces.camera import find_path_of_most_recent_image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        photo_uri=find_path_of_most_recent_image(),
    )

# Static files
@app.route('/js/index.js')
def serve_js():
    return send_from_directory('frontend/js/', 'index.js')
@app.route('/css/stylesheet.css')
def serve_css():
    return send_from_directory('frontend/css/', 'stylesheet.css')
@app.route('/images/<image_filename>')
def serve_images(image_filename):
    return send_from_directory('data/images', image_filename)

app.run(host='0.0.0.0', )
