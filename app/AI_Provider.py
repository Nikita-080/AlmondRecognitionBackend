#app imports
from ConfigManager import ConfigManager
from ResourcesManager import ResourcesManager

#imports
from ultralytics import YOLO
from PIL import Image
import io

class AI_Provider():
    def __init__(self, config, resources):
        self.config = config
        self.resources = resources
        
        if self.config.test_mode:
            self.model = None
        else:
            self.model = YOLO(self.config.model_path)
                
    def GetAnswer(self, image_data):
        if self.config.test_mode:
            return self.resources.get("default_desease_name")
        else:
            image = Image.open(io.BytesIO(image_data))
            results = self.model.predict(source=image, conf=0.5)
            try:
                code = str(int(results[0].boxes.cls.item()))    
                name = self.resources.get_name_by_code(code)
                return name
            except Exception as e:
                print(e)
                return self.resources.get("recognision_error_text")
