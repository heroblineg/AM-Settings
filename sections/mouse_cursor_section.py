# sections/mouse_cursor_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_mouse_cursor_section():
    label = Gtk.Label(label="マウスカーソルの設定だ")
    return label, "マウスカーソル"
