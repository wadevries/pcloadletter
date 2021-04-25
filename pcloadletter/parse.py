"""
Utilities for parsing the command line arguments
"""
import argparse


class KeyValueAction(argparse.Action):  # pylint: disable=too-few-public-methods
    """Action that parses key=value pairs from the command line.

    >>> parser = argparse.ArgumentParser()
    >>> action = parser.add_argument('data', nargs='*', action=KeyValueAction)
    >>> parser.parse_args(['foo=bar', 'bla=bloep '])
    Namespace(data={'foo': 'bar', 'bla': 'bloep'})
    """

    def __call__(self, parser, namespace, values, option_string=None):
        for value in values:
            if "=" not in value:
                raise ValueError(f"Provide context as key=value pairs (got {value!r})")
        setattr(namespace, self.dest, dict(pair.strip().split("=", 1) for pair in values))
