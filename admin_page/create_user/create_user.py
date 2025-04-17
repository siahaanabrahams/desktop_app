from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QPushButton, QLineEdit, QComboBox, QMessageBox
import os, re
from functools import partial
from general_function.handle_logout import handle_logout
from general_function.move_page import move_page
from admin_page.move_menu import move_menu
from admin_page.query import create_new_user, check_username

def create_user(self):
    loader = QUiLoader()
    ui_path = os.path.join(os.path.dirname(__file__), "create_user.ui")
    ui = loader.load(ui_path)
    stack_widget = self.central_widget
    stack_widget.addWidget(ui)
    stack_widget.setCurrentWidget(ui)  
    
    page_select = ui.findChild(QComboBox, 'comboBox')
    page_select.currentIndexChanged.connect(partial(move_page, self, page_select))

    menu_select = ui.findChild(QComboBox, 'menu')
    menu_select.currentIndexChanged.connect(partial(move_menu, self, menu_select))

    logoutButton = ui.findChild(QPushButton, 'logoutButton')
    logoutButton.clicked.connect(partial(handle_logout, self))  

    createButton = ui.findChild(QPushButton, 'createButton')
    createButton.clicked.connect(partial(create, ui))  

def create(ui) : 
    username = ui.findChild(QLineEdit, 'usernameInput').text()
    password = ui.findChild(QLineEdit, 'passwordInput').text()
    role = ui.findChild(QComboBox, 'roleInput').currentText()
    if username and len(username) >= 8:
        if password and len(password) >= 8 and re.search(r'\d', password):
            check_user = check_username(username) 
            if check_user is not True : 
                create_new_user(username, password, role)
                QMessageBox.information(ui, "Success", "User created.")
            else : 
                QMessageBox.warning(ui, "Fail", "Username existed.")
        else:
            QMessageBox.warning(ui, "Fail", "Password must be at least 8 characters long and contain at least one number.") 
    else:
        QMessageBox.warning(ui, "Fail", "Username must be at least 8 characters long.") 