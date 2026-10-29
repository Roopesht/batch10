from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from models import Product
from business_logic import add_product
app = FastAPI()

prods = [
    {"name": "pencil", "price":10, "stock": 25},
    {"name": "pen", "price":25, "stock": 75},

]

@app.get("/hello")
def hello():
    return {"msg": "Hello"}

@app.get("/products")
def get_products():
    prod_list = [p["name"] for p in prods]
    return {"msg": ",".join(prod_list) }

def get_username():
    #open database
    #get the table users
    #from the passed userid get the name
    return "Roopesh"

## Path parameter
@app.get("/product/{productid}")
def get_product(productid):
    price = [ p["price"] for p in prods if p["name"] == productid  ]

    if price:
        return {"msg": price }
    else:
        return {"msg": "product not founnd" }

## Query Parameter
@app.get("/productex")
def get_product(productid:str=None):

    price = [ p["price"] for p in prods if p["name"] == productid  ]
    if price:
        return {"msg": price }
    else:
        return {"msg": "product not founnd" }


@app.post("/product")
def create_product(product: Product):

    if product.name in ('gun', 'bomb'):
        raise HTTPException(
                    status_code=503,
                    detail=f"You are trying to add prohibitory item"
                )
            
    prod = {'name': product.name, 'price':  product.price, 'stock': product.stock}

    #prods.append (prod)
    add_product(prod)

    return {"msg": 'successful' }
