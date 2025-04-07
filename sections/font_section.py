# sections/font_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_font_section():
    label = Gtk.Label(label="フォントの設定を変えるんだ")
    return label, "フォント"
