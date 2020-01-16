import unittest
from ponstrans.translator import PONS


class TestPONS(unittest.TestCase):

    def setUp(self):
        self.pons = PONS()

    def test_translate(self):
        translations = self.pons.translate("hello", "en", "de")
        self.assertTrue(len(translations))

    def test_get_examples(self):
        examples = self.pons.find_examples("leben", "de", "es")
        self.assertTrue(len(examples))


if __name__ == "__main__":
    unittest.main(verbosity=3)