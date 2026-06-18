from ollama import Client
from model.context import Context


class localModel:
    def __init__(self, model: str = "llama3.2:1b") -> None:
        self.client = Client()
        self.context = Context()
        self.model = model

    def ask(self, qns: str):
        self.context.add_message({"role": "user", "content": qns})

        stream = self.client.chat(
            model=self.model,
            messages=self.context.get_messages(),
            stream=True,
        )

        response = []
        for chunk in stream:
            response.append(chunk["message"]["content"])
            yield chunk

        self.context.add_message({"role": "assistant", "content": "".join(response)})
