import pygame
import random
import os
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Hangman")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 64)
#main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")
#test
def main():
    # pygame setup    
    # p1 = PlayerWasd("./exampleShroom.png")
    # p2 = PlayerMouse("./sprite.png")
    chosenWord = sportWords()
    uniqueChar = unqiueCharacters(chosenWord)
    wrongGuessCount = 0
    correctLetters = 0
    usedLetters = []
    # allsprites = pygame.sprite.RenderPlain((p1,p2))
    running = True
    background_image = pygame.image.load("./Hangman.jpg")
    background_image = pygame.transform.scale(background_image,(1280, 720))
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in range(97,123):
                    guessLetter = chr(event.key)
                    if guessLetter not in usedLetters:
                        usedLetters.append(guessLetter)
                        if check(guessLetter, chosenWord):
                            correctLetters += 1
                            print(correctLetters)
                            findLocation(chosenWord, guessLetter)
                            #draw location of character
                        else:
                            wrongGuessCount += 1  
                            print(wrongGuessCount)
                            #draw a body part based on incorrect count

        

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
        screen.blit(background_image,(0,0))
        drawWordLine(chosenWord)
        #image,rect = load_image("Hangman.jpg",100,100)
        # writeToScreen("_", 50, 350, size = 100)
        # writeToScreen("_", 100,100,size = 100)
        if wrongGuessCount == 6:
            #draw losing screen
            print("you lose")
            running = False
        if correctLetters == uniqueChar:
            #draw win screen 
            print("you win")
            running = False
    #################################################################
        # RENDER YOUR GAME HERE
        # allsprites.update()
        # allsprites.draw(screen)


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


def writeToScreen(msg, x, y, size = 1000):
    font = pygame.font.Font(None, size)
    text = font.render(msg, True, (10, 10, 10))
    textpos = text.get_rect(centerx=x, y=y)
    screen.blit(text, textpos)

def load_image(name,x, y, colorkey=None, scale=1):
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
        rect = image.get_rect()
        rect.topleft = (x, y)
    return image, rect

#Gets a random sports related word
#chosenWord = random.choice(list of words)
def sportWords():
    sport = ["soccer", "basketball","football", "tennis", "baseball",
             "lacrosse", "golf", "volleyball","badminton","hockey"]
    choosenWord = random.choice(sport)
    return choosenWord
    
# gets the number of unique characters in the choosen word
def unqiueCharacters(chosenWord):
    uniqueChar = []
    for i in chosenWord:
        if i not in uniqueChar:
            uniqueChar.append(i)
    return len(uniqueChar)

# Returns the indexs of where the user guessed correctly at 
def findLocation(chosenWord, userGuess):
    locations = []
    for i, character in enumerate(chosenWord):
        if character == userGuess:
            locations.append(i)
    return locations

# Checks if the users guess character is in the choosen word
def check(userGuess, chosenWord):
    if userGuess.lower() in chosenWord:
        print(f'This letter is in the word!')
        return True
    else:
        print("Incorrect guess! ")
        return False
    

#checks if you lose
def lose(correctLetters, wrongGuessCount):
    while correctLetters < unqiueCharacters:
        if wrongGuessCount == 6:
            print("You lost, try again!")
            break

def drawWordLine(chosenWord):
    for i in range(0, len(chosenWord)):
        writeToScreen("_", 50 * i, 350, size = 100)

#Game logic:
#   6 incorrect guess means you lose
#   You win if you get the word under 6 incorrect guess


#Game visuals
#   draw "hangman" body parts for each incorrect guess
#   hidden word under person
#   un-gussed and gussed characters to the right of the person, crossed out means used

main()