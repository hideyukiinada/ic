"""
An image classification web app.

__author__ = "Hide Inada"
__copyright__ = "Copyright 2019, Hide Inada"
__license__ = "The MIT License"
__email__ = "hideyuki@gmail.com"
"""

import os
import logging
from pathlib import Path
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import numpy as np
import tensorflow
import tensorflow.keras.applications.resnet50
import tensorflow.keras.preprocessing
from PIL import Image

IMAGE_HEIGHT = 224
IMAGE_WIDTH = 224
IMAGE_CHANNELS = 3
SAVE_DIR = '/tmp/ic'

log = logging.getLogger(__name__)
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))  # Change the 2nd arg to INFO to suppress debug logging

app = Flask(__name__)
model = tensorflow.keras.applications.resnet50.ResNet50(weights='imagenet')
tf_default_graph = tensorflow.get_default_graph()

save_path = Path(SAVE_DIR)
if save_path.exists() is False:
    save_path.mkdir(parents=True, exist_ok=True)


@app.route('/')
def root():
    """
    Handle the initial request to the root route.
    """
    return render_template('main.html')


@app.route('/upload_image', methods=['POST'])
def upload_image():
    """
    Process the uploaded image and classify using a Keras model.

    Returns
    -------
    output: json data
        JSON dictionary containing list of top 3 names and probability for each name.
    """
    image_file = request.files['file']
    log.debug(image_file)

    filename = secure_filename(image_file.filename)
    image_path = save_path / Path(filename)
    image_file.save(str(image_path))

    pil_img = Image.open(image_path)

    pil_img = pil_img.resize((IMAGE_HEIGHT, IMAGE_WIDTH), Image.BILINEAR)
    pil_img = np.array(pil_img)
    pil_img = pil_img.reshape((1, IMAGE_HEIGHT, IMAGE_WIDTH, IMAGE_CHANNELS))

    with tf_default_graph.as_default():
        x = tensorflow.keras.applications.resnet50.preprocess_input(pil_img)
        y_hat = model.predict(x)
        top3 = tensorflow.keras.applications.resnet50.decode_predictions(y_hat, top=3)[0]
        names = list(map(lambda e: e[1], top3))
        probs = list(map(lambda e: str(round(e[2] * 100, 1)) + "%", top3))

    return jsonify({
        "name": names,
        "probability": probs
    })
