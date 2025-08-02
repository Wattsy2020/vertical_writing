import sys
import warnings
from typing import Iterable

import spacy
from spacy import tokens

DEFAULT_TEXT_HEIGHT = 8


def load_model() -> spacy.language.Language:
    # ignore a warning from huggingface that the ginza library needs to fix
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return spacy.load('ja_ginza_electra')


def parse_tokens(text: str, nlp: spacy.language.Language) -> Iterable[tokens.Token]:
    """Parse tokens using the ginza model"""
    for sent in nlp(text).sents:
          for token in sent:
            yield token


def make_text_vertical(text: str, text_height: int, nlp: spacy.language.Language) -> str:
    """
    A small program to convert Japanese text into top-to-bottom, left-to-right format
    Uses an NLP model to split up the text into words, 
    to ensure that the words aren't split into different columns
    """
    text_cols = [""]
    for token in parse_tokens(text, nlp):
        if len(token.orth_) + len(text_cols[-1]) > text_height:
            text_cols.append("")
        text_cols[-1] += token.orth_
    
    # Some words might have more characters then the text_height limit, in which case they will extend the column height 
    max_height = max(map(lambda str: len(str), text_cols))
    result = ""
    for row in range(0, max_height):
        for col in range(len(text_cols) - 1, -1, -1):
            char = text_cols[col][row] if row < len(text_cols[col]) else '　'
            result += char + ' ' # include space between the columns
        result += "\n"
    return result


def get_text_height_arg() -> int:
    if len(sys.argv) < 2:
        return DEFAULT_TEXT_HEIGHT
    if not sys.argv[1].isdecimal():
        return DEFAULT_TEXT_HEIGHT
    arg_height = int(sys.argv[1])
    return arg_height if arg_height > 0 else DEFAULT_TEXT_HEIGHT


if __name__ == "__main__":
    nlp = load_model()
    sentence = input()
    text_height = get_text_height_arg()
    result = make_text_vertical(sentence, text_height, nlp)
    print(result)
