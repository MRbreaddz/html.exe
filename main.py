import sys
import os
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from PySide2.QtGui import QIcon
from bs4 import BeautifulSoup
import tempfile
import glob
import shutil
import atexit
import getpass

html_file_contents = ''
javascript_file_contents = ''
css_file_contents = ''


html_file_contents = html_file_contents.encode()
with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp_file:
    temp_file.write(html_file_contents)
    html_temp_file_name = temp_file.name

files_type_list = ["*.png","*.jpeg","*.mp3","*.mp4","*.ico","*.webp","*.svg"]

for i in files_type_list:
    files = []
    files = glob.glob("_internal/*"+str(i))
    for a in files:
        shutil.copy(a, r"C:\Users\%s\AppData\Local\Temp" % getpass.getuser())
    files = []



app = QApplication(sys.argv)
web = QWebEngineView()

script_dir = os.path.dirname(os.path.abspath(__file__))
icon = os.path.join(script_dir, 'icon.png')


with open(html_temp_file_name, 'r',encoding='utf-8') as html_file:
    soup = BeautifulSoup(html_file, 'html.parser')
    js_tag = soup.new_tag("script")
    css_tag = soup.new_tag("style")
    js_tag.string = javascript_file_contents
    css_tag.string = css_file_contents
    soup.head.append(css_tag)
    soup.body.append(js_tag)
    title = soup.title
    if title:
        title = BeautifulSoup(title.text, 'html.parser')
        title_content = soup.get_text()
        web.setWindowTitle(str(title_content))
    with open(html_temp_file_name, 'w', encoding='utf-8') as file:
        file.write(str(soup))
web.load(QUrl.fromLocalFile(html_temp_file_name))
web.setWindowTitle(str(title))
web.setWindowIcon(QIcon(icon))
web.show()

def exit_handler():
    for i in files_type_list:
        files = []
        files = glob.glob("_internal/*"+str(i))
        for a in files:
            os.remove(r"C:\Users\%s\AppData\Local\Temp/" % getpass.getuser()+str(os.path.basename(a)))
        files = []

    os.remove(html_temp_file_name)

atexit.register(exit_handler)

sys.exit(app.exec_())