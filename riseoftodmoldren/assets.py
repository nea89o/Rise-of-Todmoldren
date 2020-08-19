import pathlib

import pygame

asset_base = pathlib.Path(__file__).parent.absolute() / 'res'


class ImageAsset:
    def __init__(self, path: str):
        self.internal = pygame.image.load(path)
        self.internal.convert()

    @classmethod
    def load(cls, name: str) -> 'ImageAsset':
        asset_path = asset_base / name
        return cls(str(asset_path))

    def as_tiled_surface(self, size: pygame.Rect) -> pygame.SurfaceType:
        surface = pygame.Surface(size.size)
        for x in range(0, size.width, self.internal.get_width()):
            for y in range(0, size.height, self.internal.get_height()):
                surface.blit(self.internal, (x, y))
        return surface


class SoundAsset:
    def __init__(self, path: str):
        if not pygame.mixer:
            return
        self.internal = pygame.mixer.Sound(path)

    @classmethod
    def load(cls, name: str) -> 'SoundAsset':
        asset_path = asset_base / name
        return cls(str(asset_path))


MENU2 = ImageAsset.load('menu2.gif')
