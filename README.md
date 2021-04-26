# pcloadletter
A CLI tool to generate PDF documents from HTML templates

---

_"PC LOAD LETTER" - WFT does that mean?!_


[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]

## Installation

```
pip install pcloadletter
```

## Usage

pcloadletter lets you generate a pdf document from an HTML [Jinja template](https://jinja.palletsprojects.com/)
given some context data from the command line and/or a .yml/.json file.

```
usage: pcloadletter [-h] [-t TEMPLATE] [-o OUT] [-c CONTEXT_FILE] [extra_context ...]

Generate PDF file from a Jinja-rendered HTML template

positional arguments:
  extra_context         key=value pairs which are added to the template context (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        The invoice template to render. (default: invoice.html)
  -o OUT, --out OUT     Destination file. (default: invoice.pdf)
  -c CONTEXT_FILE, --context-file CONTEXT_FILE
                        A .yml or .json file containing context for the template. (default: None)

Examples:

    pcloadletter --template templates/invoice.html --out invoice.pdf invoice_number=2021-001 invoice_date=`date +%Y-%m-%d`

    pcloadletter --template report.html --context-file=report-data.yml addressee="Mr. M. Bolton"
```

For example, given a template file `hello.html`:

```html
<!doctype html>
<html lang="en">
<head>
    <link rel="stylesheet" href="styles.css" />
</head>
<body>
    <h1>Hello {{ target }}!</h1>
</body>
</html>
```
and a stylesheet:
```css
.h1 {
    font-style: italic;
}
```
we can render the pdf like so;

```shell
pcloadletter --template hello.html target="world out there"
```

The context could have been given in a context file `hello.yml`;
```yaml
target: world out there
```

```shell
pcloadletter --template hello.html --context-file=hello.yml
```

The above commands will generate a file `invoice.pdf` in the current directory. You can
change the destination using 

```--out=~/Documents/report.pdf```


[pypi-image]: https://img.shields.io/pypi/v/pcloadletter
[pypi-url]: https://pypi.org/project/pcloadletter/
[build-image]: https://github.com/wadevries/pcloadletter/actions/workflows/build.yml/badge.svg
[build-url]: https://github.com/wadevries/pcloadletter/actions/workflows/build.yml
