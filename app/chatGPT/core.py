import openai

MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.5


class ChatGPT:
    @staticmethod
    def get_chat_response(prompt: str) -> str:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": ""
                },
                {"role": "user", "content": prompt},
            ],
            temperature=TEMPERATURE,
        )

        return response["choices"][0]["message"]["content"]
