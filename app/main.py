#app imports
from AI_Provider import AI_Provider
from ConfigManager import ConfigManager
from ResourcesManager import ResourcesManager

#imports
from typing import Annotated
from fastapi import FastAPI, File
import json

config = ConfigManager()
resources = ResourcesManager()
ai_provider = AI_Provider(config, resources)

app = FastAPI()

@app.post("/GetDeseaseRecognision")
def get_desease_recognision(file: Annotated[bytes, File()]):
    desease = ai_provider.GetAnswer(file)
    recomendation = resources.get_recomendation(desease)
    return [desease, recomendation]

    
