import requests


if __name__ == '__main__':

    FLASK_SERVER_URL = "http://localhost:5000/predict_post"
    FASTAPI_SERVER_URL = "http://localhost:8000/predict_post"
    img_path = "validation_image_label_four.jpeg"

    # Client Part
    # REST Api Post call to send the request to Server which will predict the image
    # class and return the result in json format.
    response = requests.post(FASTAPI_SERVER_URL, files={'file': open(img_path, 'rb')})

    print(" response: ", response.json())
