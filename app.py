from flask import Flask, request, jsonify
from utils import ServingUtil
from utils.ServingUtil import get_prediction

app = Flask(__name__)


@app.route('/predict')
def predict():
    img_path = "./images/validation_image_label_four.jpeg"
    image_tensor = ServingUtil.getTensorAfterTransformed(img_path)

    class_id, class_name = get_prediction(image_tensor)
    print("class name: ", class_name)
    return jsonify({'class_id': class_id, 'class_name': class_name})


if __name__ == '__main__':
    app.run()
