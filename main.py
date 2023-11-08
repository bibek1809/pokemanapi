from typing import Union
from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
from services.dbhelper import DatabaseHelper
import asyncio
import asyncpg
from utils import Configuration
import datetime
app = FastAPI()

db_details = {"user":Configuration.db_user, "password":Configuration.db_password,
                             "host":Configuration.db_host,"port":Configuration.db_port,"database":Configuration.db_database}
db_helper = DatabaseHelper(db_details=db_details)


@app.get("/")
def complete_configuration():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup_event():
    # Run your main function to set up the database
    await main()

async def main():
    # Establish a connection to an existing database named "test"
    # as a "postgres" user.
    conn = await asyncpg.connect(db_helper.create_conn_string)
    # Execute a statement to create a new table.
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS pokeman_table (
    name VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL
        )

    ''')

    # Insert a record into the created table.
    await conn.execute('''
        INSERT INTO pokeman_table(name, image,type) VALUES($1, $2)
    ''')

    # Select a row from the table.
    row = await conn.fetchrow(
        'SELECT * FROM users WHERE name = $1', 'Bob')
    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))

    # Close the connection.
    await conn.close()

@app.get("/api/v1/pokemons")
def get_pokemons(name: str = None, type: str = None):
    return hello
