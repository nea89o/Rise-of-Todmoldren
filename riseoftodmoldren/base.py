import typing

import pygame
from pygame.event import Event


class BaseApp:
    name: str
    size: typing.Tuple[int, int]

    def __init__(self):
        self.paused = False
        self.weight, self.height = self.size
        self.screen_rect = pygame.Rect(0, 0, *self.size)
        self.screen: pygame.SurfaceType = None
        self.should_close = False
        self.initialized = False

    def on_init(self):
        if self.initialized:
            return
        self.initialized = True
        pygame.init()
        pygame.display.set_caption(self.name)
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def pull_events(self):
        for event in pygame.event.get():
            self.on_event(event)

    def on_event(self, event):
        pass

    def on_update(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pass

    def run(self):
        self.on_init()
        while not self.should_close:
            self.pull_events()
            self.on_update()
            self.on_render()
            pygame.display.flip()
        self.on_cleanup()
        pygame.quit()


class State:
    def on_event(self, app: 'StateApp', event):
        pass

    def on_update(self, app: 'StateApp'):
        pass

    def on_render(self, app: 'StateApp'):
        pass

    def on_start(self, app: 'StateApp'):
        pass


class StateApp(BaseApp):

    def __init__(self):
        super().__init__()
        self.states: typing.List[State] = []

    def on_event(self, event):
        self.states[-1].on_event(self, event)

    def on_start(self):
        self.states[-1].on_start(self)

    def on_update(self):
        self.states[-1].on_update(self)

    def on_render(self):
        self.states[-1].on_render(self)

    def push_state(self, state: State):
        self.states.append(state)
        self.on_start()

    def replace_state(self, new_state: State):
        self.states[-1] = new_state
        self.on_start()

    def pop_state(self):
        self.states.pop()
        self.on_start()
