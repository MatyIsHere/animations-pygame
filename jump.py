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
        self.images.append(load_image('imgjump/jump1.png'))
        self.images.append(load_image('imgjump/jump2.png'))
        self.images.append(load_image('imgjump/jump3.png'))
        self.images.append(load_image('imgjump/jump4.png'))
        self.images.append(load_image('imgjump/jump5.png'))
        self.images.append(load_image('imgjump/jump6.png'))
        self.images.append(load_image('imgjump/jump7.png'))
        self.images.append(load_image('imgjump/jump8.png'))
        self.images.append(load_image('imgjump/jump9.png'))
        self.images.append(load_image('imgjump/jump10.png'))
        self.images.append(load_image('imgjump/jump11.png'))
        self.images.append(load_image('imgjump/jump12.png'))
        self.images.append(load_image('imgjump/jump13.png'))
        self.images.append(load_image('imgjump/jump14.png'))
        self.images.append(load_image('imgjump/jump15.png'))
        self.images.append(load_image('imgjump/jump16.png'))
        self.images.append(load_image('imgjump/jump17.png'))
        self.images.append(load_image('imgjump/jump18.png'))
        self.images.append(load_image('imgjump/jump19.png'))
        self.images.append(load_image('imgjump/jump20.png'))
        self.images.append(load_image('imgjump/jump21.png'))
        self.images.append(load_image('imgjump/jump22.png'))
        self.images.append(load_image('imgjump/jump23.png'))
        self.images.append(load_image('imgjump/jump24.png'))
        self.images.append(load_image('imgjump/jump25.png'))
        self.images.append(load_image('imgjump/jump26.png'))
        self.images.append(load_image('imgjump/jump27.png'))
        self.images.append(load_image('imgjump/jump28.png'))
        self.images.append(load_image('imgjump/jump29.png'))
        self.images.append(load_image('imgjump/jump30.png'))

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
    FPS = 30
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

