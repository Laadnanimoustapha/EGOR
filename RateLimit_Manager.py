from fastapi import HTTPException
import time

LIMIT = 5       # 5 times
WINDOW = 60     # in 60 secndes

request_log = {} # store requests

def check_API_rate_limit(api_key: str):

    now = time.time()

    # if api key is note in added we add him
    if api_key not in request_log :
        request_log[api_key] = []

    # if request are ver 60s will get deleted
    request_log[api_key] = [
        t for t in request_log[api_key]
        if now - t < WINDOW
    ]

    # check the rate limit
    if len(request_log[api_key]) >= LIMIT :
        raise HTTPException(
            status_code = 429,
            detail = "too meny requests, try agin after 60s"
        )
    
    # add the new request 

    request_log[api_key].append(now)
