import json

class ResourcesManager():
    def __init__(self):
        with open("resources/resources.json", encoding='utf-8') as file:  
            self.data = json.load(file)
                
    def get(self, key):
        return self.data[key]

    def get_recomendation(self, key):
        return self.data["recomendations"][key]
