import json
import platform

from src.AI_settings import AISettings
from src.chatGPT import askGPT
from src.text_voiceover import say
from src.voice_recognition import listen


def formatRequest(request: str):
    formattedRequest = {
        "request": request,
        "os": platform.system()
    }
    return f'{AISettings()}\n{json.dumps(formattedRequest)}'


def executePyCode(command: str):
    if command:
        exec(command)


def processRequest(request=''):
    if not request:
        return

    response = askGPT(formatRequest(request))

    print('\n\n\n')
    print('REQUEST:', request)
    print('RESPONSE:', response)

    try:
        resp = json.load(response)
        code = resp['command']
        message = resp['message']

        return {'code': code, 'message': message}
    except:
        return {'code': None, 'message': None}


def start():
    phrases = listen(True)
    for phrase in phrases:
        result = processRequest(phrase)
        executePyCode(result['code'])
        say(result['message'])
