import pygame as pg

pg.init() # Iniciar pygame

pantalla = pg.display.set_mode((800, 600)) # Crear pantalla

# Bucle principal
game_over = False
while not game_over: # = "Mientras game_over sea falso" ó "while True" , se mete en el bucle. Para salir, game_over a True:

    eventos = pg.event.get() # Procesar eventos. Lo que sale de la lista de event.get(), todo lo  que pasa en la ventana de pygame, lo meto en "eventos" para evitar que se cuelgue el programa
    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True # Si uno de los eventos de event.get() es de tipo cerrar "X", que se cierre pygame, poniendo game_over a True

    pantalla.fill((255, 0, 0)) # Color fondo pantalla

    pg.display.flip() # Hay que hacerlo siempre. Renderiza pantalla

pg.quit() # Al salir del bucle "while not game_over", porque game_over es True, que pygame se pare
