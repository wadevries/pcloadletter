# Sample template

This directory contains a modified version of the 'Invoice' 
sample from [WeasyPrint](https://weasyprint.org/samples/) ([source code](https://github.com/Kozea/WeasyPrint/tree/gh-pages/samples/invoice)).

Styling, markup, layout and appearance are all made by WeasyPrint. Please read the 
LICENSE contained in this directory.

## Usage

To generate the sample invoice, clone/checkout/download this directory. Then,
to generate an invoice with the invoice date set to 'today':

```shell
pcloadletter --template samples/invoice.html --context-file samples/context.yml date=`date +%Y-%m-%d`
```

This takes some content from [context.yml](context.yml). JSON formatted files are also accepted (as 
JSON is a subset of YAML), see [context.json](context.json).
