class Fred():
        """fred class variables"""
        x = 0
        y = 625
        isHit = False
        timeHit = 0
        health = 100
        leftImage = None
        rightImage = None
        leftImageHit = None
        rightImageHit = None
        direction = 1
        speed = 8
        pygame = None

        def reset(self, x):
                """reset"""
                self.x = x
                self.y = 625

                self.isHit = False
                self.timeHit = 0
                self.health = 100

                self.direction = 1
                self.speed = 8
                self.pygame = None

        def moveLeft(self, leftBound):
                """moveLeft"""
                if self.direction != 0:
                      self.direction = 0

                if((self.x - self.speed) > leftBound):
                        self.x -= self.speed

        def moveRight(self, rightBound):
                """moveRight"""
                if self.direction != 1:
                        self.direction = 1

                if((self.x + self.speed) + 58 < rightBound):
                        self.x += self.speed


        def loadImages(self, pygame):
                """loadImages"""
                self.leftImage = pygame.image.load("assets/Fred-Left.png")
                self.rightImage = pygame.image.load("assets/Fred-Right.png")
                self.leftImageHit = pygame.image.load("assets/Fred-Left-Hit.png")
                self.rightImageHit = pygame.image.load("assets/Fred-Right-Hit.png")

        def draw(self, surface, time):
                """ draw """
                if time - self.timeHit > 800:
                        self.timeHit = 0
                        self.isHit = False

                if self.direction == 1:
                        if self.isHit is False:
                                surface.blit(self.rightImage, (self.x, self.y))
                        else :
                                surface.blit(self.rightImageHit, (self.x, self.y))
                else :
                        if self.isHit is False:
                                surface.blit(self.leftImage, (self.x, self.y))
                        else :
                                surface.blit(self.leftImageHit, (self.x, self.y))

        def __init__(self, x):
                """init"""
                self.x = x
class Barrel():
        """variables"""
        slots = [(4, 103), 
                (82, 27), (157, 104), 
                (234, 27), (310, 104), 
                (388, 27), (463, 104), 
                (539, 27), (615, 104), 
                (691, 27), (768, 104), 
                (845, 27), (920, 104)]
        slot = 0
        x = 0
        y = 0

        image = None
        brokenImage = None

        isBroken = False
        timeBroken = 0
        needsRemoving = False

        size = [33,22]
        ratio = 0.66

        vy = 1.5
        gravity = 1.05
        maxY = 20

        def split(self, time):
                """split"""
                self.isBroken = True
                self.timeBroken = time
                self.vy = 5
                self.x -= 10

        def checkForCollision(self, fred):
                """collision"""
                hitX = False
                hitY = False
                if fred.x > self.x and fred.x < self.x + 75:
                        hitX = True
                elif fred.x + 57 > self.x and fred.x + 57 < self.x + 75:
                        hitX = True
                if fred.y + 120 > self.y and fred.y < self.y:
                        hitY = True
                elif fred.y < self.y + 48:
                        hitY = True
                if hitX is True and hitY is True:
                        return True

        def loadImages(self, pygame):
                """images"""
                self.image = pygame.image.load("assets/Barrel.png")
                self.brokenImage = pygame.image.load("assets/Barrel_break.png")

        def move(self, windowHeight):
                """move"""
                if self.vy < self.maxY:
                        self.vy = self.vy * self.gravity
                self.y += self.vy

                if self.y > windowHeight:
                        self.needsRemoving = True

        def draw(self, surface, pygame):
                """ draw """
                if self.isBroken is True:
                        surface.blit(self.brokenImage, (self.x, self.y))
                else :
                        surface.blit(self.image, (self.x, self.y))

        def __init__(self, slot):
                """init"""
                self.slot = slot
                self.x = self.slots[slot][0]
                self.y = self.slots[slot][1] + 24

class ToxBarrel(Barrel):
        """variables"""
        slots = [(4, 103), 
                (82, 27), (157, 104), 
                (234, 27), (310, 104), 
                (388, 27), (463, 104), 
                (539, 27), (615, 104), 
                (691, 27), (768, 104), 
                (845, 27), (920, 104)]
        slot = 0
        x = 0
        y = 0

        image = None
        brokenImage = None

        isBroken = False
        timeBroken = 0
        needsRemoving = False

        size = [33,22]
        ratio = 0.66

        vy = 1.5
        gravity = 1.05
        maxY = 20

        def split(self, time):
                """split"""
                self.isBroken = True
                self.timeBroken = time
                self.vy = 5
                self.x -= 10

        def checkForCollision(self, fred):
                """collision"""
                hitX = False
                hitY = False
                if fred.x > self.x and fred.x < self.x + 75:
                        hitX = True
                elif fred.x + 57 > self.x and fred.x + 57 < self.x + 75:
                        hitX = True
                if fred.y + 120 > self.y and fred.y < self.y:
                        hitY = True
                elif fred.y < self.y + 48:
                        hitY = True
                if hitX is True and hitY is True:
                        return True

        def loadImages(self, pygame):
                """images"""
                self.image = pygame.image.load("assets/greenBarrel.png")
                self.brokenImage = pygame.image.load("assets/greenBarrel_break.png")

        def move(self, windowHeight):
                """move"""
                if self.vy < self.maxY:
                        self.vy = self.vy * self.gravity
                self.y += self.vy

                if self.y > windowHeight:
                        self.needsRemoving = True

        def draw(self, surface, pygame):
                """ draw """
                if self.isBroken is True:
                        surface.blit(self.brokenImage, (self.x, self.y))
                else :
                        surface.blit(self.image, (self.x, self.y))

        def __init__(self, slot):
                """init"""
                self.slot = slot
                self.x = self.slots[slot][0]
                self.y = self.slots[slot][1] + 24
