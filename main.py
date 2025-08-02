import warnings
from typing import Iterable

import spacy
from spacy import tokens


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
    Convert text into top to bottom, left to right format
    Use an NLP model to split up the text into words, 
    to ensure that the words aren't split into different columns
    """
    text_cols = [""]
    for token in parse_tokens(text, nlp):
        if len(token.orth_) + len(text_cols[-1]) > text_height:
            text_cols.append("")
        text_cols[-1] += token.orth_
    
    result = ""
    for row in range(0, text_height):
        for col in range(len(text_cols) - 1, -1, -1):
            char = text_cols[col][row] if row < len(text_cols[col]) else '　'
            result += char + ' ' # include space between the columns
        result += "\n"
    return result


if __name__ == "__main__":
    nlp = load_model()
    sentence = "これは日本語で書かれた文です。このプログラムはどの文を縦書きにできる機能を持っています"
    result = make_text_vertical(sentence, 8, nlp)
    print(result)
