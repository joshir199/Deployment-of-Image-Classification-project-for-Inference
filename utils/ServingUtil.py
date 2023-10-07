import io
import torch
import json
from PIL import Image
import torchvision.transforms as transforms
from model.ConvolutionalNNModel import ConvolutionalNNModel


def getServingTransformFn(image_size):
    compose = transforms.Compose([transforms.Resize((image_size, image_size)),
                                  transforms.ToTensor()])
    return compose


def transform_image(image_bytes):
    print(" image transform starts")
    my_transforms = getServingTransformFn(16)
    image = Image.open(io.BytesIO(image_bytes)).convert("L")
    return my_transforms(image).unsqueeze(0)


def getTensorAfterTransformed(img_path):
    with open(img_path, 'rb') as f:
        print("file read starts")
        image_bytes = f.read()
        tensor = transform_image(image_bytes=image_bytes)
        print(" tensor shape: ", tensor.shape)
        return tensor


def get_prediction(test_image):
    path = "./output/model_checkpoint.pt"
    model = ConvolutionalNNModel(need_BN=False)
    model.load_state_dict(torch.load(path))
    print(" model loaded")
    output = model(test_image)
    # get index of maximum value : argmax
    _, yhat = torch.max(output.data, 1)

    predicted_idx = str(yhat.item())
    digits_class_index = json.load(open('./serving/digits_class_index.json'))

    return digits_class_index[predicted_idx]
