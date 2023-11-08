create_table = '''CREATE TABLE IF NOT EXISTS pokeman_table (
    name VARCHAR(255) Unique NOT NULL,
    image VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL);'''




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