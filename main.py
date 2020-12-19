import pygame
from random import randint

pygame.init()

wn = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Ring Ring Hello')

playerImg = pygame.image.load('~/ring-ring-hello/auger.png')
def player(x, y):
      wn.blit(playerImg, (x, y))

playerX = 268
playerY = 268

fixedPoleImg = pygame.image.load("~/ring-ring-hello/fixed-pole.png")
brokenPoleImg = pygame.image.load('~/ring-ring-hello/broken-pole.png')
def poles(img, x, y):
    wn.blit(img, (x, y))

poleIsBroken = []
for i in range(4):
    poleIsBroken.append(False)

poleX = [290, 530, 290, 50]
poleY = [50, 250, 450, 250]
whichPole = randint(0, 3)

running = True
while running:

    wn.fill((0, 0, 0))

    #create events
    for event in pygame.event.get():

        # close window
        if event.type == pygame.QUIT:
            running = False

        # move player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and playerX >= 0:
                playerX -= 20
            if event.key == pygame.K_RIGHT and playerX <= 546:
                playerX += 20
            if event.key == pygame.K_UP and playerY >= 0:
                playerY -= 20
            if event.key == pygame.K_DOWN and playerY <= 546:
                playerY += 20

            for i in range(4):
                if event.key == pygame.K_SPACE and playerX <= poleX[i] + 100 and playerX >= poleX[i] - 64 and playerY >= poleY[i] - 64 and playerY <= poleY[i] + 100 and poleIsBroken[i] == True:
                    whichPole = randint(0, 3)
                    poleIsBroken[i] = False


    if playerX > 546:
        playerX = 564

    if playerX < 0:
        playerX = 0

    if playerY > 546:
        playerY = 546

    if playerY < 0:
        playerY = 0


    # draw objects

    for i in range(4):

        if poleIsBroken[i] == False:
            poles(fixedPoleImg, poleX[i], poleY[i])

        if whichPole == i:
            poleIsBroken[i] = True

        if poleIsBroken[i] == True:
            poles(brokenPoleImg, poleX[i], poleY[i])

    player(playerX, playerY)



    pygame.display.update()
