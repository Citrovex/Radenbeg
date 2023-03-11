import json
from .AI.AI_settings import formatRequest

from .AI.ai import AI

from .text_voiceover import say
from .voice_recognition import listen

ai = AI()


def executePyCode(command: str):
    if command:
        try:
            exec(command)
        except Exception as e:
            print('Error: could not execute command. Message: {0}'.format(e))


async def processRequest(request=''):
    if not request:
        return

    response = await ai.ask(formatRequest(request))

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


async def start():
    await ai.initBing()

    phrases = listen(True)
    for phrase in phrases:
        result = await processRequest(phrase)
        executePyCode(result['code'])
        say(result['answer'])
