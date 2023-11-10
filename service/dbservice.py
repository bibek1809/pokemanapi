# from config import configuration
from utils.dbhelper import DatabaseHelper
from utils import constant
from utils.loggerfactory import LoggerFactory  
from config import configuration
logger_factory = LoggerFactory.get_logger("dbservice")

db_helper = DatabaseHelper(db_details=constant.db_details)

def get_details(name,params):
    where_condition = ''
    if name and params:
        where_condition = f'''where name= '{name}' and  type ILIKE '%{params}%' '''

    elif name:
        where_condition = f'''where name= '{name}' '''


    elif params:
        where_condition = f'''where type ILIKE '%{params}%' '''

    else:
        pass

    query = f'''select distinct name, type, image  from pokeman_table {where_condition}'''
    logger_factory.info(f"Executing query: {query}")
    result = db_helper.execute_query(query,fetch=True)
    return transform_data(result)

def transform_data(data_list):
    transformed_data = []
    for item in data_list:
        # Create a dictionary with dynamic keys
        item_dict = {}
        for index, key in enumerate(['name', 'type', 'image']):
            item_dict[key] = item[index]
        transformed_data.append(item_dict)
    logger_factory.info(f"Executing transformation:")
    return transformed_data

    
def insert_details(values):
    query = f'''INSERT INTO pokeman_table(name, type,image) {values}'''
    logger_factory.info(f"Executing Insert Query:")
    db_helper.execute_query(query)
