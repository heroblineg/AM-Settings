# sections/theme_background_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_theme_background_section():
    label = Gtk.Label(label="テーマや背景をカスタマイズ！")
    return label, "テーマと背景"
