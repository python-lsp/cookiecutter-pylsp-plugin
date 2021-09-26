from unittest.mock import ANY

from pylsp_{{ cookiecutter.plugin_name }} import plugin
import test.conftest


def test_definitions(config, workspace, document):
    position = {"line": 3, "character": 6}
    resp = plugin.pylsp_definitions(config, workspace, document, position)
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

    assert resp == expected
