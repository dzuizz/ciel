from ollama import Client
from model.context import Context


class localModel:
    def __init__(self, model: str = "llama3.2:1b") -> None:
        self.client = Client()
        self.context = Context()
        self.model = model

    def ask(self, qns: str):
        prompt = self.context.inject(qns)

        stream = self.client.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )

        response = []
        for chunk in stream:
            response.append(chunk["message"]["content"])
            yield chunk

        self.context.add_pair(qns, "".join(response))
