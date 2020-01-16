# ponstrans


Unofficial client for PONS online dictionary


## Description

Translates words and finds example-sentences.

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
>>> find_examples("leben", "de", "es")
[{'source': 'jdm das Leben verlängern', 'target': 'alargar la vida de alguien'}, {'source': 'ein schweres Leben haben', 'target': 'tener una vida dura'}, {'source': 'in beständiger Angst leben', 'target': 'vivir con miedo permanente'}]
```

Note
====

This project has been set up using PyScaffold 3.2.3. For details and usage
information on PyScaffold see https://pyscaffold.org/.
