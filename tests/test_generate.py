import datetime
from io import StringIO
from unittest import TestCase

from jinja2 import Undefined

from pcloadletter.generate import add_days, date_filter, load_context


class GenerateTest(TestCase):
    def test_load_context(self):
        f = StringIO("aap: noot\n")

        self.assertEqual(load_context(f), {"aap": "noot"})

    def test_date_filter(self):
        with self.subTest("With valid str"):
            self.assertEqual(date_filter("2021-04-25"), "25-04-2021")

        with self.subTest("With invalid str"):
            with self.assertRaises(ValueError, msg="Invalid isoformat string: '20214114'"):
                date_filter("20214114")

        with self.subTest("With date"):
            self.assertEqual(date_filter(datetime.date(2021, 2, 28)), "28-02-2021")

        with self.subTest("With format"):
            self.assertEqual(date_filter(datetime.date(2021, 2, 28), "%b"), "Feb")

        with self.subTest("With undefined"):
            self.assertEqual(date_filter(Undefined()), Undefined())

    def test_add_days(self):
        with self.subTest("With valid date"):
            self.assertEqual(add_days("2021-04-25", 7), datetime.date(2021, 5, 2))

        with self.subTest("With undefined"):
            self.assertEqual(add_days(Undefined(), 1), Undefined())
