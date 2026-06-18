from pathlib import Path

PROFILE = Path("env/PROFILE.md")
RULES = Path("env/RULES.md")


class Context:
    def __init__(self) -> None:
        self.profile = PROFILE.read_text(encoding="utf-8")
        self.rules = RULES.read_text(encoding="utf-8")
        self.convo = []  # (question, response)

    def inject(self, prompt) -> str:
        return "\n".join(
            [
                "\n".join(f"{q}\n{r}" for q, r in self.convo),
                self.profile,
                self.rules,
                prompt,
            ]
        )
        # TODO: (crude concat) replace with proper templating

    def add_pair(self, qns: str, response: str) -> None:
        self.convo.append((qns, response))
        # TODO: (convo size scales very fast) compress the context
