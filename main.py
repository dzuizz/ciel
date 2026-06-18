from ollama import chat


def main():
    msg = input("> ")
    stream = chat(
        model="qwen3.5:latest", messages=[{"role": "user", "content": msg}], stream=True
    )

    for chunk in stream:
        print(chunk["message"]["content"], end="", flush=True)


if __name__ == "__main__":
    main()
