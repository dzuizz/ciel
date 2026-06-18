from ollama import chat
from pathlib import Path


PROFILE = Path("PROFILE.md")
RULES = Path("RULES.md")


def get_prompt(msg: str) -> str:
    profile_text = PROFILE.read_text(encoding="utf-8")
    rules_text = RULES.read_text(encoding="utf-8")
    return "\n".join([rules_text, profile_text, msg])


def main() -> None:
    while True:
        msg = input("> ")
        if msg == "quit":
            print("byee")
            break

        prompt = get_prompt(msg)
        print(prompt)

        stream = chat(
            model="qwen3.5:latest",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)
        print()


if __name__ == "__main__":
    main()
