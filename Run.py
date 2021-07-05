import pygame
import sys


class Run(pygame.sprite.Sprite):
    def __init__(self, px, py):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("Assets\Run_1.png"))
        self.sprites.append(pygame.image.load("Assets\Run_2.png"))
        self.sprites.append(pygame.image.load("Assets\Run_3.png"))
        self.sprites.append(pygame.image.load("Assets\Run_4.png"))
        self.sprites.append(pygame.image.load("Assets\Run_5.png"))
        self.sprites.append(pygame.image.load("Assets\Run_6.png"))
        self.sprites.append(pygame.image.load("Assets\Run_7.png"))
        self.sprites.append(pygame.image.load("Assets\Run_8.png"))
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
pygame.display.set_caption("Mario Running")
moving_sprites = pygame.sprite.Group()
run = Run(150, 125)
moving_sprites.add(run)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            run.animate()
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(20)