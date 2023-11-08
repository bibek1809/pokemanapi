from utils.dbhelper import DatabaseHelper
from utils import Configuration,constant

db_details = {"user":Configuration.db_user, "password":Configuration.db_password,
                             "host":Configuration.db_host,"port":Configuration.db_port,"database":Configuration.db_database}
db_helper = DatabaseHelper(db_details=db_details)

def get_details(name,params):
    where_condition = ''
    if name and params:
        where_condition = f'''where name= '{name}' and type like '%{params}%' '''

    elif name:
        where_condition = f'''where name= '{name}' '''


    elif params:
        where_condition = f'''where type like '%{params}%' '''

    else:
        pass

    query = f'''select distinct name, image, type  from pokeman_table {where_condition}'''
    print(query)
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
    return transformed_data

    
def insert_details(values):
    query = f'''INSERT INTO pokeman_table(name, image,type) {values}'''
    db_helper.execute_query(query)
