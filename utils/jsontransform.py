from utils.loggerfactory import LoggerFactory
logger_factory = LoggerFactory.get_logger("jsontransform")

def transform_data(data_list,enmerate_keys:list):
    transformed_data = []
    for item in data_list:
        # Create a dictionary with dynamic keys
        item_dict = {}
        #['name', 'type', 'image']
        for index, key in enumerate(enmerate_keys):
            item_dict[key] = item[index]
        transformed_data.append(item_dict)
    logger_factory.info(f"Executing transformation:")
    return transformed_data