# sections/sound_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def create_sound_section():
    label = Gtk.Label(label="サウンドの設定はこちらでどうぞ")
    return label, "サウンド"
