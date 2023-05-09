# Example file showing a circle moving on screen
import pygame
import setting
import button

# pygame setup
pygame.init()

#variables
gamePause = False

screen = pygame.display.set_mode((setting.screenWidth, setting.screenHeight))
clock = pygame.time.Clock()
deltaTimeInSeconds = 0

#define font
font = pygame.font.SysFont("arialblack", 40)

textColor = (0,0,255)

startButtonImage = pygame.image.load('play.png').convert_alpha()
optionButtonImage = pygame.image.load('option.png').convert_alpha()

def drawText(text, font, textColor, x, y):
    img = font.render(text, True, textColor)
    screen.blit(img,(x, y))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#
startButton = button.Button(setting.screenWidth / 2, 200, startButtonImage, 1)
optionButton = button.Button(setting.screenWidth / 2, 300, optionButtonImage, 1)
3
running = True
while running:
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    if gamePause == False:
        pygame.draw.circle(screen, "red", player_pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player_pos.y -= 300 * deltaTimeInSeconds
        if keys[pygame.K_s] or  keys[pygame.K_DOWN]:
            player_pos.y += 300 * deltaTimeInSeconds
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            player_pos.x -= 300 * deltaTimeInSeconds
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            player_pos.x += 300 * deltaTimeInSeconds
        pass
    else :
        if startButton.draw(screen):
            print("Start")
        if optionButton.draw(screen):
            print("Option")
        if optionButton.draw(screen):
            print("Option")
        # drawText("Game Paused", font , textColor, setting.screenWidth / 2 , setting.screenHeight / 2)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            #pause game
            if event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE:
                print("game Pause")
                gamePause = not gamePause
        # quit game
        if event.type == pygame.QUIT:
            running = False

    # flip() the display to put your work on screen
    # pygame.display.flip()

    pygame.display.update()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    deltaTimeInSeconds = clock.tick(60) / 1000

pygame.quit()