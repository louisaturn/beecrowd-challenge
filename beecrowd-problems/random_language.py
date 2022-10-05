# This module picks a random language
from pathlib import Path

import random

FILES_DIRECTORY = "beecrowd-problems"

LANGUAGES = {
    'C': {
        'extension':"c",
        'comment': "//"
        },
    'C++': {
        'extension':"cpp",
        'comment': "//"
        },
    'C#': {
        'extension':"cs",
        'comment': "//"
        },
    'Java': {
        'extension':"java",
        'comment': "//"
        },
    'Python': {
        'extension':"py",
        'comment': "#"
        },
    'Ruby': {
        'extension':"rb",
        'comment': "#"
        },
    'Scala': {
        'extension':".scala",
        'comment': "//"
        },
    'Go': {
        'extension':"go",
        'comment': "//"
        },
    'Kotlin': {
        'extension':"kt",
        'comment': "//"
        },
    'Javascript': {
        'extension':"js",
        'comment': "//"
        },
    'Lua': {
        'extension':"lua",
        'comment': "--"
        },
    'Pascal': {
        'extension':"pas",
        'comment': "//"
        },
    'Haskell': {
        'extension':"hs",
        'comment': "--"
        },
    'OCaml': {
        'extension':"ml",
        'comment': "(*"
        },
    'PHP': {
        'extension':"php",
        'comment': "//"
        },
    'Rust': {
        'extension':"rs",
        'comment': "//"
        },
    'R': {
        'extension':"r",
        'comment': "#"
        },
    'Clojure': {
        'extension':"clj",
        'comment': ";;"
        },
    'Dart': {
        'extension':"dart",
        'comment': "//"
        },
    'Elixir': {
        'extension':"ex",
        'comment': "//"
        },
    'Swift': {
        'extension':"swift",
        'comment': "//"
        }
}

def random_language():
    return (random.choice(list(LANGUAGES.keys())))


def create_file(problem, language):

    filepath = Path(f"{FILES_DIRECTORY}/{problem}.{LANGUAGES[language]['extension']}")
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with filepath.open("w") as f:
        # TODO: comment for each language on LANGUAGE
        f.write(f"{LANGUAGES[language]['comment']} Solution of: {problem} Language: {language}")
        f.close()

def next_problem():
    # look for the last problem solved and create a file for the next solution

    if any(Path(FILES_DIRECTORY).iterdir()):
        filepath = Path(FILES_DIRECTORY).glob("**/*")
        solutions = [x.stem for x in filepath if x.is_file]
        last_solution = (max(solutions))
        new = int(last_solution) + 1
        return str(new)

    # first problem: 1001
    return "1001"

create_file(next_problem(), random_language())