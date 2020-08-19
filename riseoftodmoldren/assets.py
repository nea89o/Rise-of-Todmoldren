import pathlib

import pygame

asset_base = pathlib.Path(__file__).parent.absolute() / 'res'


class ImageAsset:
    def __init__(self, path: str, lazy=True):
        self._path = path
        self._internal = None
        if not lazy:
            self.internal.get_size()

    @property
    def internal(self):
        if self._internal is None:
            self._internal = pygame.image.load(self._path)
            self._internal.convert()
        return self._internal

    @classmethod
    def load_lazy(cls, name: str) -> 'ImageAsset':
        asset_path = asset_base / name
        return cls(str(asset_path))

    def as_tiled_surface(self, size: pygame.Rect) -> pygame.SurfaceType:
        surface = pygame.Surface(size.size, pygame.SRCALPHA, 32)
        for x in range(0, size.width, self.internal.get_width()):
            for y in range(0, size.height, self.internal.get_height()):
                surface.blit(self.internal, (x, y))
        return surface

    def as_surface(self) -> pygame.SurfaceType:
        surface = pygame.Surface(self.internal.get_size(), pygame.SRCALPHA, 32)
        surface.blit(self.internal, (0, 0))
        return surface

    def as_basic_sprite(self, **kwargs) -> pygame.sprite.Sprite:
        sprite = pygame.sprite.Sprite()
        sprite.image = self.internal
        sprite.rect = sprite.image.get_rect(**kwargs)
        return sprite


class SoundAsset:
    def __init__(self, path: str):
        if not pygame.mixer:
            return
        self.internal = pygame.mixer.Sound(path)

    @classmethod
    def load(cls, name: str) -> 'SoundAsset':
        asset_path = asset_base / name
        return cls(str(asset_path))


MENU2 = ImageAsset.load_lazy('menu2.gif')
FOREST1 = ImageAsset.load_lazy('forest1.gif')
FOREST2 = ImageAsset.load_lazy('forest2.gif')
FOREST3 = ImageAsset.load_lazy('forest3.gif')
FOREST4 = ImageAsset.load_lazy('forest4.gif')
FOREST5 = ImageAsset.load_lazy('forest5.gif')
FOREST6 = ImageAsset.load_lazy('forest6.gif')
FOREST7 = ImageAsset.load_lazy('forest7.gif')
FOREST8 = ImageAsset.load_lazy('forest8.gif')
SACK = ImageAsset.load_lazy('sack.gif')
HEAL_POTION_ICON = ImageAsset.load_lazy('heal_potion_icon.gif')
