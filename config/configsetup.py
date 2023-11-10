from service import dbservice,requestservice
import asyncpg
from utils import constant
from utils.loggerfactory import LoggerFactory
logger = LoggerFactory.get_logger("configsetup")
async def main():
    try:
        # Establish a connection to an existing database named "test"
        # as a "postgres" user.
        conn = await asyncpg.connect(dbservice.db_helper.create_conn_string())
        # Execute a statement to create a new table.
        await conn.execute(constant.create_table)
        data_list = requestservice.fetchdetails()
        # Insert a record into the created table.
        await  conn.executemany(constant.insert_query, data_list)
        logger.info(f"Configuration Setup Completed!!!!")

        # Close the connection.
        await conn.close()
    except Exception as e:
        logger.error(f"An error occurred in the main function: {str(e)}")
    