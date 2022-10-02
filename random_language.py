# This module picks a random language
from pathlib import Path

import random

FILES_DIRECTORY = "beecrowd-problems"

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
        # TODO: comment the text bellow
        f.write(f"Solution of: {problem} Language: {language}")
        f.close()

# first problem: 1001
# create_file("1001", random_language())

def next_problem():
    filepath = Path(FILES_DIRECTORY).glob("**/*")
    solutions = [x.stem for x in filepath if x.is_file]
    last_solution = (max(solutions))
    new = int(last_solution) + 1
    return str(new)

create_file(next_problem(), random_language())