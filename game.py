import pygame as pg
from random import randrange

TAMANNO = (800,600) # Constante para tamaño de pantalla

class Movil(): # Esta clase me va a permitir que defina Raqueta como un Movil. La clase Raqueta y Bola van a HEREDAR de esta y le van a sobrar los parámetros definidos en esta clase
    def __init__(self, x, y, w, h, color = (255, 255, 255)): # Constructor Movil, con parámetros posición, tamaño y color)
        self.x = x # Atributos de la clase (posicióm)
        self.y = y  # posicióm
        self.w = w  # ancho Movil
        self.h = h  # alto Movil
        self.color = color #

    @property # Decorador = pasa una función a atributo (sería como un getter)
    def izquierda(self): # Como es un método lleva (self)
        return self.x

    @izquierda.setter # Decorador (sería como definir un setter). Sintaxis = nombre de la propiedad.setter (La propiedad, en este caso "izquierda" tiene que estar definida anteriormente como propiedad. Lo hizo en el @property superior)
    def izquierda(self, valor):
        self.x = valor

    @property
    def derecha(self):
        return self.x + self.w

    @derecha.setter
    def derecha(self, valor):
        self.x = valor - self.w

    @property
    def arriba(self):
        return self.y

    @arriba.setter
    def arriba(self, valor):
        self.y = valor

    @property
    def abajo(self):
        return self.y + self.h

    @abajo.setter
    def abajo(self, valor):
        self.y = valor - self.h




    def actualizate(self):
        pass

    def dibujate(self, lienzo): # Método para que se pinte en pantalla, en una surface "lienzo". Voy a tener que informar la surface donde quiero que lo dibuje (lienzo)
        pg.draw.rect(lienzo, self.color, pg.Rect(self.x, self.y, self.w, self.h)) # Lo pinta en la surface, con mi color, mi x, mi y, mi w, mi h

    def procesa_eventos(self, lista_eventos=[]): # Método de Movil para procesar los movimientos de las raquetas. Si le pongo la lista_eventos vacia, puedo darsela ya informada o hacer un procesa eventos
        pass


class Raqueta(Movil): # Se añade el Movil
    def __init__(self, x, y, color = (255, 255, 255)): # Constructor de Raqueta, con sus parámetros a definir. Cambia al añadirle "Movil", ahora solo me interesa, posición y color
        Movil.__init__(self, x, y, 20, 120, color) # Llamo a la instanciación de Movil con sus parámetros (posición y color), está HEREDANDO de Movil (sobreescribe el init de la linea anterior), el támaño va a ser el mismo para todas las raquetas, los meto a mano (20,130). Clase dentro de otra clase?
        #self.x = x # Atributos de la clase (posicióm)- Al meter el Movil, este atributo sobra, ya lo hace Movil
        #self.y = y  # posicióm- Al meter el Movil, este atributo sobra, ya lo hace Movil
        #self.w = w  # ancho Raqueta- Al meter el Movil, este atributo sobra, ya lo hace Movil
        #self.h = h  # alto Raqueta- Al meter el Movil, este atributo sobra, ya lo hace Movil
        #self.color = color #- Al meter el Movil, este atributo sobra, ya lo hace Movil
        self.tecla_arriba = pg.K_UP # Atributo para definir las teclas para los eventos
        self.tecla_abajo = pg.K_DOWN

    def procesa_eventos(self, lista_eventos=[]): # Metodo pra procesar eventos
        if pg.key.get_pressed()[self.tecla_arriba]: # Es unmétodo de pygame, devuelve True si la tecla está pulsada o False si no lo está
            self.y -= 5

        if self.arriba <= 0: # Límites pra que la raqueta no se pierda por la parte sup/inf de la pantalla
            self.arriba = 0
        if self.abajo >= TAMANNO[1]:
            self.abajo = TAMANNO[1]

        if pg.key.get_pressed()[self.tecla_abajo]: # Es un método de pygame, devuelve True si la tecla está pulsada o False si no lo está
            self.y += 5
       
        
