import os,inspect
from utils import constant
def get_params():
    frame = inspect.currentframe().f_back
    calling_function_name = frame.f_code.co_name
    calling_file_name = frame.f_globals['__file__']
    file_name = os.path.basename(calling_file_name).split('.')[0]
    return constant.data[file_name][calling_function_name]