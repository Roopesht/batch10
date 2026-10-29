from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str                   
    price: float    = Field(1, ge=1, le=100000)   
    stock: int=0      
