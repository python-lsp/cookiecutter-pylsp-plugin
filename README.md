# cookiecutter-pylsp-plugin

Using cookiecutter-pylsp-plugin is the easiest way to start writing pylsp
plugin. This repo also aims to document how python-lsp-plugins plugins are
wired if you want to do-it-yourself instead of using the template.

## Features

- License selection
- Optionally configure PyTest with some basic fixtures
- Optionally configure publishing to PyPI using Twine
- Optionally configure Github project metadata (e.g. `ISSUE_TEMPLATE.md`)

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

```
pip install -U cookiecutter
```

Generate a pylsp plugin project:

```
cookiecutter https://github.com/lieryan/cookiecutter-pylsp-plugin
```

Follow the prompts to configure your plugin project.

Install your plugin to the same environment as `pylsp` so that it can discover
your plugin.

```
pip install --editable 'path/to/package/'
```

## Writing hooks

The most important file in the generated package is `plugin.py`, this is where
you will write pylsp hooks. The pylsp hooks corresponds to Language Server
Protocol messages, you should read through the 
[LSP specification](https://microsoft.github.io/language-server-protocol/specification).
for the hook that you want to use.

A pylsp hook is a function with a specific name, decorated by `@hookimpl`:

```
@hookimpl
def pylsp_definitions(config, workspace, document, position):
    ...
```

Refer to [list of hookspecs](https://github.com/python-lsp/python-lsp-server/blob/develop/pylsp/hookspecs.py)
for the full list of all supported hooks.

Don't confuse `@hookimpl` with the `@hookspec` decorator, which is used to
define hooks. You'll almost never need to use `@hookspec` when writing a
plugin.

You should also write some tests for your hooks. If you choose to use `pytest`
when generating the template, you should have everything you needed to start
writing basic test in the `test/test_plugin.py` file. The `test/fixtures.py`
contains some useful functions that you'll likely need to test your hooks.
Refer to [pytest documentation](https://docs.pytest.org/) if you are unfamiliar
with how to write tests in pytest.


## pylsp plugin developer documentation

The following section documents how pylsp plugin is wired to pylsp. You do not
need to understand this section if you creating your plugin from this
cookiecutter template, but it may help you if you needed to make changes to the
`entry_points` setup when using this template, or if you want to replicate what
this template does in your own project that does not use this template.

On startup, pylsp will automatically discover plugins by querying
[`pkg_resources` for entrypoints](https://setuptools.pypa.io/en/latest/pkg_resources.html#entry-points).
So that your plugin can be discovered by pylsp, you must configure the
following in the `setup.py`/`setup.cfg` of your plugin's package:

```
[options.entry_points]
pylsp = pylsp_myplugin = pylsp_myplugin.plugin
```

The entrypoint name can be anything but it's recommended to use the same name
as your plugin package's import name.

Next, you need to install your plugin package. During development, usually
you'd want to install with something like:

```
pip install --editable 'path/to/package/'
```

where `path/to/package/` is the folder where your plugin's
`setup.py`/`setup.cfg` is found.

This installs your plugin as an [editable
package](https://pip.pypa.io/en/stable/cli/pip_install/#install-editable),
which is suitable during development.

pylsp uses [pluggy](https://pluggy.readthedocs.io/en/stable/) for
plugin management. It would be helpful to be familiar and read through pluggy
documentation, but we'll go through a quick rundown here.

pylsp plugin is composed of a set of callbacks that are registered using
`@hookimpl` decorator:

```
from pylsp import hookimpl, uris, _utils

@hookimpl
def pylsp_definitions(config, workspace, document, position):
    logger.info('Retrieving definitions: %s %s %s %s', config, workspace, document, position)
    filename = __file__
    uri = uris.uri_with(document.uri, path=filename)
    with open(filename) as f:
        lines = f.readlines()
        for lineno, line in enumerate(lines):
            if 'def pylsp_definitions' in line:
                break
    return [
        {
            'uri': uri,
            'range': {
                'start': {
                    'line': lineno,
                    'character': 4,
                },
                'end': {
                    'line': lineno,
                    'character': line.find(')') + 1,
                },
            }
        }
    ]
```

Refer to [list of hookspecs](https://github.com/python-lsp/python-lsp-server/blob/develop/pylsp/hookspecs.py)
for the full list of all supported hooks.

And that's all you need to make a pylsp plugin. Once you have your entrypoint
configured and register some `@hookimpl`, pylsp will call your callbacks to
perform its functions.

What comes next, is that you'll want to publish your package in a repository
like Github and in PyPI so your package can be easily used and discovered by
your users. You can use any way to publish your plugin package, but this
cookiecutter will set you up to publish to PyPI using `twine`.
