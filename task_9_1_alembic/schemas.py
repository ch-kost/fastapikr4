from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    title: str
    price: float
    count: int
    description: str


class ProductOut(ProductCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
