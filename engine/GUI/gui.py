# engine/gui.py

import dearpygui.dearpygui as dpg
from config import SCREEN_WIDTH, SCREEN_HEIGHT


class GUI:
    def __init__(self, game):
        self.game = game
        self.fullscreen = False
        self.resolutions = [(800, 600), (1024, 768), (1280, 720), (1920, 1080)]
        self.current_res = (SCREEN_WIDTH, SCREEN_HEIGHT)

    def start_gui(self):
        dpg.create_context()

        with dpg.window(label="Main Menu", width=400, height=300):
            dpg.add_text("Lopy Engine Main Menu")
            dpg.add_button(label="Start Engine", callback=self.start_engine)
            dpg.add_button(label="Settings", callback=self.open_settings)
            dpg.add_button(label="Quit", callback=self.quit_engine)

        with dpg.window(
            label="Settings", width=400, height=300, show=False, tag="settings_window"
        ):
            dpg.add_text("Settings")
            dpg.add_text("Screen Resolution:")
            dpg.add_combo(
                items=[f"{res[0]}x{res[1]}" for res in self.resolutions],
                default_value=f"{self.current_res[0]}x{self.current_res[1]}",
                callback=self.change_resolution,
            )
            dpg.add_checkbox(
                label="Fullscreen",
                default_value=self.fullscreen,
                callback=self.toggle_fullscreen,
            )
            dpg.add_button(
                label="Back", callback=lambda: dpg.hide_item("settings_window")
            )

        dpg.create_viewport(title="Lopy Engine GUI", width=600, height=400)
        dpg.setup_dearpygui()
        dpg.show_viewport()

    def start_engine(self):
        print("Starting the game...")
        dpg.stop_dearpygui()  # Закрываем Dear PyGui
        self.game.start_game()  # Переход в игровой процесс

    def open_settings(self):
        dpg.show_item("settings_window")

    def change_resolution(self, sender, app_data):
        width, height = map(int, app_data.split("x"))
        self.current_res = (width, height)
        self.game.update_screen_size(self.current_res, self.fullscreen)

    def toggle_fullscreen(self, sender, app_data):
        self.fullscreen = app_data
        self.game.update_screen_size(self.current_res, self.fullscreen)

    def quit_engine(self):
        dpg.stop_dearpygui()
        self.game.running = False  # Завершает весь процесс
