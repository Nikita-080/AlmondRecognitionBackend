import json

class ConfigManager():
    def __init__(self):
        with open("config/config.json", encoding='utf-8') as file:  
            data = json.load(file) 
            self.test_mode = data["test_mode"]
        
