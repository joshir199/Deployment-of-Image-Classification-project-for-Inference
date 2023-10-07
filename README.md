# Deployment of Image Classification project for Inference using Flask Server
Creating deployment pipeline to deploy an Image Classification model using Flask and expose a REST API for model inference.

This project trains on standard MNIST dataset using Convolutional Neural Network (CNN) model architecture. It predicts the class which the digit shown as image in the input image files.
The Model is same as model used for Image classification in this ![image classification project](https://github.com/joshir199/Image-Classification-Using-CNN-PyTorch-project)

Further, Model deployment and Inference part of the project has been discussed in this project.

Following steps Can be followed sequentially to understand the model training, evaluation, deployment and Inference on WebServer pipeline.
----------------------------------------------
# Model Training

This project will download MNIST dataset from the standard dataset repo of PyTorch.
The dataset contains images of single digits from 0 and 9 and output label as digit.

Here's the commands to training, Please run the following commands by providing appropriate value for mentioned parameters.

full_path : full directory path to this folder where model weights will be saved after training
```bash
$ python main.py --train --seed 31 --learning_rate 0.005 --max_epoch 15
```

************************************************
# Model Evaluation
Trained Image Classification model is saved in the repository. When Evaluation is done, model is recreated using the trained model weights.

Here's the commands to evaluating, Please run the following commands by providing appropriate value for mentioned parameters.

```bash
$ python main.py --evaluate
```
**************************************************
# Model deployment with default inference on Flask Web Server

API endpoint is at '/predict' and Flask development server is initiated for running by typing following CLI command

```bash
$ python app.py
```
the response can be seen at the Web link : http://localhost:5000/ and endpoint : /predict

![Result at Web link ](https://github.com/joshir199/Deployment-of-Image-Classification-project-for-Inference/blob/main/images/Flask_server_output.png)

--------------------> Result at Web link : http://localhost:5000/predict


![](https://github.com/joshir199/Deployment-of-Image-Classification-project-for-Inference/blob/main/images/server_success_http_response.png)

---------------> Flask Server End result
*****************************************************
# Model Inference using REST Api POST requests to Web Server

Once the model is already deployed to Web Server for Inference, prediction can be easily done using REST calls with POST request sending image_file and Model Inference Endpoint Uri.

Server-Client Architecture is used for here.
Server Endpoint Uri : http://localhost:5000/predict_post

# Server Part
1. Run the Server using terminal/ CLI as below:
```bash
$ python app.py
```


# Client Part
2. Run the command with another terminal/CLI while keeping Web Server running in background using step 1.
   Go to /client folder and run following command:
```bash
$ python predictionRequest.py
```

At the Server End, If successful, success response code will be printed:

 "POST /predict_post HTTP/1.1" 200

At the Request Sender End, after successful post request, prediction result will be sent as response.
The response is sent in json format as mentioned as here: ![ json format for result](https://github.com/joshir199/Deployment-of-Image-Classification-project-for-Inference/blob/main/serving/digits_class_index.json)
  
  response:  {'class_id': 'd03', 'class_name': 'Three'}
