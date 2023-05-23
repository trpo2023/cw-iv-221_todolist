
import pytest

from PyQt5 import QtCore

import main


@pytest.fixture
def app(qtbot):
    test_hello_app = main.MainWindow()
    qtbot.addWidget(test_hello_app)

    return test_hello_app


def test_label(app):
    assert app.windowTitle() == "Планировщик задач"

