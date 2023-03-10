import json
import platform

from AI_settings import GetAISettings
from chatGPT import askGPT
from text_voiceover import say
from voice_recognition import listen

AI_SETTINGS = GetAISettings()


def formatRequest(request: str):
    formattedRequest = {
        "request": request
    }
    return f'{AI_SETTINGS}{json.dumps(formattedRequest)}'


def executePyCode(command: str):
    if command:
        try:
            exec(command)
        except Exception as e:
            print('Error: could not execute command. Message: {0}'.format(e))


def processRequest(request=''):
    if not request:
        return

    response = askGPT(formatRequest(request))

    print('\n\n\n')
    print('REQUEST:', request)
    print('RESPONSE:', response)

    try:
        resp = json.loads(response)
        code = resp['code']
        answer = resp['answer']

        return {'code': code, 'answer': answer}
    except Exception as e:
        print('Error: could not parse response. Error: {0}'.format(e))
        return {'code': None, 'answer': None}


def start():
    phrases = listen(True)
    for phrase in phrases:
        result = processRequest(phrase)
        executePyCode(result['code'])
        say(result['answer'])


executePyCode(processRequest(
    formatRequest('Open random Youtube video'))['code'])
