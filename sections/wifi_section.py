# sections/wifi_section.py

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import subprocess

def create_wifi_section():
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    label = Gtk.Label(label="Wi-Fiの設定だよ")
    vbox.pack_start(label, False, False, 0)

    wifi_status_label = Gtk.Label(label="Wi-Fiの状態を取得中...")
    vbox.pack_start(wifi_status_label, False, False, 0)
    update_wifi_status(wifi_status_label)

    return vbox, "Wi-Fi"

def update_wifi_status(label):
    GLib.timeout_add_seconds(5, _update_wifi_status_callback, label)

def _update_wifi_status_callback(label):
    try:
        result = subprocess.run(['nmcli', 'general', 'status'], capture_output=True, text=True, check=True)
        if "connected" in result.stdout:
            label.set_label("Wi-Fi: 接続済み")
        else:
            label.set_label("Wi-Fi: 未接続")
    except subprocess.CalledProcessError:
        label.set_label("Wi-Fiの状態を取得できませんでした")
    return True
