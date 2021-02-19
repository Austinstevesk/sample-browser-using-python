import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self ).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        #Navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        #back button
        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)
        #forward
        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        #refresh
        refresh_btn = QAction('Reload', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)
        #Home
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        #Url Bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))





app = QApplication(sys.argv)
QApplication.setApplicationName("Austin's browser")
window = MainWindow()
app.exec_()