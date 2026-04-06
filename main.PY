from fastapi import FastAPI , Header, HTTPException
import random
import string
import os
import asyncio
from RateLimit_Manager import check_API_rate_limit
from database import check_api_key_db
from EGOR_PAGE import HTML_PAGE

# FULLY MAID BY LAADNANI 

app = FastAPI() # Initailazing the server

DATABASE_URL = os.environ.get("DATABASE_URL") # TO SEND REGULARLY REQUESTS TO THE DATABASE T KEEP IT RUNNING

async def fake_request(fake_api = "123456-limkoe-kuasu"): #cheking evry 10 seconds if the database is still running
   while True : 
        try :
            check_api_key_db(fake_api)
        except Exception as e:
            print(f"EGOR_DB RUN INTO THISE :{e}")
        await asyncio.sleep(10)

# MAIN FUNCTIN FOR GENERATING PASSWORD
def gnreat_password(length = 12):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choice(chars) for _ in range(length))

# start the db check when the server boot up 
@app.on_event("startup")
async def statrup_events():
    asyncio.create_task(fake_request())

#SHOWING MAIN PAGES 
@app.get('/')
def home_Page() :
    return HTML_PAGE

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
