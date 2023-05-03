import os

from pygame import Surface
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale


class GameObject(Sprite):
    sprite_filename: str | None = None
    sprite_extension: str = "png"
    width: int = 40
    height: int = 40
    color_key: tuple[int, int, int] = (245, 245, 245)

    def __init__(self, topleft_x: int, topleft_y: int):
        super().__init__()
        sprite_image_full_path = os.path.join("resources", f"{self.sprite_filename}.{self.sprite_extension}")
        self.image = scale(load(sprite_image_full_path), (self.width, self.height))
        self.image.set_colorkey(self.color_key)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft_x, topleft_y

    def draw(self, surface: Surface) -> None:
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def is_collided_with(self, another_object: "GameObject") -> bool:
        return self.rect.colliderect(another_object.rect)
