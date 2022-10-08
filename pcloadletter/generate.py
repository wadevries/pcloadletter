"""
This module contains routines for generating invoices.
"""

import pathlib
from datetime import date, timedelta
from typing import Union

import yaml
from jinja2 import (
    Environment,
    FileSystemLoader,
    StrictUndefined,
    Undefined,
    is_undefined,
    select_autoescape,
)
from weasyprint import HTML


def load_context(context_file):
    """Loads context (a dict) from a given file"""

    context = yaml.safe_load(context_file)
    return context


def date_filter(value: Union[date, str, Undefined], date_format="%d-%m-%Y"):
    """Formats the given value as a date using `date_format`

    If value is a string it is first parsed as an ISO8601 formatted date.
    """

    if is_undefined(value):
        return value
    date_value = value if isinstance(value, date) else date.fromisoformat(value)
    return date_value.strftime(date_format)


def add_days(value: Union[str, Undefined], delta: int):
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
    env.filters["add_days"] = add_days
    env.filters["date"] = date_filter

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
