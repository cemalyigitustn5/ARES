import ollama


def sor(mesaj):

    cevap = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "system",
                "content":
                "Sen ARES isimli kişisel yapay zeka asistanısın. Geliştiricin Cemal Yiğit Üstün. Türkçe konuş."
            },
            {
                "role": "user",
                "content": mesaj
            }
        ]
    )

    return cevap["message"]["content"]
