import sys
import os
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from PySide2.QtGui import QIcon
from bs4 import BeautifulSoup

app = QApplication(sys.argv)
web = QWebEngineView()

script_dir = os.path.dirname(os.path.abspath(__file__))
file = os.path.join(script_dir, 'index.html')
icon = os.path.join(script_dir, 'icon.png')

web.load(QUrl.fromLocalFile(file))

html_file_path = os.path.join(script_dir, 'index.html')
with open(html_file_path, 'r') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    title = soup.title.text
web.setWindowTitle(str(title))
web.setWindowIcon(QIcon(icon))
web.show()

sys.exit(app.exec_())
