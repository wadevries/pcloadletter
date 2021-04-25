"""Make invoices, easy!"""

__version__ = "0.1.0"

import argparse
import pathlib

from pcloadletter.generate import generate_invoice
from pcloadletter.parse import KeyValueAction


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
        "--context-file",
        type=argparse.FileType("r"),
    )
    parser.add_argument("extra_context", nargs="*", action=KeyValueAction)

    options = parser.parse_args(argv)
    generate_invoice(
        options.template,
        options.out,
        options.context_file,
        options.extra_context,
    )


if __name__ == "__main__":
    main()
