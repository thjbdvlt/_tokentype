import re
import spacy.lookups
import spacy.tokens.token


def _generate_regex_emoticon():
    """Generate a regular expression that matches emoticons.

    Returns (str):  regular expression.

    Combines signs used for eyes, nose, mouth, ..., to build many emoticons.

    examples
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


isemoticon = re.compile(_generate_regex_emoticon()).fullmatch
isemoji = re.compile(r":\w+:").fullmatch
isurl = re.compile(r"(?:\w+://|www\.)[\S]+[\w/]").search
isemail = re.compile(r"[\w\.\-]@[\w\.\-]+\.[\w\.\-]").search


def gettype(s):
    """Get the token type of a string.

    Args:
        s (str):  the string.

    Note:
        The order of conditions matter!
    """

    nchars = len(list(filter(str.isalpha, s)))

    if s.isspace():
        return "space"
    elif isemoji(s):
        return "emoji"
    elif isemoticon(s) and (nchars < 2 or "xd" in s.lower()):
        return "emoticon"
    elif isurl(s) or isemail(s):
        return "url"
    elif nchars != 0:
        return "word"
    elif any(map(str.isdigit, s)):
        return "number"
    else:
        return "punct"


class Typifier:
    def __init__(self, extname):
        self.table = spacy.lookups.Table()
        self.extname = extname
        spacy.tokens.token.Token.set_extension(extname, default=None)

    def __call__(self, doc):
        table = self.table
        for token in doc:
            norm = token.norm
            if norm in table:
                setattr(token._, self.extname, table[norm])
            else:
                _type = gettype(token.text)
                setattr(token._, self.extname, _type)
                table[norm] = _type
        return doc


@spacy.Language.factory("tokentype", default_config={"name": "tokentype", "extname": "tokentype"})
def create_tokentypifier(nlp, name, extname):
    return Typifier(extname)
