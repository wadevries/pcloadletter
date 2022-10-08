"""Make invoices, easy!"""

__version__ = "0.1.0"

import argparse
import pathlib
import textwrap

from pcloadletter.generate import generate_invoice
from pcloadletter.parse import KeyValueAction


class HelpFormatter(argparse.RawTextHelpFormatter, argparse.ArgumentDefaultsHelpFormatter):
    """Combine RawTextHelpFormatter and ArgumentDefaultsHelpFormatter"""


def main(argv=None):
    """Main entry point of pcloadletter"""

    parser = argparse.ArgumentParser(
        formatter_class=HelpFormatter,
        description="Generate PDF file from a Jinja-rendered HTML template",
        # pylint: disable=C0301, C0303
        epilog=textwrap.dedent(
            """
            Examples:

                pcloadletter --template templates/invoice.html --out invoice.pdf invoice_number=2021-001 invoice_date=`date +%Y-%m-%d`
            
            """  # noqa: E501, W293
        ),
    )
    parser.add_argument(
        "-t",
        "--template",
        type=pathlib.Path,
        default="invoice.html",
        help="The invoice template to render.",
    )
    parser.add_argument(
        "-o",
        "--out",
        default="invoice.pdf",
        help="Destination file.",
    )
    parser.add_argument(
        "-c",
        "--context-file",
        type=argparse.FileType("r"),
        help="A .yml or .json file containing context for the template.",
    )
    parser.add_argument(
        "extra_context",
        nargs="*",
        action=KeyValueAction,
        help="key=value pairs which are added to the template context",
    )
    # pylint: disable=C0301, C0303
    parser.epilog = textwrap.dedent(
        """
        Examples:
        
            pcloadletter --template templates/invoice.html --out invoice.pdf invoice_number=2021-001 invoice_date=`date +%Y-%m-%d`
        
            pcloadletter --template report.html --context-file=report-data.yml addressee="Mr. M. Bolton"
        """  # noqa: E501, W293
    )

    options = parser.parse_args(argv)
    generate_invoice(
        options.template,
        options.out,
        options.context_file,
        options.extra_context,
    )


if __name__ == "__main__":
    main()
