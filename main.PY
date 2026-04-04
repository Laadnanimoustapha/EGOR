from fastapi import FastAPI , Header, HTTPException
import random
import string
import os
from RateLimit_Manager import check_API_rate_limit
from database import check_api_key_db

# FULLY MAID BY LAADNANI 

app = FastAPI() # Initailazing the server

# MAIN FUNCTIN FOR GENERATING PASSWORD
def gnreat_password(length = 12):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choice(chars) for _ in range(length))

#SHOWING PAGES 
@app.get('/')
def home_Page() :
    return {"message" : "welcom to EGOR"}

@app.get("/generate")
def generate(length: int = 12 , x_api_key: str = Header(...)):
    
    #CHECK IF API KEY IS IN THE DATABASE
    if not check_api_key_db(x_api_key):
        raise HTTPException(
            status_code = 401,
            detail = "INVALID API KEY ⚠"
        )

    check_API_rate_limit(x_api_key)
    return {"password" : gnreat_password(length)}
