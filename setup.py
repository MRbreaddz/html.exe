import shutil
import glob
import os
from PyInstaller.__main__ import run

if __name__ == '__main__':
    opts = ['main.py','-w','--icon=icon.png']
    run(opts)

file = 'index.html'
icon = 'icon.png'
folder = 'dist/main/_internal'

shutil.copy(file, folder)
shutil.copy(icon, folder)

js_files = glob.glob("*.js")
for i in js_files:
    shutil.copy(i, folder)

css_files = glob.glob("*.css")
for i in css_files:
    shutil.copy(i, folder)

html_files = glob.glob("*.html")
for i in html_files:
    shutil.copy(i, folder)

png_files = glob.glob("*.png")
for i in png_files:
    shutil.copy(i, folder)

shutil.rmtree("build")
os.remove("main.spec")

print("Exporting done")
input("Press any button to exit")
