import pygame as pg
from random import randrange

TAMANNO = (800,600) # Constante para tamaño de pantalla


class Bola():
    def __init__(self, x, y, w, h, color=(255, 255, 255)): # Constructor, con sus atributos a definir
        self.x = x # Atributos de la clase (posicióm)
        self.y = y  # posicióm
        self.w = w  # ancho bola
        self.h = h  # alto bola
        self.color = color #
        self.derecha = True # Atributo para el cambio de dirección de la bola (eje x)
        self.arriba = True # Atributo para el cambio de dirección de la bola (eje y)

    def actualizate(self): # Método de la clase Bola (para que se mueva sola)
        if self.derecha: # Si self.derecha está a True:
            self.x += 5 # Velocidad hacia la derecha
        else:
            self.x -= 5 # Velocidad hacia la izquierda

        if self.x + self.w >= TAMANNO[0]: # Condición cuando la bola toca el límite 800
            self.derecha = False # Cambia de dirección

        if self.x <= 0: # Condición cuando la bola toca el límite 0
            self.derecha = True # Cambia de dirección

        if self.arriba: # Si self.arriba está a True:
            self.y -= 5 # Velocidad hacia arriba
        else:
            self.y += 5 # Velocidad hacia abajo

        if self.y + self.h >= TAMANNO[1]: # Condición cuando la bola toca el límite 600
            self.arriba = True # Velocidad hacia arriba

        if self.y <= 0: 
            self.arriba = False # Velocidad hacia abajo


class Game():
    def __init__(self): # Contructor
        self.pantalla = pg.display.set_mode((TAMANNO)) # Parametro pantalla = Crear pantalla
        self.reloj = pg.time.Clock() # Atributo reloj de pygame para reducir velocidad bola
        self.bolas = [] # Hay que crear el atributo self.bolas con una lista vacia para meter ahí todas las bolas creadas con el bucle, sino peta
        #self.bola = Bola(700 - 10, TAMANNO[1] // 2 - 10, 20, 20) # Instacia la Bola dentro del init de Game, definiendo los atributos de posición y tamaño)
        for i in range(10): # Para crear 10 bolas con un bucle en vez de crearlas una por una
            ancho = randrange(10, 41) # Variable ancho con un random en x, y 
            bola = Bola(randrange(0, TAMANNO[0]), randrange(0, TAMANNO[1]),ancho, ancho, (randrange(256), randrange(256), randrange(256))) # Definir atibuto bola (como variable local, sin el self.) con posición random, ancho ramdom y color random
            self.bolas.append(bola) # Mete en la lista vacia, del atributo self.bolas, todas las bola creadas en el bucle "for i in range(10)"

    def bucle_principal(self): # Método de la clase, bucle principal
        game_over = False # no hace falta ponerle self.game_over. Es una variable local dentro del método
        pg.init() # Inicializa pygame

        while not game_over: # = "Mientras game_over sea falso" ó "while True" , se mete en el bucle. Para salir, game_over a True:
            self.reloj.tick(60) # Configuación velocidad del reloj para velocidad bola

            eventos = pg.event.get() # Procesar eventos. Lo que sale de la lista de event.get(), todo lo  que pasa en la ventana de pygame, lo meto en "eventos" para evitar que se cuelgue el programa
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True # Si uno de los eventos de event.get() es de tipo cerrar "X", que se cierre pygame, poniendo game_over a True

            #self.bola.actualizate() # Llama al método actualizate de la clase Bola, es donde está definido el movimiento de bola
            for i in range(10): # Llama al método actualizate de la clase Bola, pero para todo el bucle de bolas creadas con el bucle de crear bolas
                self.bolas[i].actualizate()


            self.pantalla.fill((0, 0, 0)) # Color fondo pantalla. Lleva self. delante porque es un atributo de la clase (linea 5), sino, no lo reconoce
            #pg.draw.rect(self.pantalla, self.bola.color, pg.Rect(self.bola.x, self.bola.y, self.bola.w, self.bola.h)) # Pinta la bola con el metodo "rect" de pygame (surface, color (bola.color ya está definido),tamaño(bola.x, bola.y...ya están definidos)), lo pintamos despues de pantalla para que se vea, son capas.
            for i in range(10):
                pg.draw.rect(self.pantalla, self.bolas[i].color, pg.Rect(self.bolas[i].x, self.bolas[i].y, self.bolas[i].w, self.bolas[i].h)) # Bucle para pintar las bola creadas con el bucle, con el metodo "rect" de pygame (surface, color (bola.color ya está definido),tamaño(bola.x, bola.y...ya están definidos)), lo pintamos despues de pantalla para que se vea, son capas.


            pg.display.flip() # Hay que hacerlo siempre. Renderiza pantalla
        pg.quit() # Al salir del bucle "while not game_over", porque game_over es True, que pygame se cierre

if __name__ == "__main__":
    juego = Game() # Aquí instancia la clase al objeto juego. Si lo lanzo, aún no hace nada, solo se ha instanciado la clase, no se ha llamado a ningun método
    juego.bucle_principal() # Se llama al método de la clase, ya en el objeto "juego"

