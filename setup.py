from setuptools import setup

setup(
    name="tokentype",
    entry_points={
        "spacy_factories": ["tokentype = tokentype.tokentype:create_tokentypifier"]
    }
)
