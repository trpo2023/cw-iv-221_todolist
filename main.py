import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton, QLineEdit
from datetime import datetime


class Widget(QtWidgets.QWidget):
    clicked = QtCore.pyqtSignal()
    clicke = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.le = QLineEdit()
        self.delete_button = QPushButton("✓")
        self.delete_butto = QPushButton("X")
        hlay = QtWidgets.QHBoxLayout(self)
        hlay.addWidget(self.le)
        hlay.addWidget(self.delete_button)
        hlay.addWidget(self.delete_butto)
        self.delete_button.clicked.connect(self.clicked)
        self.delete_butto.clicked.connect(self.clicke)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.resize(1000, 400)
        self.setWindowTitle("Планировщик задач")

        self.tab_widget = QtWidgets.QTabWidget()
        self.work_tab = QtWidgets.QWidget()
        self.tab_widget.addTab(self.work_tab, "")
        self.others_commands_widget = QtWidgets.QListWidget()

        vlay = QtWidgets.QVBoxLayout(self.work_tab)
        hlay = QtWidgets.QHBoxLayout()
        self.add_button = QtWidgets.QPushButton("Добавить пункт")
        self.add_butto = QtWidgets.QPushButton("В невыполенное.txt")
        self.add_butto.clicked.connect(self.ReadText_fn)
        self.add_button.clicked.connect(self.add)
        hlay.addWidget(self.add_button)
        hlay.addWidget(self.add_butto)
        vlay.addLayout(hlay)
        vlay.addWidget(self.others_commands_widget)

        self.setCentralWidget(self.tab_widget)

    def add(self):
        it = QtWidgets.QListWidgetItem()
        self.others_commands_widget.addItem(it)
        widget = Widget()
        widget.clicked.connect(self.delete)
        widget.clicke.connect(self.delete1)
        self.others_commands_widget.setItemWidget(it, widget)
        it.setSizeHint(widget.sizeHint())

    def delete(self):
        widget = self.sender()
        gp = widget.mapToGlobal(QtCore.QPoint())
        lp = self.others_commands_widget.viewport().mapFromGlobal(gp)
        row = self.others_commands_widget.row(self.others_commands_widget.itemAt(lp))
        t_it = self.others_commands_widget.takeItem(row)
        f = open("история.txt", "a")
        f.write(
            datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M")
            + "\n"
            + widget.le.text()
            + ": Сделано"
            + "\n"
        )
        f.close()
        del t_it

    def delete1(self):
        widget = self.sender()
        gp = widget.mapToGlobal(QtCore.QPoint())
        lp = self.others_commands_widget.viewport().mapFromGlobal(gp)
        row = self.others_commands_widget.row(self.others_commands_widget.itemAt(lp))
        t_it = self.others_commands_widget.takeItem(row)
        del t_it

    def ReadText_fn(self):
        for index in range(0, self.others_commands_widget.count()):
            TargetItem = (
                self.others_commands_widget.itemWidget(
                    self.others_commands_widget.item(index)
                )
                .children()[1]
                .text()
            )
            print(TargetItem)
            f = open("невыполенное.txt", "a")
            f.write(
                " Не выполнено за "
                + datetime.strftime(datetime.now(), "%d.%m.%Y")
                + ":\n"
                + TargetItem
                + "\n"
            )
            f.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
