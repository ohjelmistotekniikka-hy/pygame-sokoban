import pygame


class GameLoop:
    def __init__(self, level, renderer, event_loop, clock, cell_size):
        self._level = level
        self._renderer = renderer
        self._event_loop = event_loop
        self._clock = clock
        self._cell_size = cell_size

    def start(self):
        while True:
            if self._handle_events() == False:
                break

            current_time = self._clock.get_ticks()

            self._level.update(current_time)
            self._render()

            if self._level.is_completed():
                break

            self._clock.tick(60)

    def _handle_events(self):
        for event in self._event_loop.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_robot(dx=-self._cell_size)
                if event.key == pygame.K_RIGHT:
                    self._level.move_robot(dx=self._cell_size)
                if event.key == pygame.K_UP:
                    self._level.move_robot(dy=-self._cell_size)
                if event.key == pygame.K_DOWN:
                    self._level.move_robot(dy=self._cell_size)
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()