class Bola(Movil): # Ahora HEREDA de Movil
    def __init__(self, x, y, color=(255, 255, 255)): # Constructor, con sus parámetros a definir
        super().__init__(x, y, 20, 20, color) # Esto, super(), es lo mismo que: "Movil.__init__(self, x, y, 20, 20, color)". Es otra sintaxis para HEREDAR
        #self.x = x # Atributos de la clase (posicióm) - Al meter el Movil, este atributo sobra, ya lo hace Movil
        #self.y = y  # posicióm - Al meter el Movil, este atributo sobra, ya lo hace Movil
        #self.w = w  # ancho Bola - Al meter el Movil, este atributo sobra, ya lo hace Movil
        #self.h = h  # alto Bola - Al meter el Movil, este atributo sobra, ya lo hace Movil
        #self.color = color # - Al meter el Movil, este atributo sobra, ya lo hace Movil
        self.swDerecha = True # Atributo para el cambio de dirección de la bola (eje x) - Le cambia el nombre de self.derecha a swDerecha ????
        self.swArriba = True # Atributo para el cambio de dirección de la bola (eje y) - Le cambia el nombre de self.ariiba a swArriba ????

    def actualizate(self): # Método de la clase Bola (para que se mueva sola)
        if self.swDerecha: # Si self.derecha está a True:
            self.x += 5 # Velocidad hacia la derecha
        else:
            self.x -= 5 # Velocidad hacia la izquierda

        if self.izquierda >= TAMANNO[0]: # Condición cuando la bola toca el límite 800 . Antes del los @property : "if self.x + self.w >= TAMANNO[0]:
            self.swDerecha = False # Cambia de dirección

        if self.derecha <= 0: # Condición cuando la bola toca el límite 0 - # Antes de los property :"if self.x"
            self.swDerecha = True # Cambia de dirección

        if self.swArriba: # Si self.arriba está a True:
            self.y -= 5 # Velocidad hacia arriba
        else:
            self.y += 5 # Velocidad hacia abajo

        if self.abajo >= TAMANNO[1]: # Condición cuando la bola toca el límite 600 . Antes de los @ property: "if self.y + self.h >= TAMANNO[1]:""
            self.swArriba = True # Velocidad hacia arriba

        if self.arriba <= 0:  # Antes de los property :"if self.y"
            self.swArriba = False # Velocidad hacia abajo


