# sections/bluetooth_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_bluetooth_section():
    label = Gtk.Label(label="Bluetoothの設定をする場所だよ")
    return label, "Bluetooth"
