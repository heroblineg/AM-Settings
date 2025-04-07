# sections/mouse_keyboard_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_mouse_keyboard_section():
    label = Gtk.Label(label="マウスとキーボードの設定だよ")
    return label, "マウスとキーボード"
