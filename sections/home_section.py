# sections/home_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_home_section():
    label = Gtk.Label(label="ようこそ！ここはホームセクションだよ。")
    return label, "ホーム"
