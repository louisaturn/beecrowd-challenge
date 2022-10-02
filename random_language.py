# This module picks a random language
from pathlib import Path
import random

FILES_DIRECTORY = "beecrowd_problems"

LANGUAGES = {
    'C':"c",
    'C++':"cpp",
    'C#':"cs",
    'Java':"java",
    'Python':"py",
    'Ruby':"rb",
    'Scala':".scala",
    'Go':"go",
    'Kotlin':"kt",
    'Javascript':"js",
    'Lua':"lua",
    'Pascal':"pas",
    'Haskell':"hs",
    'OCaml':"ml",
    'PHP':"php",
    'Rust':"rs",
    'R':"r",
    'Clojure':"clj",
    'Dart':"dart",
    'Elixir':"ex",
    'Swift':"swift",
}

def random_language():
    return (random.choice(list(LANGUAGES.keys())))


def create_file(problem, language):

    filepath = Path(f"{FILES_DIRECTORY}/{problem}.{LANGUAGES[language]}")
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with filepath.open("w") as f:
        f.write(f"Solution of {problem} on {language}:")
        f.close()

create_file("1", random_language())