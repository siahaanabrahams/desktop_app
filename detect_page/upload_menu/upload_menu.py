from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QPushButton, QLabel, QComboBox, QLineEdit, QMessageBox
import os
from functools import partial
from general_function.handle_logout import handle_logout
from general_function.move_page import move_page
from detect_page.move_menu import move_menu 

def upload_menu(self):
    loader = QUiLoader()
    ui_path = os.path.join(os.path.dirname(__file__), "upload_menu.ui")
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