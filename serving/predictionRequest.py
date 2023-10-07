import requests


if __name__ == '__main__':

    WEB_SERVER_URI = "http://localhost:5000/predict_post"
    img_path = "./validation_image_label_four.jpeg"

    # REST Api Post call to send the request to Server which will predict the image
    # class and return the result in json format.
    response = requests.post(WEB_SERVER_URI, files={'file': open(img_path, 'rb')})

    print(" response: ", response.json())
