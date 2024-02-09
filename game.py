import pygame
import os
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Name Of The game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 64)
# testing words
#main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")

def main():
    # pygame setup    
    p1 = PlayerWasd("./exampleShroom.png")
    p2 = PlayerMouse("./sprite.png")
    allsprites = pygame.sprite.RenderPlain((p1,p2))
    running = True
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
    #################################################################
        # RENDER YOUR GAME HERE
        allsprites.update()
        allsprites.draw(screen)


    ##############################################################
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()


class PlayerMouse(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.image, self.rect = load_image(image,scale=.1)#adjust scale to get character sizing right
        self.rect.topleft = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)#adjust arugments for disired starting position
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos






class PlayerWasd(pygame.sprite.Sprite):
    
    def __init__(self,image):
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = 15
        self.image, self.rect = load_image(image,scale=.5)#adjust scale to get character sizing right
        self.rect.topleft = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)#adjust arugments for disired starting position
    def update(self):
        keys = pygame.key.get_pressed()
        (x,y) = self.rect.topleft
        if keys[pygame.K_w]:
            y -= self.speed
        if keys[pygame.K_s]:
            y += self.speed
        if keys[pygame.K_a]:
            x -= self.speed
        if keys[pygame.K_d]:
            x += self.speed
        self.rect.topleft = (x,y)


def writeToScreen(msg, x, y):
        text = font.render(msg, True, (10, 10, 10))
        textpos = text.get_rect(centerx=x, y=y)
        screen.blit(text, textpos)


def load_image(name, colorkey=None, scale=1):
    #fullname = os.path.join(data_dir, name)
    image = pygame.image.load(name)
    size = image.get_size()
    size = (size[0] * scale, size[1] * scale)
    image = pygame.transform.scale(image, size)

    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()















main()