class Game():
    def __init__(self): # Contructor
        self.pantalla = pg.display.set_mode((TAMANNO)) # Parametro pantalla = CREAR PANTALLA
        self.reloj = pg.time.Clock() # Atributo reloj de pygame para reducir velocidad bola = CREAR RELOJ
        #self.bolas = [] # Hay que crear el atributo self.bolas con una lista vacia para meter ahí todas las bolas creadas con el bucle, sino peta
        self.todos = [] # Crea una lista vacia para posteriormente añadir ahi todos los objetos que nos interese meter, para iterarlos con un bucle y ahorrar código = CREAR LISTA VACIA
        
        self.player1 = Raqueta(10, (TAMANNO[1] -120) // 2) # Intancia Raqueta 1, con sus parametros definidos (posición x, y, tamaño ancho, alto (definidos en la su clase) y color por defecto) = CREAR PLAYER1
        self.player1.tecla_arriba = pg.K_w # Define teclas para player1
        self.player1.tecla_abajo = pg.K_s # Define teclas para player 1
        self.player2 = Raqueta(TAMANNO[0] -30, (TAMANNO[1] - 120) // 2) # Intancia Raqueta 2, con sus parametros definidos (posición x, y, tamaño ancho, alto (definidos en su clase) y color por defecto) = CREAR PLAYER2

        self.todos.append(self.player1) # Añade a la lista de self.todos la raqueta 1
        self.todos.append(self.player2) # Añade a la lista de self.todos la raqueta 2


        #self.bola = Bola(700 - 10, TAMANNO[1] // 2 - 10, 20, 20) # Instacia la Bola dentro del init de Game, definiendo los atributos de posición y tamaño)
        #for i in range(1): # Para crear 10 bolas con un bucle en vez de crearlas una por una. - Despues de Movil, creamos la bola asi:
            #ancho = randrange(10, 41) # Variable ancho con un random en x, y - Después de Movil, no me hace falta
        self.bola = Bola(TAMANNO[0] //2 -10, TAMANNO[1] //2 -10, (255, 255, 0)) # Definir atibuto bola (como variable local, sin el self.) con posición random, ancho ramdom y color random = CREAR BOLA
        #self.bolas.append(bola) # Mete en la lista vacia, del atributo self.bolas, todas las bola creadas en el bucle "for i in range(10)"
        self.todos.append(self.bola) #Añade bola a la lista vacia

    def bucle_principal(self): # Método de la clase, bucle principal
        game_over = False # no hace falta ponerle self.game_over. Es una variable local dentro del método
        pg.init() # Inicializa pygame

        while not game_over: # = "Mientras game_over sea falso" ó "while True" , se mete en el bucle. Para salir, game_over a True:
            self.reloj.tick(60) # Configuación velocidad del reloj para velocidad bola

            eventos = pg.event.get() # Procesar eventos. Lo que sale de la lista de event.get(), todo lo  que pasa en la ventana de pygame, lo meto en "eventos" para evitar que se cuelgue el programa
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True # Si uno de los eventos de event.get() es de tipo cerrar "X", que se cierre pygame, poniendo game_over a True
                '''
                if evento.type == pg.KEYDOWN: # Si el evento es del tipo presionar tecla
                    if evento.key == pg.K_UP: # evento.key, solo será informado si el evento.type es de tipo KEYDOWN. K_UP es propio de pygame (flecha arriba)
                        self.player2.y -= 5 # La raqueta 2 se mueve 5 hacia arriba. Le informo quien se mueve (self.player2), en que eje se mueve (.y) y cuanto se mueve (-5)
                    if evento.key == pg.K_DOWN:
                        self.player2.y += 5

                    if evento.key == pg.K_w:
                        self.player1.y -= 5
                    if evento.key == pg.K_s:
                        self.player1.y += 5
                '''
                '''
            # Control d eventos para movimiento de las raquetas
            self.player1.procesa_eventos() # Llamada al método de procesar eventos de Raqueta. Hay que diferenciar las teclas de movimiento. Creamos self.tecla_arriba, abajo en clase Game, al instaciar raqueta
            self.player2.procesa_eventos() # Llamada al método de procesar eventos de Raqueta. Hay que diferenciar las teclas de movimiento. Creamos self.tecla_arriba, etc en la clase raqueta
                '''
            

            #self.bola.actualizate() # Llama al método actualizate de la clase Bola, es donde está definido el movimiento de bola
            #for i in range(1): # Llama al método actualizate de la clase Bola, pero para todo el bucle de bolas creadas con el bucle de crear bolas
                #self.bolas[i].actualizate()
            for movil in self.todos: # Iteración para actualizar los personajes. Cuando le toque a bola, ejecuta el def actualizate() de la clase Bola. Cuando le toque a la raqueta (no tiene método actualizate, cogerá el de Movil)
                movil.procesa_eventos() # Aprovecha la iteración para procesar los eventos de raqueta (sustituye a los 2 parrafos comentados de arriba)
                movil.actualizate()


            self.pantalla.fill((0, 0, 0)) # Color fondo pantalla. Lleva self. delante porque es un atributo de la clase (linea 5), sino, no lo reconoce
            #pg.draw.rect(self.pantalla, self.bola.color, pg.Rect(self.bola.x, self.bola.y, self.bola.w, self.bola.h)) # Pinta la bola con el metodo "rect" de pygame (surface, color (bola.color ya está definido),tamaño(bola.x, bola.y...ya están definidos)), lo pintamos despues de pantalla para que se vea, son capas.
            #for i in range(1): # Esto era para antes de Movil y self.todos
                #pg.draw.rect(self.pantalla, self.bolas[i].color, pg.Rect(self.bolas[i].x, self.bolas[i].y, self.bolas[i].w, self.bolas[i].h)) # Bucle para pintar las bola creadas con el bucle, con el metodo "rect" de pygame (surface, color (bola.color ya está definido),tamaño(bola.x, bola.y...ya están definidos)), lo pintamos despues de pantalla para que se vea, son capas.
                #pg.draw.rect(self.pantalla, self.player1.color,pg.Rect(self.player1.x, self.player1.y, self.player1.w, self.player1.h)) # Pinta raqueta del player1, con el método rect de pygame
                #pg.draw.rect(self.pantalla, self.player2.color,pg.Rect(self.player2.x, self.player2.y, self.player2.w, self.player2.h)) # Pinta raqueta del player2, con el método rect de pygame

            for movil in self.todos: # Iteración para pintar todos los personajes (están dentro de self.todos)
                #pg.draw.rect(self.pantalla, personaje.color, pg.Rect(self.pantalla, personaje.color, personaje.x, personaje.y, personaje.w, personaje.h))
                movil.dibujate(self.pantalla) # Movil tiene un método propio para dibujarse, pues lo llamo.


            pg.display.flip() # Hay que hacerlo siempre. Renderiza pantalla
        pg.quit() # Al salir del bucle "while not game_over", porque game_over es True, que pygame se cierre

if __name__ == "__main__":
    juego = Game() # Aquí instancia la clase al objeto juego. Si lo lanzo, aún no hace nada, solo se ha instanciado la clase, no se ha llamado a ningun método
    juego.bucle_principal() # Se llama al método de la clase, ya en el objeto "juego"

