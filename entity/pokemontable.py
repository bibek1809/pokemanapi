from entity.entity import Entity
from utils.loggerfactory import LoggerFactory
from utils.jsontransform import transform_data
logger_factory = LoggerFactory.get_logger("pokemontable")

class Pokemon(Entity):
    def get_details(self,name,type):
        where_condition = ''
        if name and type:
            where_condition = f'''where name= '{name}' and  type ILIKE '%{type}%' '''

        elif name:
            where_condition = f'''where name= '{name}' '''


        elif type:
            where_condition = f'''where type ILIKE '%{type}%' '''

        else:
            pass

        query = f'''select distinct name, type, image  from pokeman_table {where_condition}'''
        logger_factory.info(f"Executing query: {query}")
        result = self.db_helper.execute_query(query,fetch=True)
        keys = ['name', 'type', 'image']
        return transform_data(result,keys)
    
    def insert_details(self,values):
        query = f'''INSERT INTO pokeman_table(name, type,image) {values}'''
        logger_factory.info(f"Executing Insert Query:")
        self.db_helper.execute_query(query)