from collections import Counter

from spacy.language import Language

from liwc import LIWC


def category_couter(nlp: Language, liwc: LIWC, text: str) -> Counter:
    text_tokens = [w.lower_ for w in nlp(text)]
    return Counter(category for token in text_tokens for category in liwc(token))
