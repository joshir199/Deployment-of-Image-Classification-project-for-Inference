import io
from PIL import Image
import torchvision.transforms as transforms


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
