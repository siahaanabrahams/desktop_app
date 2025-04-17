from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QPushButton, QLineEdit, QComboBox, QMessageBox
import os
from functools import partial
from general_function.handle_logout import handle_logout
from general_function.move_page import move_page
from admin_page.move_menu import move_menu
from admin_page.query import check_password, change_password_que

def change_password(self):
    loader = QUiLoader()
    ui_path = os.path.join(os.path.dirname(__file__), "change_password.ui")
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
    
    createButton = ui.findChild(QPushButton, 'changeButton')
    createButton.clicked.connect(partial(change, self, ui))  

def change(self,ui) :
    username = self.username
    oldPasswordInput = ui.findChild(QLineEdit, 'oldPasswordInput').text()
    newPasswordInput = ui.findChild(QLineEdit, 'newPasswordInput').text()
    validation = check_password(username, oldPasswordInput) 
    if validation == False : 
        QMessageBox.warning(ui, "Fail", "Old password is wrong") 
    else : 
        change_password_que(username, newPasswordInput)
        QMessageBox.information(ui, "Success", "Change password success.")
