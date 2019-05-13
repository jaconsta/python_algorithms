import unittest

from parenthesis_match import parenthesis_match


class TestParenthesis (unittest.TestCase):
    def test_close_parenthesis_easy(self):
        text = '(){}'
        words_match = parenthesis_match(text)
        self.assertEqual(words_match, True)

    def test_close_parenthesis_medium(self):
        text = '[{()()}({[]})]({}[({})])((((((()[])){}))[]{{{({({({{{{{{}}}}}})})})}}}))[][][]'
        words_match = parenthesis_match(text)
        self.assertEqual(words_match, True)

    def test_miss_close(self):
        text = '({(()))}}'
        words_match = parenthesis_match(text)
        self.assertEqual(words_match, False)
