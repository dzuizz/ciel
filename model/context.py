from pathlib import Path

PROFILE = Path("env/PROFILE.md")
RULES = Path("env/RULES.md")


class Context:
    def __init__(self) -> None:
        self.profile = PROFILE.read_text(encoding="utf-8")
        self.rules = RULES.read_text(encoding="utf-8")
        self.convo = []  # (prompt, answer)

    def inject(self, prompt) -> str:
        return "\n".join(["\n".join(self.convo), self.profile, self.rules, prompt])
        # TODO: (crude concat) replace with proper templating

    def add_pair(self, prompt: str, answer: str) -> None:
        self.convo.append((prompt, answer))
        # TODO: (convo size scales very fast) compress the context
