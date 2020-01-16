![GitHub Actions status | sdras/awesome-actions](https://github.com/plysytsya/ponstrans/workflows/tests/badge.svg)
[![codecov](https://codecov.io/gh/plysytsya/ponstrans/branch/master/graph/badge.svg)](https://codecov.io/gh/plysytsya/ponstrans/branch/master/graph/badge.svg)
![PyPI](https://img.shields.io/pypi/v/ponstrans)

# ponstrans


Unofficial client for PONS online dictionary


## Description

Translates words scraping https://en.pons.com/ in the background.

Supported languages:
```
"ar": "Arabic",
"bg": "Bulgarian",
"zh": "Chinese",
"nl": "Dutch",
"en": "English",
"fr": "French",
"de": "German",
"el": "Greek",
"it": "Italian",
"la": "Latin",
"pl": "Polish",
"pt": "Portuguese",
"ru": "Russian",
"sl": "Slovenian",
"es": "Spanish",
"tr": "Turkish",
"cs": "Czech",
"da": "Danish",
"hu": "Hungarian",
"no": "Norwegian",
"sv": "Swedish",
"lb": "Elvish"
```

## Installation
```
pip install ponstrans
```

## Usage

```
>>> from ponstrans import translate, find_examples
>>> translations = translate(word="hallo", source_language="de", target_language="en")
>>> translations[:2]
[{'source': 'hallo', 'target': 'hello'}, {'source': 'hallo (zur Begrüßung)', 'target': 'hi'}]
```

Note
====

The performance is quite bad because it scrapes the whole
html page in the background. Use the official (paid) API for better performance:
https://en.pons.com/p/online-dictionary/developers/api
