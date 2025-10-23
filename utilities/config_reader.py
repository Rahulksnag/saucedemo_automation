import configparser

def read_config(section, key):
    config = configparser.ConfigParser()
    config.read("./config/config.ini")
    return config.get(section, key)
