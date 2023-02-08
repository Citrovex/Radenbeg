import json
import platform
from AI_settings import AISettings

from chatGPT import askGPT
from text_voiceover import say
from voice_recognition import listen


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

    response = askGPT()
    try:
        resp = json.load(response)
        code = resp['command']
        message = resp['message']

        return {code: code, message: message}
    except SyntaxError as _e:
        pass

    print('\n\n\n')
    print('REQUEST:', request)
    print('RESPONSE:', response)


def start():
    phrases = listen(True)
    for phrase in phrases:
        result = processRequest(phrase)
        executePyCode(result.code)
        say(result.message)
