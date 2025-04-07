# sections/usb_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_usb_section():
    label = Gtk.Label(label="USB関連の設定はこちら")
    return label, "USB"
