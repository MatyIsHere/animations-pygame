# Material para Profesores de School Of Tech
# https://github.com/MatyIsHere/animations-pygame
import pygame
import sys

def load_image(name):
    image = pygame.image.load(name)
    return image

class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image('imgdead/dead1.png'))
        self.images.append(load_image('imgdead/dead2.png'))
        self.images.append(load_image('imgdead/dead3.png'))
        self.images.append(load_image('imgdead/dead4.png'))
        self.images.append(load_image('imgdead/dead5.png'))
        self.images.append(load_image('imgdead/dead6.png'))
        self.images.append(load_image('imgdead/dead7.png'))
        self.images.append(load_image('imgdead/dead8.png'))
        self.images.append(load_image('imgdead/dead9.png'))
        self.images.append(load_image('imgdead/dead10.png'))
        self.images.append(load_image('imgdead/dead11.png'))
        self.images.append(load_image('imgdead/dead12.png'))
        self.images.append(load_image('imgdead/dead13.png'))
        self.images.append(load_image('imgdead/dead14.png'))
        self.images.append(load_image('imgdead/dead15.png'))
        self.images.append(load_image('imgdead/dead16.png'))
        self.images.append(load_image('imgdead/dead17.png'))
        self.images.append(load_image('imgdead/dead18.png'))
        self.images.append(load_image('imgdead/dead19.png'))
        self.images.append(load_image('imgdead/dead20.png'))
        self.images.append(load_image('imgdead/dead21.png'))
        self.images.append(load_image('imgdead/dead22.png'))
        self.images.append(load_image('imgdead/dead23.png'))
        self.images.append(load_image('imgdead/dead24.png'))
        self.images.append(load_image('imgdead/dead25.png'))
        self.images.append(load_image('imgdead/dead26.png'))
        self.images.append(load_image('imgdead/dead27.png'))
        self.images.append(load_image('imgdead/dead28.png'))
        self.images.append(load_image('imgdead/dead29.png'))
        self.images.append(load_image('imgdead/dead30.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(5, 5, 601, 502)

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def main():
    pygame.init()
    fpsClock = pygame.time.Clock()
    FPS = 25
    screen = pygame.display.set_mode((1024, 768))

    my_sprite = TestSprite()
    my_group = pygame.sprite.Group(my_sprite)

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        my_group.update()
        screen.fill((0, 0, 0))
        fpsClock.tick(FPS)
        my_group.draw(screen)
        pygame.display.flip()

if __name__ == '__main__':
    main()

