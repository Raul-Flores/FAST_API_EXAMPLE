from pydantic import BaseModel

class ItemRequestModel(BaseModel):
    name: str
    price: int
    quantity: int

class ItemResponseModel(ItemRequestModel):
    id: int