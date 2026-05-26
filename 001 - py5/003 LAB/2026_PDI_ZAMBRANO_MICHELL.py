
import py5

def setup():
    py5.size(600, 400)        #se crea la ventana de 600x400 píxeles.
    py5.background(255)       #pinta el fondo de blanco estilo pizarra.
    print('pizarra lista')

def draw():
    #función que se ejecuta en loop.
    if py5.is_mouse_pressed:  #si el mouse está presionado
        #se va a dibuja una línea desde la posición donde el mouse está siendo presionado
        #hasta la posición actual cuando lo suelto, esto crea el efecto de trazado estilo lápiz.
        py5.line(py5.pmouse_x, py5.pmouse_y, py5.mouse_x, py5.mouse_y)

def key_pressed():
    #esta función se ejecuta cuando se aprieta alguna de las teclas siguientes:

    if py5.key == 'c':
        py5.background(255)  #si se presiona c vuelve al background blanco.

    elif py5.key == 'r':
        py5.stroke(255, 0, 0)  #si se presiona r la linea cambia a color rojo.

    elif py5.key == 'b':
        py5.stroke(0, 0, 0)    #si se presiona b la linea vuelve al color negro.

py5.run_sketch()
