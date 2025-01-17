tokentype
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

nlp = spacy.load("fr_core_news_sm")
nlp.add_pipe("tokentype")

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

nlp = spacy.load("fr_core_news_sm")
nlp.add_pipe("tokentype", name="quoi", config={"extname": "kindoftoken"})
```

# installation

```bash
git clone https://github.com/thjbdvlt/tokentype tokentype
cd tokentype
pip install .
```

dependencies
------------

- spacy
