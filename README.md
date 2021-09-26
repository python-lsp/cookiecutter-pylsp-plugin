# cookiecutter-pylsp-plugin

Using cookiecutter-pylsp-plugin is the easiest way to start writing pylsp
plugin. This repo also aims to document how python-lsp-plugins plugins are
wired if you want to do-it-yourself instead of using the template.

## Features

- License selection

## Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

```
pip install -U cookiecutter
```

Generate a Python package project:

```
cookiecutter https://github.com/lieryan/cookiecutter-pylsp-plugin
```


## pylsp plugin developer documentation

The following section will help you understand how pylsp plugin is wired to the
pylsp, which will help you make changes to the base setup when using this
template or to do what this template does yourself.

On startup, pylsp will automatically discover plugins by querying
`pkg_resources` for package entrypoints. So that your plugin can be discovered
by pylsp, you must configure the following in the setup.py/setup.cfg of your
plugin's package:

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

where `path/to/package/` is the folder where your plugin's setup.py/setup.cfg
is found.

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

Refer the [list of hookspecs](https://github.com/python-lsp/python-lsp-server/blob/develop/pylsp/hookspecs.py).

And that's all you need to make a pylsp plugin. Once you have your entrypoint
configured and register some `@hookimpl`, pylsp will call your callbacks to
perform its functions.

What comes next, is that you'll want to publish your package in a repository
like Github and in PyPI so your package can be easily used and discovered by
your users. You can use any way to publish your plugin package, but this
cookiecutter will set you up to publish to PyPI using `twine`.
