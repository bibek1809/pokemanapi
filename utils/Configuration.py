from utils.Env import Env
import os
import json
env = Env.instance()


db_user = env.get_or_default("postgressql.user", "admin")
db_password= env.get_or_default("postgressql.password", "admin")
db_host = env.get_or_default("postgressql.host", "admin")
db_port= env.get_or_default("postgressql.port", "admin")
db_database= env.get_or_default("postgressql.database", "admin")