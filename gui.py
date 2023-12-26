import sys

from PyQt5.QtGui import QPainter, QPen

from plane import *

from PyQt5.QtCore import QSize, Qt

from PyQt5.QtWidgets import (QMainWindow,
                            QPushButton,
                            QLabel,
                            QLineEdit,
                            QVBoxLayout,
                            QWidget

)

from PyQt5.uic import loadUi

from main_window_ui import Ui_MainWindow


class AboutWindow(QMainWindow):
    """Class for the About section window
    doesnt have much
    """
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: white;")
        self.setWindowTitle("About.")

        self.setFixedSize(QSize(400, 320))

        self.info = QLabel()

        self.info.setText(
            "This is a program made for a plane simulation."
            "\nTo use it: "
            "\nChoose an option."
            "\nAnd press the button to do things"
            "\nCheck button."
            "\nEnjoy!")
        layout = QVBoxLayout()

        layout.addWidget(self.info,0,Qt.AlignmentFlag.AlignTop|Qt.AlignmentFlag.AlignHCenter)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

def start_about():
    """Function used for staring the about
    window in a way that saves it from the GC
    I think it is needed for the about window
    """
    about = AboutWindow()
    return about

class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.plane = Plane()
        self.setupUi(self)

        self.about.show()

        self.comboBox.hide()
        self.inputs = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4]
        self.buttons = [self.radioButton,
                        self.radioButton_2,
                        self.radioButton_3]
        self.hide_input()
        self.label.hide()
        button_text = ["Add shape", "Remove shape","See shapes"]

        for number, button in enumerate(self.buttons):
            button.setText(button_text[number])
            button.toggled.connect(self.on_clicked_radio)

        self.about.pressed.connect(self.show_about)

    def hide_input(self):
        for i in self.inputs:
            i.hide()
        self.label_2.hide()

    def show_input(self):
        for i in self.inputs:
            i.show()
        self.label_2.show()

    def remove_combo_item(self, index):
        self.plane.remove_shape(index)
        self.comboBox.removeItem(index)


    def see_shapes(self):
        self.label.setText(self.plane.__str__())
        self.label.adjustSize()
        self.label.show()

    def add_shapes(self):
        print(self.comboBox.currentText())
        if self.comboBox.currentText() == "Rectangle":
            data = [i.text() for i in self.inputs]
        else:
            data = [self.lineEdit_3.text(), self.lineEdit_4.text()]
        data = [[j for j in i.split()] for i in data]
        if self.comboBox.currentText() == "Rectangle":
            self.plane.add_shape('2', data)
        else:
            self.plane.add_shape('1', data)


    def remove_shapes(self):

        if self.comboBox.currentIndex() == -1:
            return -1
        self.comboBox.currentIndexChanged.connect(self.plane.remove_shape)


    def input_choices(self, stuff):
        for i in self.inputs:
            i.clear()
        if stuff == "Rectangle":
            self.show_input()
        else:
            self.hide_input()
            self.lineEdit.show()
            self.lineEdit_2.show()
            self.label_2.show()

    def on_clicked_radio(self):
        rbutton = self.sender()
        if rbutton.isChecked():
            try:
                self.pushButton.pressed.disconnect()
            except Exception:
                pass
            match(rbutton.text()):
                case "Add shape":
                    self.comboBox.clear()
                    self.pushButton.pressed.connect(self.add_shapes)
                    self.label.setText("To add a new shape: Input the vertices into the fields below and press the add button.")
                    self.label.adjustSize()
                    self.label.show()
                    self.show_input()
                    self.comboBox.addItems(["Rectangle", "Circle"])
                    self.comboBox.show()
                    self.pushButton.setText("Add shape")
                    self.comboBox.currentTextChanged.connect(self.input_choices)

                case "Remove shape":
                    self.pushButton.pressed.connect(self.remove_shapes)
                    self.comboBox.clear()
                    self.comboBox.show()
                    self.comboBox.addItems([shape.__str__() for shape in self.plane.stuff])
                    self.pushButton.setText("Remove shape")
                    self.label.setText("Choose a shape from the dropdown menu and press the remove button.")
                    self.label.adjustSize()
                    self.label.show()
                    self.hide_input()

                case "See shapes":
                    self.pushButton.pressed.connect(self.see_shapes)
                    self.comboBox.hide()
                    self.hide_input()
                    self.pushButton.setText("See shapes")
                    self.label.clear()

                case _:
                    self.comboBox.hide()
                    self.label.hide()
                    self.hide_input()

    def show_about(self):
        """Function used for getting the
             about window up and running
             very important!
             """
        self.about_wnd = start_about()
        self.about_wnd.show()

class DrawWidget(QWidget):
    def __init__(self):
        super().__init__()
        painter = QPainter(self)
        painter.drawLine(1,1,200,200)
        self.show()
