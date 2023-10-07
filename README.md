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
