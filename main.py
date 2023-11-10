from typing import Union
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.exceptions import RequestValidationError
# from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse
from service import dbservice
from utils.loggerfactory import LoggerFactory  # Import your LoggerFactory class
from utils import constant
from config import configsetup
app = FastAPI()

logger = LoggerFactory.get_logger("main")

@app.get("/api/v{version}/pokemons", tags=["Pokemons"])
def get_pokemons(version: int, name: str = None, params: str = None):
    if version == 1:
        try:
            data = dbservice.get_details(name, params)
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
    try:
    # Run your main function to set up the database
        await configsetup.main()
    except Exception as e:
        logger.error(f"An error occurred during startup: {str(e)}")
        return JSONResponse(content=f"An error occurred during startup: {str(e)}", status_code=500)




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
