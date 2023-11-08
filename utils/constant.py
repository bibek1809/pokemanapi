create_table = '''CREATE TABLE IF NOT EXISTS pokeman_table (
    name VARCHAR(255) Unique NOT NULL,
    image VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL);'''

insert_query = '''
        INSERT INTO pokeman_table(name, type, image)
        VALUES ($1, $2, $3)
        ON CONFLICT (name) DO UPDATE
        SET image = EXCLUDED.image, type = EXCLUDED.type;
    '''



invalid_version= {
"success": False,
"code": 400,
"error": 'BAD_REQUEST',
"message": 'Invalid Version !'
}


Home= {
"success": True,
"code": 200,
"error": 'Valid Request',
"message": 'Valid Request !'
}