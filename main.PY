from fastapi import FastAPI , Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import secrets # using secrets instead of randome for batter cryptographi protection
import string
import os
import asyncio
from RateLimit_Manager import check_API_rate_limit
from database import check_api_key_db
from EGOR_PAGE import HTML_PAGE

# FULLY MAID BY LAADNANI 

# Initailazing the server
app = FastAPI(title="EGOR",description="main sercer by me ladnani",version="1.2.0",docs_url="/docs") 

#allow requestes frome frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["x_api_key"],
)

DATABASE_URL = os.environ.get("DATABASE_URL")  

#cheking evry 10 seconds if the database is still running
async def fake_request(fake_api = "123456-limkoe-kuasu"): 
    while True : 
        try :
            check_api_key_db(fake_api)
        except Exception as e:
            print(f"EGOR_DB RUN INTO THISE :{e}")
        await asyncio.sleep(20)

# check length f the passwored requested
def check_password_lenth(length):
    if length < 8 or length > 100 :
        raise HTTPException(status_code = 400, detail="length must be bteween 8 & 100")

# MAIN FUNCTIN FOR GENERATING PASSWORD
def generate_password(length = 12):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(secrets.choice(chars) for _ in range(length))

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
    
    check_password_lenth(length)
    check_API_rate_limit(x_api_key)
    return {
        "status" : "success",
        "data":{
              "password" : generate_password(length)
        }
    }
