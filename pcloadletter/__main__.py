"""Make invoices, easy!"""

__version__ = "0.1.0"

import argparse
import pathlib
from datetime import date, timedelta
from typing import Union

import yaml
from jinja2 import (
    Environment,
    FileSystemLoader,
    StrictUndefined, is_undefined, select_autoescape,
)
from weasyprint import HTML

from pcloadletter.parse import KeyValueAction


def load_context(context_file):
    """Loads context (a dict) from a given file"""

    context = yaml.safe_load(context_file)
    return context


def date_filter(value: Union[date, str], date_format='%d-%m-%Y'):
    """Formats the given value as a date using `date_format`

    If value is a string it is first parsed as an ISO8601 formatted date.
    """

    if is_undefined(value):
        return value
    date_value = value if isinstance(value, date) else date.fromisoformat(value)
    return date_value.strftime(date_format)


def add_days(value: str, delta: int):
    """Adds `delta` number of days to `value`"""

    if is_undefined(value):
        return value
    return date.fromisoformat(value) + timedelta(delta)


def generate_invoice(
    template=pathlib.Path("invoice.html"),
    destination="invoice.pdf",
    context_file=None,
    extra_context=None,
):
    """Generate an invoice (pdf)"""
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"]),
        undefined=StrictUndefined,
    )
    env.filters['add_days'] = add_days
    env.filters['date'] = date_filter

    context = {}
    if context_file:
        context.update(load_context(context_file))
    if extra_context:
        context.update(extra_context)

    loaded_template = env.get_template(str(template))

    rendered_html = loaded_template.render(**context)
    html = HTML(
        string=rendered_html,
        base_url=str(template.parent),
    )
    html.write_pdf(destination)


def main(argv=None):
    """Main entry point of pcloadletter"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--template",
        type=pathlib.Path,
        default="invoice.html",
        help="The invoice template to render. Defaults to invoice.html",
    )
    parser.add_argument(
        "--out",
        default="invoice.pdf",
        help="Destination file.",
    )
    parser.add_argument(
        '--context-file',
        type=argparse.FileType('r'),
    )
    parser.add_argument('extra_context', nargs='*', action=KeyValueAction)

    options = parser.parse_args(argv)
    generate_invoice(
        options.template,
        options.out,
        options.context_file,
        options.extra_context,
    )


if __name__ == "__main__":
    main()
