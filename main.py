import pygame

"""
def DrawCursor(self):
        self.game.DrawText('*', 30, self.cursor_rect.x, self.cursor_rect.y + 5)
"""


class Game():
    def __init__(self):  # Konstruktor do przechowania podstawowych zmiennych:
        pygame.init()
        self.SCREEN_W = 800
        self.SCREEN_H = 400
        self.window = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.start = True
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.fontName = "Gang Wolfik Blade.ttf"
        self.KEY_UP = False  # kontroler akcji klawisza
        self.KEY_DOWN = False  # kontroler akcji klawisza
        self.state = 'Menu'
        self.stateX = self.SCREEN_W / 2
        self.stateY = self.SCREEN_H / 2

    def Init(self):
        pygame.display.set_caption("My Menu")

    def UpdateEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.start = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("Wcisnalem strzalke w gore")
                    self.KEY_UP = True
                if event.key == pygame.K_DOWN:
                    print("wcisnalem strzalke w dol")
                    self.KEY_DOWN = True

    def CheckKeys(self):
        if (self.KEY_DOWN == True):
            if (self.state == 'Menu'):
                self.state = 'Options'
                self.stateY = self.SCREEN_H / 2 + 50
            elif (self.state == 'Options'):
                self.state = 'Exit'
                self.stateY = self.SCREEN_H / 2 + 100
            elif (self.state == 'Exit'):
                self.state = 'Menu'
                self.stateY = self.SCREEN_H / 2
        elif (self.KEY_UP):
            if (self.state == 'Menu'):
                self.state = 'Exit'
                self.stateY = self.SCREEN_H/2 + 100
            elif (self.state == 'Options'):
                self.state = 'Menu'
                self.stateY = self.SCREEN_H/2
            elif (self.state == 'Exit'):
                self.state = 'Options'
                self.stateY = self.SCREEN_H/2 + 50
    def ResetKeys(self):
        self.KEY_DOWN = False
        self.KEY_UP = False
    def Update(self):
        self.UpdateEvents()
        self.CheckKeys()
        self.ResetKeys()
        pygame.display.update()

    def DrawText(self, text, size, x, y):
        font = pygame.font.Font(self.fontName, size)
        textSurface = font.render(text, True, self.WHITE)
        textRectangle = textSurface.get_rect()
        textRectangle.center = (x, y)
        self.window.blit(textSurface, textRectangle)

    def DrawPointer(self):
        self.DrawText("*", 40, self.stateX - 150, self.stateY + 10)

    def Render(self):
        self.window.fill(self.BLACK)
        self.DrawText("Menu Gry", 48, self.SCREEN_W / 2, self.SCREEN_H / 2 - 100)
        self.DrawText("Nowa gra", 40, self.SCREEN_W / 2, self.SCREEN_H / 2)
        self.DrawText("Opcje", 40, self.SCREEN_W / 2, self.SCREEN_H / 2 + 50)
        self.DrawText("Wyjscie", 40, self.SCREEN_W / 2, self.SCREEN_H / 2 + 100)
        self.DrawPointer()

    def Run(self):
        self.Init()
        while self.start:
            self.Update()
            self.Render()


# MAIN PROGRAM:
game = Game()
game.Run()
