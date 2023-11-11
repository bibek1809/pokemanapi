from config import configuration
create_table = '''drop table pokeman_table; CREATE TABLE IF NOT EXISTS pokeman_table (
    name VARCHAR(255) Unique NOT NULL,
    type VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL);'''

insert_query = '''
        INSERT INTO pokeman_table(name, type, image)
        VALUES ($1, $2, $3)
        ON CONFLICT (name) DO UPDATE
        SET type = EXCLUDED.type,image = EXCLUDED.image;
    '''



invalid_version= {
"success": False,
"code": 400,
"error": 'BAD_REQUEST',
"message": 'Invalid Version !'
}
server_error= {
"success": False,
"code": 400,
"error": 'Server Error',
"message": 'Server Error !'
}
params_error= {
"success": False,
"code": 400,
"error": 'Invalid params used:{}',
"message": 'Parameter Error !'
}


Home= {
"success": True,
"code": 200,
"error": 'Valid Request',
"message": 'Valid Request !'
}
db_details = {"user":configuration.db_user, "password":configuration.db_password,
                             "host":configuration.db_host,"port":configuration.db_port,"database":configuration.db_database}

data = {
    "main":{
        "get_pokemons":{'name','type'}
    }
}
