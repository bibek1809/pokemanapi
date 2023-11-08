from sqlalchemy import create_engine,text


class DatabaseHelper:

    def __init__(self,db_details):
        self.user = db_details['user']
        self.password = db_details['password']
        self.host = db_details['host']
        self.port = db_details['port']
        self.database = db_details['database']

    def create_conn_string(self):
        self.connection_str = f'''postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'''
        return self.connection_str
        #return "postgresql://admin:admin@localhost/pokemon"

    
    def create_engine(self):
        engine = create_engine(self.create_conn_string())
        return engine

    
    def execute_query(self,query,fetch=False):
        connection = self.create_engine().connect()
        sql = text(query)
        if fetch == False:
            connection.execute(sql)
            return True
        results = connection.execute(sql).fetchall()
        print(results)
        return results
