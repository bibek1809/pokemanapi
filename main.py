from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from fastapi.responses import JSONResponse
from entity.pokemontable import Pokemon
pokemon = Pokemon()
from utils.loggerfactory import LoggerFactory  # Import your LoggerFactory class
from utils import constant,validation
from config import configsetup
app = FastAPI()

logger = LoggerFactory.get_logger("main")

@app.get("/api/v{version}/pokemons", tags=["Pokemons"])
def get_pokemons(request: Request, version: int, name: str = Query(None, title="Pokemon Name"), type: str = Query(None, title="Pokemon Type")):    # if kwargs.keys(): 
    unexpected_params = set(request.query_params.keys()) - validation.get_params()
    if unexpected_params:
        logger.warning(f"Invalid params used: {unexpected_params}")
        error_message = constant.params_error["error"].format(unexpected_params)
        return JSONResponse(content=dict(constant.params_error, error=error_message), status_code=400)
    if version == 1:
        try:
            data = pokemon.get_details(name, type)
            logger.info("Data fetched successfully")
            return {"data": data}
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}")
            return JSONResponse(content=constant.server_error, status_code=500)
    else:
        logger.warning(f"Invalid version requested: {version}")
        return JSONResponse(content=constant.invalid_version, status_code=400)

        
@app.get("/")
async def home():
    # await configsetup.main()
    logger.info("Home endpoint accessed done.")
    return constant.Home, 200 

async def startup_event():
    max_retries = 10
    retry_interval_seconds = 5

    for retry_attempt in range(1, max_retries + 1):
        try:
            # Run your main function to set up the database
            await configsetup.main()
            logger.info("Database setup completed successfully.")
            break  # Break out of the loop if successful
        except Exception as e:
            logger.error(f"Error during database setup: {str(e)}")
            
            if retry_attempt < max_retries:
                logger.info(f"Retrying in {retry_interval_seconds} seconds (attempt {retry_attempt}/{max_retries}).")
                await asyncio.sleep(retry_interval_seconds)
            else:
                logger.error(f"Max retries reached. Unable to set up the database.")
                raise JSONResponse(content=f"Unable to set up the database: {str(e)}", status_code=500)



app.add_event_handler("startup", startup_event)



# CORS middleware for handling Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can customize this based on your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler
@app.exception_handler(Exception)
async def validation_exception_handler(request: Request, exc: Exception):
    logger.error(f"An unexpected error occurred: {str(exc)}")
    return JSONResponse(content=constant.server_error, status_code=500)
