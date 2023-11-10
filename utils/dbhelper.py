from sqlalchemy import create_engine,text
from utils.loggerfactory import LoggerFactory  


class DatabaseHelper:

    def __init__(self,db_details):
        self.user = db_details['user']
        self.password = db_details['password']
        self.host = db_details['host']
        self.port = db_details['port']
        self.database = db_details['database']
        self.logger_factory = LoggerFactory.get_logger("dbhelper")

    def create_conn_string(self):
        self.connection_str = f'''postgresql://{self.user}:{self.password}@db:{self.port}/{self.database}'''
        # self.logger_factory.info(f"{self.connection_str}")
        return self.connection_str
        #return "postgresql://admin:admin@localhost/pokemon"

    def create_engine(self):
        try:
            engine = create_engine(self.create_conn_string())
            self.logger_factory.info("Database engine created successfully.")
            return engine
        except Exception as e:
            self.logger_factory.error(f"Error creating database engine: {str(e)}")
            raise
    

    def execute_query(self, query, fetch=False):
        connection = self.create_engine().connect()
        sql = text(query)
        try:
            if fetch is False:
                connection.execute(sql)
                return True
            results = connection.execute(sql).fetchall()
            self.logger_factory.info(f"Executed query: {query}")
            return results
        except Exception as e:
            self.logger_factory.error(f"Error executing query: {query}, Error: {str(e)}")
            raise