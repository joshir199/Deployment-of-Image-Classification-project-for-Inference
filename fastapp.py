from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from utils import ServingUtil
from utils.ServingUtil import get_prediction, transform_image, getTensorAfterTransformed

fastapp = FastAPI()


class LabelResult(BaseModel):
    class_id: str
    class_name: str


@fastapp.get('/predict')
async def predict():
    img_path = "./images/validation_image_label_four.jpeg"
    image_tensor = ServingUtil.getTensorAfterTransformed(img_path)

    # Connecting with Database or Inference endpoint (in this case) for
    # creating response or result for REST API request
    class_id, class_name = get_prediction(image_tensor)
    print("class name: ", class_name)

    # Convert the result into JSON format
    return LabelResult(class_id=class_id, class_name=class_name)


@fastapp.post('/predict_post')
async def predict_post(image_file: UploadFile = File(...)):

    image = await image_file.read()
    image_tensor = transform_image(image_bytes=image)
    class_id, class_name = get_prediction(image_tensor)

    print("class name: ", class_name)
    return LabelResult(class_id=class_id, class_name=class_name)



# Calling FastAPI Server using terminal:
# uvicorn file_name:FastAPI_variable_name --reload
# uvicorn fastapi:fastapi --reload
"""
reload : It will reload the Server if already running. And If any changes made to fastapi file, the server will
         automatically reload without any need to manually restart the Server.
"""