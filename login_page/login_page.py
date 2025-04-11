import os
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import QEvent, Qt, QObject
from functools import partial
from login_page.query import auth, get_id_user, get_role, get_id_operation, log_in_session


class EnterEventFilter(QObject):
    def __init__(self, parent, ui):
        super().__init__()
        self.parent = parent
        self.ui = ui

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and event.key() in (Qt.Key_Return, Qt.Key_Enter):
            handle_login(self.parent, self.ui)
            return True  # Event sudah ditangani
        return False  # Lanjutkan event seperti biasa


def login_page(self):
    loader = QUiLoader()
    ui_path = os.path.join(os.path.dirname(__file__), "login_page.ui")
    ui = loader.load(ui_path)
    stack_widget = self.central_widget
    stack_widget.addWidget(ui)
    stack_widget.setCurrentWidget(ui)

    loginButton = ui.findChild(QPushButton, 'loginButton')
    loginButton.clicked.connect(partial(handle_login, self, ui))

    # Pasang event filter ke input username dan password
    usernameInput = ui.findChild(QLineEdit, 'usernameInput')
    passwordInput = ui.findChild(QLineEdit, 'passwordInput')

    self.enter_filter = EnterEventFilter(self, ui)  # Disimpan agar tidak garbage collected
    usernameInput.installEventFilter(self.enter_filter)
    passwordInput.installEventFilter(self.enter_filter)


def handle_login(self, ui):
    from menu_page.menu_page import menu_page
    self.username = ui.findChild(QLineEdit, 'usernameInput').text()
    self.password = ui.findChild(QLineEdit, 'passwordInput').text()
    username = self.username
    password = self.password
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Warning)
    msg_box.setWindowTitle("Login Gagal")
    msg_box.setStyleSheet("QLabel{ color: white; } QMessageBox { background-color: black; }")
    if username and len(username) >= 8:
        if password and len(password) >= 8:
            auth_ = auth(username, password)
            if auth_ is True:
                self.id_user = get_id_user(username)
                id_user = self.id_user
                self.role = get_role(id_user)
                log_in_session(id_user)
                self.id_operation = get_id_operation(id_user)
                menu_page(self)
            else:
                msg_box.setText("Please enter a correct username and password")
                msg_box.exec()
        else:
            msg_box.setText("Please enter a valid password")
            msg_box.exec()
    else:
        msg_box.setText("Please enter a valid username")
        msg_box.exec()
