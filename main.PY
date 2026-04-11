from sqlalchemy import engine
from fastapi import FastAPI , Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from pydantic import BaseModel
import secrets # better cryptographic
import string
from python.RateLimit_Manager import check_API_rate_limit
from python.database import check_api_key_db,engine
from python.EGOR_PAGE import HTML_PAGE
from python.ai_summarizer import get_summarize_and_explanation

    #---------------- FULLY MAID BY LAADNANI ------------------------#

class SummarizeRequest(BaseModel):
    text:str

# Initailazing the server
app = FastAPI(title="EGOR",description="main server by me ladnani",version="1.2.0",docs_url=None,redoc_url =None) 

#allow requestes frome frontends
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://hrms-two-iota.vercel.app"], # will add new urls inchalaah in the future 
    allow_methods=["GET","POST"],
    allow_headers=["x_api_key"],
)

# check length f the passwored requested
def check_password_lenth(length):
    if length < 8 or length > 100 :
        raise HTTPException(status_code = 400, detail="length must be bteween 8 and 100")

# MAIN FUNCTIN FOR GENERATING PASSWORD
def generate_password(length = 12):
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(secrets.choice(chars) for _ in range(length))

# start the db check when the server boot up # no tasks yet 
# @app.on_event("startup")
# async def statrup_events():
#     asyncio.create_task(fake_request())

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

@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn :
            conn.execute(text("SELECT 1"))
        return {"status":"healthy","database":"connected"}
    except Exception:
        raise HTTPException(status_code=503, detail="database unreachable")

@app.post("/api/summarize")
def summarize(request:SummarizeRequest, x_api_key: str = Header(...)):
    if not check_api_key_db(x_api_key):
        raise HTTPException(status_code = 401, detail = "INVALID API KEY ⚠")
    
    check_API_rate_limit(x_api_key,LIMIT=1)
    
    try :
        result = get_summarize_and_explanation(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))