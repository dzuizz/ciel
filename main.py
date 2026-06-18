import time

from model.olma import localModel


def main() -> None:
    model = localModel()

    while True:
        msg = input("> ")
        if msg == "quit":
            print("byee")
            break

        start_stream = time.time()
        print("\rdoing something...", end="", flush=True)

        stream = model.ask(msg)

        chunk = next(stream)
        print(f"\r{chunk['message']['content']}", end="", flush=True)

        for chunk in stream:
            print(chunk["message"]["content"], end="", flush=True)

        elapsed_stream = time.time() - start_stream
        print(f"\n\nanswered in {elapsed_stream:.1f}s", flush=True)


if __name__ == "__main__":
    main()
