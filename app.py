from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/prediction')
def predict_image_class():
    prediction = 1
    print("predicted class is : ", prediction)


if __name__ == '__main__':
    app.run()