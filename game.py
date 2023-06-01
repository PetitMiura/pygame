import pygame
import random
import math

class Bolas:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bolas")

        self.players = []
        '''
        for i in range (random.randint(1, 11)):
            b = Ball(random.randint(0, 800), random.randint(0, 600), 15,
                 random.randint(-10, 10), random.randint(-10, 10))
            self.players.append(b)

        #Variable de player = pelota
        #self.player = Ball(400, 300, 30, (255, 255, 255), random.randint(-15, 15), random.randint(-10, 10))
        #self.player = Ball(400, 300, 10, dx=10, dy=15)
        #self.player2 = Ball(200, 200, 30, (255, 255, 0), random.randint(-15, 15), random.randint(-10, 10))
        '''
        self.players.append(
            Ball(150, 150, 15, 10, 10)
        )
        self.players.append(
            Ball(200, 200, 20, -10, -10)
        )
        self.metronomo = pygame.time.Clock()

    def main_loop(self):
        game_over = False

        while game_over == False:
            self.metronomo.tick(30)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_over = True

            self.screen.fill ((0, 255, 0))

            self.players[0].ball_collision(self.players[1])
            
            for bola in self.players:
                bola.draw(self.screen)
                bola.update(self.screen)
                

            
            #self.player.draw(self.screen)
            #self.player2.draw(self.screen)  
            #self.player.update(self.screen)    
            #self.player2.update(self.screen)        
      
            

            pygame.display.flip()

class Ball:
    def __init__(self, x, y, radio, dx=0, dy=0):  # ATRIBUTOS (COMPORTAMIENTO, FUNCION Y ESTADO))
        self.x = x
        self.y = y
        self.radio = radio
        self.color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
        self.dx = dx
        self.dy = dy

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radio)
        
    def update(self, surface):
        self.x += self.dx
        self.y += self.dy

        if self.y >= surface.get_height() - self.radio or self.y <= self.radio:
            self.dy = -self.dy
            
        if self.x >= surface.get_width() - self.radio or self.x <= self.radio:
            self.dx = -self.dx
          
    def ball_collision(self, otra):
        distancia = math.sqrt((otra.x - self.x) ** 2 + (otra.y - self.y) ** 2)
        if distancia <= self.radio + otra.radio:
            self.dx = - self.dx
            self.dy = - self.dy
            otra.dx = - otra.dx
            otra.dy = - otra.dy


if __name__ == "__main__":
    juego = Bolas()
    ball = Ball(400,400,40)
    juego.main_loop()