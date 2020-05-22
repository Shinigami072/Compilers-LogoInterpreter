import threading

import pygame

from interpreter.runtime.Display import EnvironmentDisplay
from interpreter.runtime.Model import Environment
from interpreter.display.pygame.Renderers import EnvironmentRenderer

WHITE = pygame.Color(255, 255, 255)


class PygameDisplay(EnvironmentDisplay):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        self.thread = threading.Thread(target=lambda: self.window_eventloop(), daemon=True)

        pygame.init()
        self.environment = EnvironmentRenderer(environment)
        self.screen = pygame.display.set_mode(
            (round(environment.width), round(environment.height)),
            flags=pygame.RESIZABLE)
        self.running = True
        self.thread.start()

    def window_eventloop(self):

        # main loop
        while self.running and threading.currentThread().isAlive():
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    self.close()
                elif event.type == pygame.VIDEORESIZE:
                    self.on_resize()

            self.on_draw()
            pygame.display.update()

    def on_draw(self):
        self.screen.fill(0)
        self.environment.draw(self.screen)

    def on_resize(self):
        pass

    def close(self):
        self.running = False
        self.thread.join(0)
