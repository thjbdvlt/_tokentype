\_tokentype
===========

|token|type|
|-----|----|
|hello|word|
|12|number|
|p.10|word|
|:-)|emoticon|
|=P|emoticon|
|:happy:|emoji|
|www.on-tenk.com|url|
|...|punct|

usage
-----

```python
import spacy
import _tokentype

nlp = spacy.load("fr_core_news_sm")
nlp.add_pipe("_tokentype")

for token in nlp("ho! :-)"):
    print(token, token._.tokentype)
# ho word
# ! punct
# :-) emoticon
```

configuration
-------------

as the module does nearly nothing, there is not much you can configure, but you can change the extension name:


```python
import spacy
import _tokentype

nlp = spacy.load("fr_core_news_sm")
nlp.add_pipe("_tokentype", name="quoi", config={"extname": "kindoftoken"})
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
