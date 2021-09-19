import logging

from pylsp import hookimpl


logger = logging.getLogger(__name__)


@hookimpl
def pylsp_settings():
    logger.info('Initializing pylsp_{{cookiecutter.plugin_name}}')

    # Disable default plugins that conflicts with our plugin
    return {
        'plugins': {
            # 'autopep8_format': {'enabled': False},
            # 'definition': {'enabled': False},
            # 'flake8_lint': {'enabled': False},
            # 'folding': {'enabled': False},
            # 'highlight': {'enabled': False},
            # 'hover': {'enabled': False},
            # 'jedi_completion': {'enabled': False},
            # 'jedi_rename': {'enabled': False},
            # 'mccabe_lint': {'enabled': False},
            # 'preload_imports': {'enabled': False},
            # 'pycodestyle_lint': {'enabled': False},
            # 'pydocstyle_lint': {'enabled': False},
            # 'pyflakes_lint': {'enabled': False},
            # 'pylint_lint': {'enabled': False},
            # 'references': {'enabled': False},
            # 'rope_completion': {'enabled': False},
            # 'rope_rename': {'enabled': False},
            # 'signature': {'enabled': False},
            # 'symbols': {'enabled': False},
            # 'yapf_format': {'enabled': False},
        },
    }
