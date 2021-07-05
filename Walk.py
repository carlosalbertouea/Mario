import pygame
import sys


class Walk(pygame.sprite.Sprite):
    def __init__(self, px, py):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("Assets\Walk_1.png"))
        self.sprites.append(pygame.image.load("Assets\Walk_2.png"))
        self.sprites.append(pygame.image.load("Assets\Walk_3.png"))
        self.sprites.append(pygame.image.load("Assets\Walk_4.png"))
        self.sprites.append(pygame.image.load("Assets\Walk_5.png"))
        self.sprites.append(pygame.image.load("Assets\Walk_6.png"))
        self.sprites.append(pygame.image.load("Assets\Walk_7.png"))
        self.sprites.append(pygame.image.load("Assets\Walk_8.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [px, py]

    def animate(self):
        self.is_animating = True

    def update(self):
        if self.is_animating:
            self.current_sprite += 1
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
            self.image = self.sprites[self.current_sprite]


pygame.init()
clock = pygame.time.Clock()
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Walking")
moving_sprites = pygame.sprite.Group()
walk = Walk(150, 125)
moving_sprites.add(walk)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            walk.animate()
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(10)
