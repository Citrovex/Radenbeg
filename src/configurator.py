import json
import platform


def getConfig():
    with open("config.json", "r") as jsonFile:
        data = json.load(jsonFile)
        schema = data["$schema"]
        if schema:
            language = schema["language"]
            nameOfUser = schema["nameOfUser"]
            nameOfBot = schema["nameOfBot"]
            formats = schema["formats"]

            return {
                'OS': platform.system(),
                language: language,
                nameOfBot: nameOfBot,
                nameOfUser: nameOfUser,
                formats: formats
            }

    jsonFile.close()


def setConfig(OS: str, language: str, nameOfBot: str, nameOfUser: str, formats: str):
    data = {
        OS: OS,
        language: language,
        nameOfBot: nameOfBot,
        nameOfUser: nameOfUser,
        formats: formats
    }

    with open("config.json", "w") as jsonFile:
        json.dump(data, jsonFile)
        jsonFile.close()
