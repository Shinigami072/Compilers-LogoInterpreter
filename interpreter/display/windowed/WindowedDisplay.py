import threading

import pyglet

from interpreter.display.windowed.Renderers import EnvironmentRenderer
from interpreter.runtime.Display import EnvironmentDisplay
from interpreter.runtime.Model import Environment


class EnvironentWindow(pyglet.window.Window):

    def __init__(self, environment: Environment, fps: float = 60.0):
        super(EnvironentWindow, self).__init__(resizable=True,
                                               width=round(environment.width),
                                               height=round(environment.height))
        pyglet.clock.schedule_interval(lambda dt: self.on_draw(), 1.0 / fps)
        self.environment = EnvironmentRenderer(environment)
        self._robot = environment.turtle
        self._environment = environment
        self.scale = 1.0

    def on_draw(self):
        self.clear()
        self.set_caption("Turtle Display %s" % str(self._robot))
        pyglet.gl.glPushMatrix()
        pyglet.gl.glScalef(self.scale, self.scale, 1.0)
        self.environment.draw()
        pyglet.gl.glPopMatrix()

    def on_resize(self, width, height):
        super(EnvironentWindow, self).on_resize(width, height)
        ew = self._environment.width
        eh = self._environment.height

        if width > height:
            self.scale = (height / eh)
        else:
            self.scale = (width / ew)


class WindowedDisplay(EnvironmentDisplay):
    def __init__(self, environment: Environment):
        super().__init__(environment)
        self.window = EnvironentWindow(environment=environment)
        self.thread = threading.Thread(target=lambda: pyglet.app.run(), daemon=True)
        self.thread.start()

    def close(self):
        self.window.close()
        self.thread.join(0)
