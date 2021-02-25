import pygame


class GameLogic:
    def __init__(self, level, renderer, event_loop):
        self._level = level
        self._renderer = renderer
        self._event_loop = event_loop

    def start_game_loop(self):
        while True:
            if self._handle_events() == False:
                break

            self._render()

            if self._level.is_completed():
                break

    def _handle_events(self):
        for event in self._event_loop.get_event():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.move_robot(dx=-1)
                if event.key == pygame.K_RIGHT:
                    self._level.move_robot(dx=1)
                if event.key == pygame.K_UP:
                    self._level.move_robot(dy=-1)
                if event.key == pygame.K_DOWN:
                    self._level.move_robot(dy=1)
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render_display()
