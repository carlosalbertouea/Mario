import pygame
import sys


class Jump(pygame.sprite.Sprite):
    def __init__(self, px, py):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load("Assets\Jump_1.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_2.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_3.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_4.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_5.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_6.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_7.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_8.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_9.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_10.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_11.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_12.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_13.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_14.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_15.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_16.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_17.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_18.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_19.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_20.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_21.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_22.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_23.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_24.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_25.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_26.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_27.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_28.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_29.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_30.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_31.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_32.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_33.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_34.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_35.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_36.png"))
        self.sprites.append(pygame.image.load("Assets\Jump_37.png"))
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
pygame.display.set_caption("Mario Jumping")
moving_sprites = pygame.sprite.Group()
jump = Jump(150, 125)
moving_sprites.add(jump)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            jump.animate()
    screen.fill((0, 0, 0))
    moving_sprites.draw(screen)
    moving_sprites.update()
    pygame.display.flip()
    clock.tick(30)