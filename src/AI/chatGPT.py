import requests
import json


def askGPT(request: str = '') -> str:
    """
    Ask Chat GPT. Free usage.
    * Model — davinci-003
    ! Limited to 15 requests per day
    ! Has no chat history
    """

    response = requests.get(f"https://openai-api-yak3s7dv3a-ue.a.run.app/?q=null%0A%20Q%3A%20{request}%20%3F%20%0A%20A%3A%20&userid=cf69ae3bc8a585eb6f04cbfbe5696cfd6635796542a251d9ca91b2953529e7&segmentation=OPENAI_CHATGPT_VERSION", headers={
        "accept": "text/event-stream",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "dnt": "1",
        "origin": "https://merlin.foyer.work",
        "referer": "https://merlin.foyer.work/",
        "sec-ch-ua": "Not_A Brand\";v=\"99\", \"Microsoft Edge\";v=\"109\", \"Chromium\";v=\"109",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70",
    }, stream=True)

    result = ''

    for line in response.iter_lines():
        if line:
            try:
                result += json.loads(line.decode("utf-8").replace('data: ',
                                                                  ''))['choices'][0]['text']
            except:
                pass

    return result
