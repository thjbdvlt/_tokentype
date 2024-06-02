\_tokentype
===========

|token|type|
|-----|----|
|hello|word|
|12|number|
|p.10|word|
|:-)|emoticon|
|:-P|emoticon|
|:happy:|emoji|
|www.on-tenk.org|url|
|...|punct|

usage
-----

```python
import spacy
import _tokentype

@spacy.Language.factory("_tokentype")
def create_tokentypifier(nlp, name="_tokentype"):
    return _tokentype.Typifier()

nlp = spacy.load("fr_core_news_sm")
nlp.add_pipe("_tokentype")
```

# installation

```bash
git clone https://github.com/thjbdvlt/_tokentype _tokentype
cd _tokentype
pip install .
```

dependencies
------------

- spacy
- python 3.8
