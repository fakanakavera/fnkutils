# utils.py
import yaml
import os

def load_yaml(filename):
    choices_file = os.path.join(os.path.dirname(__file__), filename)
    with open(choices_file, 'r') as file:
        return yaml.safe_load(file)