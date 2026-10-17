from  fastapi import FastAPI
app = FastAPI()
import logging
logging.basicConfig(level=logging.INFO)

@app.get("/hello")
def hello():
    return {"msg": "Hello"}

@app.get("/login")
def login():
    logging.info(f"1. Received login request for item: ")
    
    # Validation already done by FastAPI!
    logging.info("2. Validation passed")
    
    # Processing
    logging.info("3. Processing item...")
    
    # Response
    logging.info("4. Sending response")
    return {"msg": "You are logged in"}

@app.post("/register")
def register():

    return {"msg": "You are logged in"}

