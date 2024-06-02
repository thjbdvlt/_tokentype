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

nlp = spacy.load("fr_core_news_sm")
nlp.add_pipe("_tokentype")
```

configuration
-------------

as the module does nearly nothing, there is not much you can configure, but you can change the extension name:


```python
import spacy
import _tokentype

nlp = spacy.load("fr_core_news_sm")

@spacy.Language.factory("custom_tokentype")
def create_tokentypifier(nlp, name="custom_tokentype"):
    return Typifier(extname="TOKEN_SUBCLASS")

nlp.add_pipe("custom_tokentype")
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
