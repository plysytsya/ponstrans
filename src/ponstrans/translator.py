from collections import OrderedDict

from bs4 import BeautifulSoup
import requests

from ponstrans.supported_langs import pairs


class PONS:
    def __init__(self):
        self.pairs = pairs
        self.locales = {
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
            "lb": "Elvish",
        }

    def translate(self, word, source_lang, target_lang):
        url = self.find_url(source_lang, target_lang)
        query_url = url.replace("q=", f"q={word}")
        return self.scrape_translations(query_url)[1:]

    def find_url(self, source, target):
        found = [pair for pair in pairs if pair["source"] == source and pair["target"] == target]
        if len(found):
            return found[0]["url"]
        else:
            raise Exception(f"Language pair {source} - {target} is not supported.")

    def scrape_translations(self, url: str):
        translations = []
        html: str = requests.get(url).text
        soup = BeautifulSoup(html, features="html.parser")
        # results = soup.find("div", {"class": "entry first"})
        sources = soup.findAll("div", {"class": "source"})
        targets = soup.findAll("div", {"class": "target"})
        for source, target in zip(sources, targets):
            source_text = source.get_text().replace('\n', '').rstrip()
            target_text = target.get_text().replace('\n', '').rstrip()
            if {"source": source_text, "target": target_text} not in translations:
                translations.append({"source": source_text, "target": target_text})
        return translations  # removes dupes and drops first item


if __name__ == "__main__":
    pons = PONS()
    print(pons.translate("loben", "de", "es"))
