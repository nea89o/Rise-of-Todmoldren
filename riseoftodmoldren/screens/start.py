from ..base import State, StateApp


class StartScreen(State):
    def __init__(self):
        self.background = None

    def on_start(self, app: 'StateApp'):
        if self.background is None:
            from .. import assets
            self.background = assets.MENU2.as_tiled_surface(app.screen_rect)

    def on_event(self, app: 'StateApp', event):
        pass

    def on_render(self, app: 'StateApp'):
        app.screen.blit(self.background, (0, 0))
