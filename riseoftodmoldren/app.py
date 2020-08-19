import pygame

from .base import StateApp
from .screens.start import StartScreen


class TheRiseOfTodmoldren(StateApp):
    name = "The Rise Of Todmoldren"
    size = (1280, 720)

    def __init__(self):
        super().__init__()

        if not pygame.image.get_extended():
            raise SystemExit("Sorry, extended image module required")

    def on_init(self):
        super().on_init()
        self.push_state(StartScreen())
