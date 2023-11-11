from utils.loggerfactory import LoggerFactory
from utils.dbhelper import DatabaseHelper
from utils import constant
logger_factory = LoggerFactory.get_logger("entity")


class Entity:
    def __init__(self):
        self.db_helper = DatabaseHelper(db_details=constant.db_details)
