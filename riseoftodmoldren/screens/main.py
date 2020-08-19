from .. import assets
from ..base import State, StateApp


class MainScreen(State):
    background = None
    sack = None
    potion = None

    def on_start(self, app: 'StateApp'):
        if self.background is None:
            self.background = assets.FOREST1.as_tiled_surface(app.screen_rect)
            self.sack = assets.SACK.as_surface()
            self.potion = assets.HEAL_POTION_ICON.as_surface()

    def on_render(self, app: 'StateApp'):
        app.screen.blit(self.background, (0, 0))
        app.screen.blit(self.sack, (25, 600))
        app.screen.blit(self.potion, (760, 435))
