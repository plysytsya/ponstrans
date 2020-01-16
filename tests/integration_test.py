import unittest
from ponstrans import translate


class TestPONS(unittest.TestCase):

    def test_translate(self):
        translations = translate("hello", "en", "de")
        self.assertTrue(len(translations))


if __name__ == "__main__":
    unittest.main(verbosity=3)