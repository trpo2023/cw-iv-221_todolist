import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def Add_OtherItem():
    ItemOther = CustomItem()
    ItemOther.SetupItem(OthersCommandsWidget)


def ReadText_fn():
    for index in range(0, OthersCommandsWidget.count()):
        TargetItem = (
            OthersCommandsWidget.itemWidget(OthersCommandsWidget.item(index))
            .children()[1]
            .text()
        )
        print(TargetItem)

    def delete(self):
        widget = self.sender()
        gp = widget.mapToGlobal(QtCore.QPoint())
        lp = self.others_commands_widget.viewport().mapFromGlobal(gp)
        row = self.others_commands_widget.row(self.others_commands_widget.itemAt(lp))
        t_it = self.others_commands_widget.takeItem(row)
        shost = self.text()
        f = open("история.txt", "a")
        f.write(shost + "\n" + time + " пункт выполнен." + "\n")
        f.close()
        del t_it


app = QtWidgets.QApplication(sys.argv)


class CustomItem(object):
    def SetupItem(self, OthersCommandList):
        self.Item = QtWidgets.QListWidgetItem()
        self.Item.setStatusTip("TItem")

        self.MainWidget = QtWidgets.QWidget()

        self.CommandLine = QtWidgets.QLineEdit("")

        self.DeleteButton = QtWidgets.QPushButton("x")
        self.DeleteButton.setFixedSize(22, 22)

        self.ItemLayoutBox = QtWidgets.QHBoxLayout()

        self.ItemLayoutBox.addWidget(self.CommandLine)
        self.ItemLayoutBox.addWidget(self.DeleteButton)

        self.MainWidget.setLayout(self.ItemLayoutBox)

        self.Item.setSizeHint(self.MainWidget.sizeHint())

        OthersCommandList.addItem(self.Item)
        OthersCommandList.setItemWidget(self.Item, self.MainWidget)


if __name__ == "__main__":
    AppWindow = QtWidgets.QMainWindow()
    AppWindow.setWindowTitle("PoC ListWidget")
    AppWindow.setFixedSize(550, 550)

    TabWindow = QtWidgets.QTabWidget(AppWindow)
    TabWindow.setGeometry(8, 10, 535, 505)

    WorkTAB = QtWidgets.QWidget()
    TabWindow.addTab(WorkTAB, "Tab.01")

    OthersCommandsWidget = QtWidgets.QListWidget(WorkTAB)
    OthersCommandsWidget.setGeometry(QtCore.QRect(8, 40, 515, 430))

    AddButton = QtWidgets.QPushButton(WorkTAB)
    AddButton.setText("Add Item")
    AddButton.setGeometry(QtCore.QRect(8, 8, 0, 0))
    AddButton.setFixedSize(70, 22)

    AddButton.clicked.connect(Add_OtherItem)

    AppWindow.show()
    sys.exit(app.exec_())
