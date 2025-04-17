from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QPushButton, QLabel, QComboBox, QLineEdit, QMessageBox
import os
from functools import partial
from general_function.handle_logout import handle_logout
from general_function.move_page import move_page
from admin_page.move_menu import move_menu
from admin_page.query import find_username

def delete_user(self):
    loader = QUiLoader()
    ui_path = os.path.join(os.path.dirname(__file__), "delete_user.ui")
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

    searchButton = ui.findChild(QPushButton, 'searchButton')
    searchButton.clicked.connect(partial(find_user, ui))

    username_select = ui.findChild(QComboBox, 'usernameList').currentText()
    print(username_select)

def find_user(ui) :
    username = ui.findChild(QLineEdit, 'usernameInput').text()
    list_username = find_username(username)
    username_list_widget = ui.findChild(QComboBox, 'usernameList')
    username_list_widget.clear() 
    if list_username : 
        usernames = [user[0] for user in list_username]
        username_list_widget.addItems(usernames)
    else :
        QMessageBox.warning(ui, "Fail", "Username not found.") 