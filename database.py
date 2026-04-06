import os
from sqlalchemy import create_engine, text

# 100% BY LAADNANI

# We load the URL from environment variables to bypass GitHub secret protections!
DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_engine (DATABASE_URL,connect_args={"ssl": {}}, pool_pre_ping = True , pool_recycle = 300)

# creat an engine (connection) that connect to the avien database
# pool_pre_ping=True  : forces SQLAlchemy to transparently send a test ping (like SELECT 1) to the database every time you request a connection.
# pool_recycle=300: This proactively replaces connection objects in the pool before they get a chance to reach timeouts on the server side (recycling every 5 minutes).

def check_api_key_db(api_key : str):
    with engine.connect() as conn :
        query = text("SELECT * FROM api_keys WHERE api_key = :key")
        result = conn.execute(query,{"key" : api_key}).fetchone()

        return result is not None
