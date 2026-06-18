from pathlib import Path

PROFILE = Path("env/PROFILE.md")
RULES = Path("env/RULES.md")


class Context:
    def __init__(self) -> None:
        self.profile = PROFILE.read_text(encoding="utf-8")
        self.rules = RULES.read_text(encoding="utf-8")
        self.messages = [{"role": "system", "content": self.get_context()}]

    def add_message(self, message) -> None:
        self.messages.append(message)

    def get_context(self) -> str:
        return "\n".join([self.profile, self.rules])

    def get_messages(self):
        return self.messages
