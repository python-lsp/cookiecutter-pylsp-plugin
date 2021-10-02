from unittest.mock import ANY

from pylsp_{{ cookiecutter.plugin_name }} import plugin
from test.conftest import *


def test_definitions(config, workspace, document):
    position = {"line": 3, "character": 6}

    response = plugin.pylsp_definitions(
        config=config,
        workspace=workspace,
        document=document,
        position=position,
    )

    expected = [
        {
            "uri": ANY,
            "range": {
                "start": {
                    "line": ANY,
                    "character": ANY,
                },
                "end": {
                    "line": ANY,
                    "character": ANY,
                },
            },
        },
    ]

    assert response == expected


def test_code_action(config, workspace, document, code_action_context):
    selection = {
        "start": {
            "line": 3,
            "character": 0,
        },
        "end": {
            "line": 4,
            "character": 0,
        },
    },

    response = plugin.pylsp_code_actions(
        config=config,
        workspace=workspace,
        document=document,
        range=selection,
        context=code_action_context,
    )

    expected = [
        {
            'title': 'Extract method',
            'kind': 'refactor.extract',
            'command': 'foobar-1',
            'arguments': ['hello', 'world'],
        }
    ]

    assert response == expected
