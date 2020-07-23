import yaml


def process_configs():
    with open("configs/config.yml", 'r') as file:
        configs = yaml.load(file, Loader=yaml.FullLoader)
    return configs


def get_path(configs):
    return configs["path"]