import json
import os

def load_config(config_preset):
    config_path = os.path.join(os.path.dirname(__file__), f'{config_preset}.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

