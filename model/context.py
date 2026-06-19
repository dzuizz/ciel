from pathlib import Path


def _ctx(name: str) -> Path:
    private = Path("env") / name
    return private if private.exists() else Path("env.example") / name


PROFILE = _ctx("PROFILE.md")
RULES = _ctx("RULES.md")
NOTES = _ctx("notes")  # TODO: add notes RAG


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
