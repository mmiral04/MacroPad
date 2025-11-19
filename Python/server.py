import socket
from pynput.keyboard import Key, Controller

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from MainWindowUI import Ui_MainWindow

import threading
import subprocess
import os
import multiprocessing

import json

HOST = "192.168.1.148"
PORT = 12345


keyboard = Controller()
config_file = r"E:/GitHub/Proyects/MacroPad/MacroPad/Python/config.json"
mapping = {}

def load_config():
    with open(config_file) as f:
        data = json.load(f)
        for key in data:
            if data[key][0] == 1: # Key sequence
                mapping[key] = (1, data[key][1])
            else: # Application
                mapping[key] = (2, data[key][1], data[key][2])


def special_keys(key):
    if key == "Ctrl":
        return Key.ctrl
    elif key == "Alt":
        return Key.alt
    elif key == "Backspace":
        return Key.backspace
    elif key == "Cmd":
        return Key.cmd
    elif key == "Del":
        return Key.delete
    elif key == "Esc":
        return Key.esc
    elif key == "Return":
        return Key.enter
    elif key == "Shift":
        return Key.shift
    elif key == "Space":
        return Key.space
    elif key == "Tab":
        return Key.tab
    else:
        return key.lower()
    

def parse_key_combo(keys):
    keys = keys.split(",")
    for k in keys:
        _k = k.strip().split("+")
        for j in _k:
            keyboard.press(special_keys(j))
        _k.reverse()
        for j in _k:
            keyboard.release(special_keys(j))

def execute(path):
    proc = multiprocessing.Process(target= subprocess.call, args=(path,))
    proc.start()

connected_socket = None
connection = None

def open_socket(outputLog):
    outputLog("Connecting to device...")
    global connected_socket
    global connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        connected_socket = s
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        connection = conn
        with conn:
            outputLog(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    if data == b"disconnected":
                        outputLog(f"Disconnected")
                        break
                    else:
                        data = data.decode("utf-8")
                        if mapping[data][0] == 1: # key sequence
                            parse_key_combo(mapping[data][1])
                        else: # application
                            execute(mapping[data][1])
                except KeyError:
                    pass


## GUI code
open_thread = None
logger = None

def connect():
    global open_thread
    global logger
    open_thread = threading.Thread(target=open_socket, args=(logger, ))
    open_thread.daemon = True
    open_thread.start()

def disconnect():
    logger("Disconnected")    
    connection.send(b"Disconnected")
    connected_socket.close()
    #connected_socket = None

class MainWindow(QMainWindow):
    def __init__(self):
        global logger
        global open_thread

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow(mapping)
        self.ui.setupUi(self)
        logger = self.ui.getLogger()

        open_thread = threading.Thread(target = open_socket, args=(logger,))
        open_thread.daemon = True
        self.ui.setConnect(connect)
        self.ui.setDisconnect(disconnect)
        self.ui.pushButton_12.clicked.connect(self.updateConfig)
        open_thread.start()
    
    def updateConfig(self):
        global config_file
        res = self.ui.openSettings(config_file)
        if res:
            config_file = res

if __name__ == "__main__":
    load_config()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    load_config()

#os.startfile(r"C:\Program Files\WindowsApps\SpotifyAB.SpotifyMusic_1.267.560.0_x64__zpdnekdrzrea0\Spotify.exe")
