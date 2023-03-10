from fastapi import FastAPI;
from enum import Enum;

app = FastAPI()

class ModelName(str, Enum):
    alexet  = "alexet",
    resnet = "resnet",
    lenet = "lenet",
    alisi = "alisi"


@app.get("/")
async def root():
    return {"message": "Hello world"}

@app.get("/items/{item_id}")
async def read_iteam(item_id: int):
    return {"item_id": item_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alisi:
        return {"model_name": model_name, "message": "Make life a better place with deep learning FTW!"}
    
    if model_name is ModelName.alexet:
        return {"model_name": model_name, "message": ""}
    
    return {"model_name": model_name, "message": "Have some residuals"}


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    return fake_items_db[skip : skip + limit]