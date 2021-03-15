import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, \
    QPushButton, QMainWindow, QGridLayout


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count_of_buttons = 1
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.setGeometry(700, 200, 500, 400)

        self.button_add = QPushButton('Add')
        self.button_add.clicked.connect(self.add_button)

        self.button_clear = QPushButton('Clear')  # +++
        self.button_clear.clicked.connect(self.clear_button)  # +++

        self.layout_buttons = QVBoxLayout()
        self.layout_buttons.addStretch()

        self.frame = QFrame()
        self.frame.setMinimumSize(200, 200)
        self.frame.setFrameStyle(QFrame.Box)
        self.frame.setLayout(self.layout_buttons)

        self.main_layout = QGridLayout(self.centralWidget)  # QGridLayout
        self.main_layout.addWidget(self.button_add, 0, 0)
        self.main_layout.addWidget(self.button_clear, 0, 1)  # +++
        self.main_layout.addWidget(self.frame, 1, 0, 1, 2)  # +++

    def add_button(self):
        # -       self.main_layout.addWidget(self.frame)
        self.button = QPushButton(f"Кнопка № {self.count_of_buttons}")
        self.button.clicked.connect(lambda ch, btn=self.button: self.pressed_btn(btn))
        self.count_of_buttons += 1
        self.layout_buttons.insertWidget(0, self.button)

    def pressed_btn(self, btn):
        print(f"кнопка нажата: {btn.text()}")

    # +++ vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    def clear_button(self):
        widgets = self.frame.layout().count()
        if widgets > 1:
            for i in range(widgets - 1):
                widget = self.frame.layout().itemAt(0).widget()
                self.frame.layout().removeWidget(widget)
                widget.hide()
            # +++ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.exit(app.exec_())