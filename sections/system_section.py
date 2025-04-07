# sections/system_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_system_section():
    label = Gtk.Label(label="システムの情報とか設定だよ")
    return label, "システム"
