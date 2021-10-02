# {{cookiecutter.project_slug}}

{{cookiecutter.description}}

This is a plugin for [Python LSP Server](https://github.com/python-lsp/python-lsp-server).

## Installation

Install into the same virtualenv as python-lsp-server itself.

``` bash
pip install {{ cookiecutter.project_slug }}
```

## Configuration

... TODO ...

## Features

This plugin adds the following features to `pylsp`:

- ... TODO ...

## Developing

Install development dependencies with (you might want to create a virtualenv first):

``` bash
git clone {{cookiecutter.repository_url}} {{cookiecutter.project_slug}}
cd {{cookiecutter.project_slug}}
pip install -e '.[dev]'
```

{%- if cookiecutter.test_type == 'pytest' %}

Run `pytest` to run plugin tests.
{%- endif %}

{% if cookiecutter.publishing_type == "Publish to PyPI using twine" %}
## Publishing

If this is your first time publishing to PyPI, follow the instruction at [Twine
docs](https://packaging.python.org/guides/distributing-packages-using-setuptools/#create-an-account)
to create an PyPI account and setup Twine.

Build a package using setuptools:

``` bash
python setup.py sdist
twine check dist/*
```

Then upload using Twine:

```
twine upload dist/*
```

Alternatively, you may want to upload to test PyPI first before going live:

```
twine upload --repository testpypi dist/*
```
{%- endif %}

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) from 
[lieryan/cookiecutter-pylsp-plugin](https://github.com/lieryan/cookiecutter-pylsp-plugin)
project template.
