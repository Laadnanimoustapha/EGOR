import os
from sqlalchemy import create_engine, text

# 100% BY LAADNANI

# We load the URL from environment variables to bypass GitHub secret protections!
DATABASE_URL = os.environ.get("DATABASE_URL", "mysql+pymysql://avnadmin:YOUR_AIVEN_PASSWORD_HERE@mysql-258f62ab-nonasto372-88c3.g.aivencloud.com:23661/EGOR_DB")

engine = create_engine (DATABASE_URL,connect_args={"ssl": {}})# creat an engine (connection) that connect to the avien database


def check_api_key_db(api_key : str):
    with engine.connect() as conn :
        query = text("SELECT * FROM api_keys WHERE api_key = :key")
        result = conn.execute(query,{"key" : api_key}).fetchone()

        return result is not None
