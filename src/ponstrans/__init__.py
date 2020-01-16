# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound
from ponstrans.translator import PONS


def translate(word, source_language, target_language):
    pons = PONS()
    return pons.translate(word, source_language, target_language)


def find_examples(word, source_language, target_language):
    pons = PONS()
    return pons.find_examples(word, source_language, target_language)


try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
finally:
    del get_distribution, DistributionNotFound
