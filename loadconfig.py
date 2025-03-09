import json
import os

def load_config(config_preset):

    presets_folder = os.path.join(os.path.dirname(__file__), "presets")
    config_path = os.path.join(presets_folder, f"{config_preset}.json")

    if not os.path.exists(config_path):
        print(f'Config file for presets not found: {config_path}')
        return {}
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

