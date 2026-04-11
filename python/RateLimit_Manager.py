from fastapi import HTTPException
import time
import redis
import os


REDIS_URL = os.getenv("REDIS_URL")

if not REDIS_URL :
    raise RuntimeError("REDIS URL IS NOTE PROVIDED OR IS WRONG")

redis_client = redis.from_url(REDIS_URL, decode_responses = True) # creat connectin with redis and decode response frome bytes 

def check_API_rate_limit(api_key: str, LIMIT: int = 5, WINDOW: int = 60):

    now = time.time()
    redis_key = f"API_KEY_RATE_LIMIT:{api_key}" # to creat cnnection with redis upstash 

    redis_client.zremrangebyscore(redis_key,'-inf', now - WINDOW) # remove reqrstes older thatn 60s for thise api key
    courrent_requests = redis_client.zcard(redis_key) # count the valide requests
    
    # check the rate limit
    if courrent_requests >= LIMIT :
        raise HTTPException(
            status_code = 429,
            detail = "Too many requests, try again after 60s "
        )
    
    redis_client.zadd(redis_key, {str(now):now}) # add the new request
    redis_client.expire(redis_key,WINDOW) # delet the entier api_key rate limit requestes is inactive for 60s