import shutil
import glob
import os
from PyInstaller.__main__ import run

with open("main.py", 'w') as file:
    file.writelines("""import sys
import os
from PySide2.QtWidgets import QApplication
from PySide2.QtWebEngineWidgets import QWebEngineView
from PySide2.QtCore import QUrl
from PySide2.QtGui import QIcon
from bs4 import BeautifulSoup
import tempfile

html_file_contents = ''
javascript_file_contents = ''
css_file_contents = ''


html_file_contents = html_file_contents.encode()
with tempfile.NamedTemporaryFile(suffix='.html', delete=False) as temp_file:
    temp_file.write(html_file_contents)
    html_temp_file_name = temp_file.name


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

sys.exit(app.exec_())
""")

html_file_contents = ''
javascript_file_contents = ''
css_file_contents = ''

with open("index.html", 'r') as file:
    html_file_contents = file.read()



js_files = glob.glob("*.js")
for i in js_files:
    with open(i, 'r',encoding='utf-8') as file:
        javascript_file_contents += file.read()

        

css_files = glob.glob("*.css")
for i in css_files:
    with open(i, 'r',encoding='utf-8') as file:
        css_file_contents += file.read()



modified_lines = []

with open("main.py", 'r') as file:
    for line in file:
        if "html_file_contents = ''" in line:
            line = line.replace("html_file_contents = ''", f"html_file_contents = '''{html_file_contents}'''")
        if "javascript_file_contents = ''" in line:
            line = line.replace("javascript_file_contents = ''", f"javascript_file_contents = '''{javascript_file_contents}'''")
        if "css_file_contents = ''" in line:
            line = line.replace("css_file_contents = ''", f"css_file_contents = '''{css_file_contents}'''")
        modified_lines.append(line)

with open("main.py", 'w',encoding='utf-8') as file:
    file.writelines(modified_lines)

if __name__ == '__main__':
    opts = ['main.py','-w','--icon=icon.png']
    run(opts)

icon = 'icon.png'
folder = 'dist/main/_internal'

shutil.copy(icon, folder)

png_files = glob.glob("*.png")
for i in png_files:
    shutil.copy(i, folder)

shutil.rmtree("build")
os.remove("main.spec")

print("Exporting done")
input("Press any button to exit")
