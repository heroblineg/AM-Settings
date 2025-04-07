#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import importlib.util
import os

class SettingsApp(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="システム設定")
        self.set_default_size(800, 600)

        self.notebook = Gtk.Notebook()
        self.notebook.set_tab_pos(Gtk.PositionType.LEFT)
        self.add(self.notebook)

        self.load_sections()

        self.show_all()

    def load_sections(self):
        sections_order = [
            "home_section.py",
            "separator_wifi_bluetooth",
            "wifi_section.py",
            "bluetooth_section.py",
            "separator_display_power_usb_mousekeyboard",
            "display_section.py",
            "power_section.py",
            "usb_section.py",
            "mouse_keyboard_section.py",
            "separator_themebackground_mousecursor_font",
            "theme_background_section.py",
            "mouse_cursor_section.py",
            "font_section.py",
            "separator_system",
            "system_section.py",
        ]

        sections_dir = "sections"
        loaded_sections = set()

        for item in sections_order:
            if item.endswith("_section.py"):
                filename = item
                module_name = filename[:-3]
                filepath = os.path.join(sections_dir, filename)
                spec = importlib.util.spec_from_file_location(module_name, filepath)
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                    create_func_name = f"create_{module_name}"
                    if hasattr(module, create_func_name):
                        create_func = getattr(module, create_func_name)
                        content, tab_label = create_func()
                        self.notebook.append_page(content, Gtk.Label(label=tab_label))
                        loaded_sections.add(filename)
                    else:
                        print(f"Warning: {filename} に関数 '{create_func_name}' がありません。")
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
            elif item.startswith("separator_"):
                # 区切りに見えるラベルを追加する
                separator_label = Gtk.Label(label=" ")  # 空のラベルでスペースを作る
                self.notebook.append_page(separator_label, Gtk.Label(label=""))
                # タブを非表示にする（見た目上区切りのようにする）
                num_pages = self.notebook.get_n_pages()
                self.notebook.set_show_tabs(False) # 一旦非表示にして…
                self.notebook.set_show_tabs(True)  # 再表示。追加されたタブだけ非表示にならない？

        # sections フォルダ内の残りのセクションを読み込む
        for filename in os.listdir(sections_dir):
            if filename.endswith("_section.py") and filename not in loaded_sections:
                module_name = filename[:-3]
                filepath = os.path.join(sections_dir, filename)
                spec = importlib.util.spec_from_file_location(module_name, filepath)
                module = importlib.util.module_from_spec(spec)
                try:
                    spec.loader.exec_module(module)
                    create_func_name = f"create_{module_name}"
                    if hasattr(module, create_func_name):
                        create_func = getattr(module, create_func_name)
                        content, tab_label = create_func()
                        self.notebook.append_page(content, Gtk.Label(label=tab_label))
                except Exception as e:
                    print(f"Error loading remaining section {filename}: {e}")

if __name__ == '__main__':
    app = SettingsApp()
    Gtk.main()
