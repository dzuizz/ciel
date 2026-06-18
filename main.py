import time

from ollama import chat
from pathlib import Path


PROFILE = Path("PROFILE.md")
RULES = Path("RULES.md")
MODEL = "llama3.2:1b"


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
        # print(prompt)  TODO: implement error logs later

        stream = chat(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        start_stream = time.time()
        print("\rdoing something...", end="", flush=True)

        chunk = next(stream)
        print(f"\r{chunk['message']['content']}", end="", flush=True)

        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)
        print(flush=True)
        elapsed_stream = time.time() - start_stream
        print(f"answered in {elapsed_stream:.1f}s", flush=True)


if __name__ == "__main__":
    main()
