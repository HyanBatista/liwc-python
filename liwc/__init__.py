from typing import Dict, List, Tuple

from liwc.trie import TrieMixin


class LIWC(TrieMixin):
    """
    Reads a LIWC lexicon from a file in the .dic format, holding the lexicon and
    the category mapping, where:
    * `lexicon` is a dict mapping string patterns to lists of category names
    * `category_mapping` is a dictionary of category names (as strings) and values
    """

    def __init__(self, dic_filepath: str) -> None:
        lines = self._load_dic(dic_filepath)
        lines, category_mapping = self._parse_categories(lines)
        self.lexicon = self._parse_lexicon(lines, category_mapping)
        self.category_mapping = category_mapping
        self.trie = self.build_trie(self.lexicon)

    def __call__(self, token: str) -> List[str]:
        """
        Return a list with the categories of the given token.
        """
        return self.search_trie(self.trie, token)

    def _load_dic(self, dic_filepath) -> List[str]:
        lines = []
        with open(dic_filepath, 'r', encoding="ISO-8859-1") as f:
            for line in f.readlines():
                lines.append(line.replace('\n', ''))
        return lines

    def _parse_categories(self, lines: List[str]) -> Tuple[List[str], Dict[str, int]]:
        """
        Read (category_id, category_name) pairs from the categories section.
        Each line consists of an integer followed a tab and then the category name.
        This section is separated from the lexicon by a line consisting of a single "%".
        """
        category_mapping = {}

        if lines[0] != '%':
            raise Exception("File doesn't match required structure")
        else:
            lines.pop(0)
        while(lines[0] != '%'):
            category_id, category_name = lines[0].split('\t')
            category_mapping[category_id] = category_name
            lines.pop(0)
        lines.pop(0)
        return lines, category_mapping

    def _parse_lexicon(self, lines: List[str], category_mapping: Dict[str, int]) -> Dict[str, List[str]]:
        """
        Read (match_expression, category_names) pairs from the lexicon section.
        Each line consists of a match expression followed by a tab and then one or more
        tab-separated integers, which are mapped to category names using `category_mapping`.
        """
        lexicon = {}
        for line in lines:
            categories = line.split('\t')
            pattern = categories.pop(0)
            lexicon[pattern] = [
                category_mapping[category_id]
                for category_id in categories
            ]
        return lexicon
