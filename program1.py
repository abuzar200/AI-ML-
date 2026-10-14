"""Lab 01: a small, explainable rule-based AI assistant."""

from __future__ import annotations

import re


def reply(message: str) -> str:
    """Choose a response using transparent keyword rules (not an LLM)."""
    words = set(re.findall(r"[a-z]+", message.lower()))
    if not words:
        return "Please enter a question or greeting."
    if {'hi', 'hello', 'hey'} & words:
        return "Hello! Ask me about AI, Python, or how to get started."
    if 'ai' in words or {'artificial', 'intelligence'} <= words:
        return "Artificial intelligence lets computers perform tasks involving learning, reasoning and decisions."
    if 'python' in words:
        return "Python is useful for AI because it is readable and has strong data science libraries."
    if 'help' in words:
        return "Try: hello, what is AI?, why Python?, or bye."
    if {'bye', 'goodbye', 'quit'} & words:
        return "Goodbye. Keep experimenting!"
    return "I do not have a rule for that yet. You can teach me a new one."


def main() -> None:
    print('AI Lab 01 | Rule-based assistant (type bye to exit)')
    while True:
        try:
            message = input('You: ')
        except (EOFError, KeyboardInterrupt):
            print('\nSession ended.')
            return
        print('Bot:', reply(message))
        if {'bye', 'goodbye', 'quit'} & set(message.lower().split()):
            return


if __name__ == '__main__':
    main()
