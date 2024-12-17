from decouple import config
import configparser


def load_settings():
    config = configparser.ConfigParser()
    config.read("settings.ini")

    min_number = int(config["GAME_SETTINGS"]["min_number"])
    max_number = int(config["GAME_SETTINGS"]["max_number"])
    attempts = int(config["GAME_SETTINGS"]["attempts"])
    starting_balance = int(config["GAME_SETTINGS"]["starting_balance"])

    return min_number, max_number, attempts, starting_balance
