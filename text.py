from pygame import Surface
from pygame.font import Font


class Text(Font):
    def __init__(
        self,
        text: str,
        topleft: tuple[int, int],
        font_size: int = 30,
        font_color: tuple[int, int, int] | None = None,
    ) -> None:
        super().__init__(None, font_size)
        self.__font_color = font_color or (255, 255, 255)
        self.__text = text
        self.__topleft = topleft

    def draw(self, surface: Surface) -> None:
        surface.blit(self.render(self.__text, 0, self.__font_color), self.__topleft)
