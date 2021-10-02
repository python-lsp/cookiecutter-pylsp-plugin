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
