from openai import OpenAI
from config import OPENAI_API_KEY


class AresAI:

    def __init__(self):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY
        )


    def sor(self, mesaj):

        cevap = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Sen ARES isimli kişisel yapay zeka asistanısın. Geliştiricin Cemal Yiğit Üstün."
                },
                {
                    "role": "user",
                    "content": mesaj
                }
            ]
        )

        return cevap.choices[0].message.content

