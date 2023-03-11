from EdgeGPT import Chatbot, ConversationStyle
from .AI_settings import SERVICE_START_RESPONSE, GetAISettings

from .chatGPT import askGPT


class AI:
    bingAI = None

    async def initBing(self):
        try:
            # Try to init Bing AI
            print("Initializing Bing AI...")
            bingAI = Chatbot(cookiePath='./cookies.json')
            response = await bingAI.ask(prompt=GetAISettings(), conversation_style=ConversationStyle.creative)
            answer = response['item']['messages'][1]['text']
            if answer == SERVICE_START_RESPONSE:
                print("Bing AI started")
                self.bingAI = bingAI
        except:
            print("Error: could not start Bing AI")

    async def ask(self, prompt: str):
        if (prompt):
            # Try to use Bing AI first
            if (self.bingAI):
                print("Asking Bing AI...")
                response = await self.bingAI.ask(prompt=prompt, conversation_style=ConversationStyle.creative)
                try:
                    answer = response['item']['messages'][1]['text']
                    if answer:
                        return answer
                except:
                    pass

            # Use ChatGTP
            print("Asking ChatGTP...")
            return askGPT(GetAISettings(inlineRequest=prompt))
