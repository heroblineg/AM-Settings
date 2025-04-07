# sections/power_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_power_section():
    label = Gtk.Label(label="電源に関する設定をする場所")
    return label, "電源"
