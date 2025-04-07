# sections/display_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_display_section():
    label = Gtk.Label(label="ディスプレイの設定だよん")
    return label, "ディスプレイ"
