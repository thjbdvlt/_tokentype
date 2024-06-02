import re
import spacy.lookups


def _generate_regex_emoticon():
    """Genère une expression régulière pour match les émoticons.

    Returns (str):  une expression régulière pour match les émoticons.

    Combine des signes utilisés pour les yeux, le nez, la bouche pour construire une série d'émoticons.

    exemples
    --------
        :-)
        D-;
        >:^)
    """

    # side emoticons, like: :-)
    eyebrowsleft = r">?"
    eyebrowsright = r"<?"
    eyes = r"[\:=;8x%]'?"
    nose = r"[-o\^]?"
    mouth = r"[\(\)\]\[\}\{\}dp0o/31\*\|\><x#]+"
    sideleft = eyebrowsleft + eyes + nose + mouth
    sideright = mouth + nose + eyes + eyebrowsright

    # face emoticons, like: o.O
    facemouth = r"(?:\.|_+)"
    faceeyes = [
        r"[oO0@]",
        r"[vV]",
        r"\.",
        r"-",
        r";",
        r"\^",
        r"[<>]",
    ]
    facesemoticons = [i + facemouth + i for i in faceeyes]

    # any emoticons (face or side)
    anyemoticon = r"|".join(
        [rf"(?:{i})" for i in [sideright, sideleft] + facesemoticons]
        + [r"(?:</?3)"]
    )

    return anyemoticon


_isemoticon = re.compile(_generate_regex_emoticon()).fullmatch
_isemoji = re.compile(r":\w+:").fullmatch
_isurl = re.compile(r"(?:\w+://|www\.)[\S]+[\w/]").search
_isemail = re.compile(r"[\w\.\-]@[\w\.\-]+\.[\w\.\-]").search


def gettype(s):
    """Définit le type d'une string: mot, nombre, emoticon, url, etc.

    Args:
        s (str): la string dont il faut identifier le type.

    Note:
        l'ordre des conditions est important.
    """

    if s.isspace():
        return "space"
    elif _isemoji(s):
        return "emoji"
    elif _isemoticon(s):
        return "emoticon"
    elif _isurl(s) or _isemail(s):
        return "url"
    elif any([char.isalpha() for char in s]):
        return "word"
    elif any([char.isdigit() for char in s]):
        return "number"
    else:
        return "punct"


class Typifier:
    def __init__(self):
        self.table = spacy.lookups.Table()

    def __call__(self, doc):
        table = self.table
        for token in doc:
            norm = token.norm
            if norm in table:
                token._.tokentype = table[norm]
            else:
                _type = gettype(token.text)
                token._.tokentype = _type
                table[norm] = _type
        return doc
