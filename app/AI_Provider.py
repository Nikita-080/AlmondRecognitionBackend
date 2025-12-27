#app imports
from ConfigManager import ConfigManager
from ResourcesManager import ResourcesManager

class AI_Provider():
    def __init__(self, config, resources):
        self.config = config
        self.resources = resources
        
        if self.config.test_mode:
            self.model = None
        else:
            pass
                
    def GetAnswer(self, image):
        if self.config.test_mode:
            return self.resources.get("default_desease_name")
        else:
            pass
