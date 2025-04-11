from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        from login_page.login_page import login_page
        super().__init__()
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget) 

        # Tambahkan halaman login
        login_page(self)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.showMaximized() 
    app.exec()
