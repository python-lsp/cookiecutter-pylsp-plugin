# {{cookiecutter.project_slug}}

{{cookiecutter.description}}

This is a plugin for the [Python LSP Server](https://github.com/python-lsp/python-lsp-server).

## Installation

Install into the same virtualenv as python-lsp-server itself.

```
pip install {{ cookiecutter.project_slug }}
```

## Configuration

... TODO ...

## Developing

Install development dependencies with (you might want to create a virtualenv first):

```
git clone {{cookiecutter.repository_url}} {{cookiecutter.project_slug}}
cd {{cookiecutter.project_slug}}
pip install -e '.[dev]'
```

{%- if cookiecutter.test_type == 'pytest' %}

Run `pytest` to run plugin tests.
{%- endif %}


{%- if cookiecutter.publishing_type == "Publish to PyPI using twine" %}
## Publishing

```
python -m build
twine upload dist/*
```
{%- endif %}

## Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[lieryan/cookiecutter-pylsp-plugin](https://github.com/lieryan/cookiecutter-pylsp-plugin)
project template.
