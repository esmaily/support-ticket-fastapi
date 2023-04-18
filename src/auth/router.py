# from .dependencies import valid_post_id
from fastapi import APIRouter, status
# from pydantic import BaseModel, root_validator

from enum import Enum
from starlette.responses import Response


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


api_router = APIRouter()

@api_router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@api_router.get(
    "/login",
    status_code=status.HTTP_200_OK,
    description="for test",
    responses={}
)
async def get_post_by_id():
    return {
        "nane": "test"
    }
