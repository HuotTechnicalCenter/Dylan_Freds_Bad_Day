import pygame, sys, random, math
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS
import pygame.time as GAME_TIME
import objects

windowWidth = 1000
windowHeight = 768

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption('Fred\'s Bad Day')
textFont = pygame.font.SysFont("monospace", 50)

gameStarted = False
gameStartedTime = 0
gameFinishedTime = 0
gameOver = False

startScreen = pygame.image.load("assets/startgame.png")
endScreen = pygame.image.load("assets/gameover.png")

background = pygame.image.load("assets/background.png")
Fred = objects.Fred(windowWidth / 2)
Barrels = []
toxBarrels = []
lastBarrel = 0
lastBarrelSlot = 0
barrelInterval = 1500

goLeft = False
goRight = False

def quitGame():
        pygame.quit()
        sys.exit()

def newBarrel():
        global Barrels, toxBarrels, lastBarrel, lastBarrelSlot
        whatBarrel = random.randint(0, 5)
        slot = random.randint(0, 12)
        if whatBarrel > 1:
                
                while slot == lastBarrelSlot:
                        slot = random.randint(0, 12)

                theBarrel = objects.Barrel(slot)
                theBarrel.loadImages(pygame)

                Barrels.append(theBarrel)
                lastBarrel = GAME_TIME.get_ticks()
                lastBarrelSlot = slot

        if whatBarrel == 1:
                while slot == lastBarrelSlot:
                        slot = random.randint(0, 12)

                theToxBarrel = objects.ToxBarrel(slot)
                theToxBarrel.loadImages(pygame)

                toxBarrels.append(theToxBarrel)
                lastBarrel = GAME_TIME.get_ticks()
                lastBarrelSlot = slot

Fred.loadImages(pygame)

# 'main' loop
while True:
        
        timeTick = GAME_TIME.get_ticks()

        if gameStarted is True and gameOver is False:

                surface.blit(background, (0, 0))

                Fred.draw(surface, timeTick)

                barrelsToRemove = []
                toxBarrelsToRemove = []

                for idx, barrel in enumerate(Barrels):
                        barrel.move(windowHeight)
                        barrel.draw(surface, pygame)

                        if barrel.isBroken is False:

                                hasCollided = barrel.checkForCollision(Fred);
                                
                                if hasCollided is True:
                                        barrel.split(timeTick)
                                        Fred.isHit = True
                                        Fred.timeHit = timeTick
                                        if Fred.health >= 10:
                                                Fred.health -= 10
                                        else :
                                                gameOver = True
                                                gameFinishedTime = timeTick

                        elif timeTick - barrel.timeBroken > 1000:

                                barrelsToRemove.append(idx)
                                continue

                        if barrel.needsRemoving is True:
                                barrelsToRemove.append(idx)
                                continue

                for idx, toxBarrel in enumerate(toxBarrels):
                        toxBarrel.move(windowHeight)
                        toxBarrel.draw(surface, pygame)
                        
                        if toxBarrel.isBroken is False:

                                hasCollided = toxBarrel.checkForCollision(Fred);
                                
                                if hasCollided is True:
                                        toxBarrel.split(timeTick)
                                        Fred.isHit = True
                                        Fred.timeHit = timeTick
                                        if Fred.health >= 10:
                                                Fred.health = Fred.health - 20
                                        else :
                                                gameOver = True
                                                gameFinishedTime = timeTick

                        elif timeTick - toxBarrel.timeBroken > 1000:

                                toxBarrelsToRemove.append(idx)
                                continue

                        if toxBarrel.needsRemoving is True:
                                toxBarrelsToRemove.append(idx)
                                continue
                
                pygame.draw.rect(surface, (175,59,59), (0, windowHeight - 10, (windowWidth / 100) * Fred.health , 10))

                for index in barrelsToRemove:
                        del Barrels[index]
                for index in toxBarrelsToRemove:
                        del toxBarrels[index]

                        
                if goLeft is True:
                        Fred.moveLeft(0)
                
                if goRight is True:
                        Fred.moveRight(windowWidth)

        elif gameStarted is False and gameOver is False:
                surface.blit(startScreen, (0, 0))

        elif gameStarted is True and gameOver is True:
                surface.blit(endScreen, (0, 0))
                timeLasted = (gameFinishedTime - gameStartedTime) / 1000
        
                if timeLasted < 10:
                        timeLasted = "0" + str(timeLasted)
                else :
                        timeLasted = str(timeLasted)

                renderedText = textFont.render(timeLasted, 1, (175,59,59))
                surface.blit(renderedText, (495, 430))

        # Handle user and system events 
        for event in GAME_EVENTS.get():

                if event.type == pygame.KEYDOWN:

                        if event.key == pygame.K_ESCAPE:
                                quitGame()
                        elif event.key == pygame.K_LEFT:
                                goLeft = True
                                goRight = False
                        elif event.key == pygame.K_RIGHT:
                                goLeft = False
                                goRight = True
                        elif event.key == pygame.K_RETURN:
                                if gameStarted is False and gameOver is False:
                                        gameStarted = True
                                        gameStartedTime = timeTick
                                elif gameStarted is True and gameOver is True:
                                        Fred.reset(windowWidth / 2)
                                        
                                        Barrels = []
                                        toxBarrels = []
                                        barrelInterval = 1500

                                        gameOver = False

        if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                        goLeft = False
                if event.key == pygame.K_RIGHT:
                        goRight = False

                if event.type == GAME_GLOBALS.QUIT:
                        quitGame()

        clock.tick(60)
        pygame.display.update()

        if GAME_TIME.get_ticks() - lastBarrel > barrelInterval and gameStarted is True:
                newBarrel()
                if barrelInterval > 150:
                        barrelInterval -= 50
