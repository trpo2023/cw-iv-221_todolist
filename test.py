import pytest

from PyQt5 import QtCore, QtWidgets, QtGui
from pytestqt.qt_compat import qt_api

import main


@pytest.fixture
def app(qtbot):
    test_hello_app = main.MainWindow()
    qtbot.addWidget(test_hello_app)

    return test_hello_app


def test_label(app):
    assert app.windowTitle() == "Планировщик задач"

def test_buttonlable(app):
    assert app.add_button.text() == "Добавить пункт"

def test_add_button_creates_line_edit(app):
    # Нажимаем на кнопку добавления
    app.add_button.click()

    # Получаем виджет, связанный с добавленным элементом
    widget = app.others_commands_widget.itemWidget(app.others_commands_widget.item(0))

    # Проверяем, что в виджете создан QLineEdit
    assert isinstance(widget.le, QtWidgets.QLineEdit)

def test_delete_button(app, qtbot):
    app.add_button.click()
    widget = app.others_commands_widget.itemWidget(app.others_commands_widget.item(0))
    # Нажимаем на кнопку удаления в виджете
    qtbot.mouseClick(widget.delete_button, QtCore.Qt.LeftButton)
    # Проверяем, что элемент был удален
    assert app.others_commands_widget.count() == 0
    
def test_delete_butto(app, qtbot):
    app.add_button.click()
    widget = app.others_commands_widget.itemWidget(app.others_commands_widget.item(0))
    qtbot.mouseClick(widget.delete_butto, QtCore.Qt.LeftButton)
    assert app.others_commands_widget.count() == 0
