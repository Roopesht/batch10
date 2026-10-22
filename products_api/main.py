from fastapi import FastAPI
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

