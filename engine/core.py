# engine/core.py

import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from engine.GUI.gui import GUI


class Game:
    def __init__(self):
        pygame.init()
        self.screen = None  # Инициализируется позже в start_game
        pygame.display.set_caption("Lopy Engine Game")
        self.clock = pygame.time.Clock()
        self.running = True  # Управляет состоянием всего игрового процесса

        # Инициализируем GUI
        self.gui = GUI(self)

    def update_screen_size(self, size, fullscreen):
        """Изменяет размер экрана и режим отображения"""
        flags = pygame.FULLSCREEN if fullscreen else 0
        self.screen = pygame.display.set_mode(size, flags)

    def start_game(self):
        """Запускает pygame после завершения работы GUI"""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.main_loop()  # Запускаем основной игровой цикл

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def run(self):
        # Сначала запускаем интерфейс GUI
        self.gui.start_gui()
        # После закрытия GUI запускаем основной игровой цикл
        if self.running:
            self.start_game()
