import spacy

from liwc import LIWC
from liwc.utils import category_couter


nlp = spacy.load('pt_core_news_md')
liwc = LIWC('data/LIWC2007_Portugues_win.dic')

def test_liwc():
    print(liwc('abastecimento*'))


def test_counter():
    text = """
    Ler histórias é um jeito de fortalecer vínculos com a criança, se divertindo e se emocionando junto com ela.
    """
    print(category_couter(nlp, liwc, text))


if __name__ == '__main__':
    test_liwc()
    test_counter()