from utils.env import Env
from utils.tokenencryption import TokenEncryptor
env = Env.instance()


db_user = TokenEncryptor.decrypt_token(env.get_or_default("postgressql.user", "admin"))
db_password= TokenEncryptor.decrypt_token(env.get_or_default("postgressql.password", "admin"))
db_host = env.get_or_default("postgressql.host", "admin")
db_port= env.get_or_default("postgressql.port", "admin")
db_database= TokenEncryptor.decrypt_token(env.get_or_default("postgressql.database", "pokemon"))