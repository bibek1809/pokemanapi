from typing import Union
from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse
from utils.dbhelper import DatabaseHelper
from service import dbservice,requestservice
import asyncio
import asyncpg
from utils import Configuration,constant
import datetime
app = FastAPI()

db_details = {"user":Configuration.db_user, "password":Configuration.db_password,
                             "host":Configuration.db_host,"port":Configuration.db_port,"database":Configuration.db_database}
db_helper = DatabaseHelper(db_details=db_details)


@app.get("/api/v{version}/pokemons", tags=["Pokemons"])
def get_pokemons(version: int,name: str = None,params: str = None):
    if version == 1:
        data = dbservice.get_details(name,params)
        return {"data": data}  
    else:
        return JSONResponse(content=constant.invalid_version, status_code=400)

@app.get("/")
def home():
    return constant.Home, 200 


@app.on_event("startup")
async def startup_event():
    # Run your main function to set up the database
    await main()

async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect('postgresql://admin:admin@localhost/pokemon')
    # Execute a statement to create a new table.
    await conn.execute(constant.create_table)
    requestservice.fetchdetails()
    # Insert a record into the created table.
    await conn.execute('''
        INSERT INTO pokeman_table(name, image, type)
        VALUES ('test', 'files', 'hi')
        ON CONFLICT (name) DO UPDATE
        SET image = EXCLUDED.image, type = EXCLUDED.type;

    ''')


    # Close the connection.
    await conn.close()
