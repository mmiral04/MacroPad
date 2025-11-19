from PIL import Image, ImageDraw

# connection
import socket
import bluetooth
import time

# GUI
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSystemTrayIcon, QMenu
from PySide6.QtCore import QFile
from PySide6.QtGui import QIcon, QAction
from MainWindowUI import Ui_MainWindow

# Macros
from pynput.keyboard import Key, Controller, KeyCode
import threading
import subprocess
import multiprocessing
import os
import json

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image


TARGET_NAME = "MacroPad"
TARGET_ADDRESS = "10:06:1C:41:81:26"

keyboard = Controller()

config_file = r"config.json"


mapping = {}

open_thread = None
logger = None
connected_socket = None

closeFlag = False
def connectionProtocol(s):
    s.send(b"begin connection")
    try:
        data = s.recv(1024)
    except ConnectionAbortedError:
        return False
    if data == b"accept connection":
        print("Connection established")
        return True
    return False

def getTargetAddress():
    global TARGET_ADDRESS

    nearby_devices = bluetooth.discover_devices(lookup_names=True,lookup_class=True)
    print(nearby_devices)
    for btaddr, btname, btclass in nearby_devices:
        if TARGET_NAME == btname:
            TARGET_ADDRESS = btaddr
            break

def load_config():
    with open(config_file) as f:
        data = json.load(f)
        for key in data:
            mapping[key] = data[key]


def save_config():
    with open(config_file, "w") as f:
        json.dump(mapping, f)

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
    elif len(key) == 1:
        return key.lower()
    elif "0x" in key:
        return KeyCode.from_vk(int(key, 16))
    else:
        raise ValueError
    
def parse_key_combo(keys):
    keys = keys.split(",")
    parsed_keys = []
    try:
        for k in keys:
            _k = k.strip().split("+")
            for j in _k:
                parsed_keys.append(special_keys(j.strip()))
    except ValueError:
        return
    
    for k in parsed_keys:
        keyboard.press(k)
    for k in parsed_keys[::-1]:
        keyboard.release(k)

def execute(path):
    proc = threading.Thread(target= subprocess.run, args=(path,))
    proc.start()

def executeScript(path):
    thrd = threading.Thread(target = subprocess.run, args = (["python", path],), daemon=True)
    thrd.start()

def connection(logger):
    global connected_socket

    if TARGET_ADDRESS is not None:
        logger("Connecting to {} at {}...".format(TARGET_NAME, TARGET_ADDRESS))
        port = 1
        s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        
        isConnected = False
        tries = 0
        while not isConnected and tries < 3:
            try:
                s.connect((TARGET_ADDRESS, port))
                isConnected = True
            except TimeoutError:
                logger("[ERROR]: Timeout ocurred, retrying...")
                tries += 1

        if not isConnected:
            logger("[ERROR]: Connection failed")
            return
        
        connected_socket = s
        logger("Connected to {}".format(TARGET_NAME))
        res = connectionProtocol(s)
        while res:
            try:
                data = s.recv(1024)
            except (ConnectionAbortedError, OSError):
                break
            if not data:
                break
            try:
                if data == b"disconnect":
                    logger("Disconnected")
                    connected_socket.shutdown(socket.SHUT_RDWR)
                    connected_socket.close()
                    break
                else:
                    data = data.decode("utf-8")
                    if mapping[data]["type"] == 1:
                        parse_key_combo(mapping[data]["shortcut"])
                    elif mapping[data]["type"] == 2:
                        execute(mapping[data]["app"])
                    else:
                        executeScript(mapping[data]["app"])
            except KeyError:
                pass

    else:
        logger("[ERROR] Invalid target address")

def connect():
    global open_thread
    global logger
    open_thread = threading.Thread(target = connection, args = (logger, ))
    open_thread.daemon = True
    open_thread.start()

def disconnect():
    if connected_socket != None:
        logger("Disconnecting...")
        try:
            connected_socket.send(b"disconnected")
            time.sleep(1)
            connected_socket.shutdown(socket.SHUT_RDWR)
            connected_socket.close()
        except ConnectionAbortedError:
            connected_socket.shutdown(socket.SHUT_RDWR)
            connected_socket.close()
        except OSError:
            logger("[Error]: Connection aborted error")
        logger("Disconnected")



class MainWindow(QMainWindow):
    def __init__(self):
        global logger
        global open_thread

        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow(mapping)
        self.ui.setupUi(self)
        logger = self.ui.getLogger()
        
        self.setWindowIcon(QIcon("icon.ico"))

        open_thread = threading.Thread(target = connection, args=(logger,))
        open_thread.daemon = True
        self.ui.setConnect(connect)
        self.ui.setDisconnect(disconnect)
        self.ui.pushButton_12.clicked.connect(self.updateConfig)
        open_thread.start()
        self.setVisible(False)


    def closeEvent(self, event):
        if closeFlag:
            save_config()
            event.accept()
        else:
            self.setVisible(False)
            event.ignore()
    
    def updateConfig(self):
        global config_file
        res = self.ui.openSettings(config_file)
        if res:
            config_file = res

def onQuit(app, window):
    global closeFlag
    closeFlag = True
    disconnect()
    window.close()
    app.quit()

def onOpen(window):
    window.show()
    window.setVisible(True)

if __name__ == "__main__":
    print(os.getppid())
    load_config()
    app = QApplication(sys.argv)
    global window
    window = MainWindow()
    window.setVisible(False)

    icon = QIcon("icon.ico")
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    menu = QMenu()

    openAction = QAction("Open")
    openAction.triggered.connect(lambda : onOpen(window))
    menu.addAction(openAction)

    quitAction = QAction("Quit")
    quitAction.triggered.connect(lambda: onQuit(app, window))
    menu.addAction(quitAction)

    tray.setContextMenu(menu)

    app.exec()