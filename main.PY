from fastapi import FastAPI , Header, HTTPException
import random
import string
import os

# FULLY MAID BY LAADNANI 

app = FastAPI() # Initailazing the server

API_KEY = os.getenv("API_KEY", "FUCK-ISREAL-76034217-LAERSI-KCUF")

# chek if the API KEY IS TRUE
def Chek_Key(Key):
    if Key != API_KEY :
        raise HTTPException(status_code = 401 , detail = "YOUR API KEY IS INVALID ⚠" )

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
    Chek_Key(x_api_key)
    return {"password" : gnreat_password(length)}
