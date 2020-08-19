import pygame

from .main import MainScreen
from .. import assets
from ..base import State, StateApp


class StartScreen(State):
    background = None

    def on_start(self, app: 'StateApp'):
        if self.background is None:
            self.background = assets.MENU2.as_tiled_surface(app.screen_rect)

    def on_keydown(self, app: 'StateApp', key):
        app.replace_state(MainScreen())

    def on_event(self, app: 'StateApp', event):
        if event.type == pygame.MOUSEBUTTONUP:
            app.replace_state(MainScreen())

    def on_render(self, app: 'StateApp'):
        app.screen.blit(self.background, (0, 0))
