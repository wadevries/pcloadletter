import argparse
from unittest import TestCase

from pcloadletter.parse import KeyValueAction


class KeyValueActionTest(TestCase):
    def setUp(self) -> None:
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('pairs', action=KeyValueAction, nargs='*')

    def test_parse_args(self):
        with self.subTest('Valid pairs'):
            options = self.parser.parse_args(['foo=bar', 'baz=bah'])
            self.assertEqual(
                {'foo': 'bar', 'baz': 'bah'},
                options.pairs
            )

        with self.subTest('No = in pair'):
            with self.assertRaises(ValueError, msg="Provide context as key=value pairs (got 'foobarbaz')"):
                self.parser.parse_args(['foobarbaz'])

        with self.subTest('No pairs'):
            options = self.parser.parse_args([])
            self.assertEqual(options.pairs, {})
