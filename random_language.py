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
        'extension':"scala",
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

    file_path = Path(f"{FILES_DIRECTORY}/{problem}.{LANGUAGES[language]['extension']}")
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w") as f:
        problem_link = f"https://www.beecrowd.com.br/judge/problems/view/{problem}"
        comment = f"{LANGUAGES[language]['comment']} Solution of: {problem_link} Language: {language}"
       
        #close comment line (OCaml)
        f.write(f"{comment}*)" if language == 'OCaml' else f"{comment}")
        f.close()

def next_problem():
    # look for the last problem solved and create a file for the next solution

    if any(Path(FILES_DIRECTORY).iterdir()):
        file_path = Path(FILES_DIRECTORY).glob("**/*")
        solutions = [x.stem for x in file_path if x.is_file]
        last_solution = (max(solutions))
        new = int(last_solution) + 1
        return str(new)

    # first problem: 1001
    return "1001"

create_file(next_problem(), random_language())