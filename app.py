from flask import Flask, request, jsonify
from utils import ServingUtil
from utils.ServingUtil import get_prediction, transform_image


# Server Part in Client-Server Architecture
# Flask’s main job is to handle HTTP requests and
# route them to the appropriate function in the application.
# Initializing the web server
app = Flask(__name__)


# Run the following command inside the folder that contains app.py
# It will put Flask in debug mode and providing helpful error messages,
# debug mode will trigger a reload of the application after all code changes.
# Without debug mode, you’d have to restart the server after every change.

# export FLASK_APP=app.py
# export FLASK_ENV=development

# Later, flask can be initiated using command : flask run

@app.get('/predict')  # rout decorator to connect GET to this function
def predict():
    img_path = "./images/validation_image_label_four.jpeg"
    image_tensor = ServingUtil.getTensorAfterTransformed(img_path)

    # Connecting with Database or Inference endpoint (in this case) for
    # creating response or result for REST API request
    class_id, class_name = get_prediction(image_tensor)
    print("class name: ", class_name)

    # Convert the result into JSON format
    return jsonify({'class_id': class_id, 'class_name': class_name})


@app.post('/predict_post')
def predict_post():
    print(" something ")

    image_file = request.files['file']
    image_bytes = image_file.read()
    image_tensor = transform_image(image_bytes=image_bytes)
    class_id, class_name = get_prediction(image_tensor)

    print("class name: ", class_name)
    return jsonify({'class_id': class_id, 'class_name': class_name})


if __name__ == '__main__':
    app.run()
