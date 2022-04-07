# Práctica 2: Uso de bibliotecas de programación de interfaces de usuario en modo texto.
## Ejercicio: Programar videojuego similar a Pong! usando la biblioteca ncurses.
### Introducción

Haciendo uso de la biblioteca *ncurses* para programación de interfaces de usuario en modo texto
y del lenguaje de programación Python se ha desarrollado un videojuego simple similar al clásico
Pong! de 1972.
---

### Funcionamiento del videojuego

El funcionamiento del videojuego es muy simple. Al iniciar el juego lo primero que aparecerá será una
ventana en la que se indica que se introduzca el nombre del primer jugador, una vez introducido y pulsada
la tecla "Enter" el juego solicitará el nombre del segundo jugador.

![Nombre Jugador 1](https://github.com/mnc99/PDIH/blob/main/P2/Screenshots/player1-name.png?raw=true)
![Nombre Jugador 2](https://github.com/mnc99/PDIH/blob/main/P2/Screenshots/player2-name.png?raw=true)

Una vez que se han introducido los nombres de los dos jugadores, se muestra una nueva ventana que indica
los controles del juego:

- Controles jugador 1:
    - Mover barra hacia arriba: Pulsar tecla 'a'.
    - Mover barra hacia abajo: Pulsar tecla 'z'.

- Controles jugador 2:
    - Mover barra hacia arriba: Pulsar tecla 'k'.
    - Mover barra hacia abajo: Pulsar tecla 'm'.

![Controles jugadores](https://github.com/mnc99/PDIH/blob/main/P2/Screenshots/controles-jugadores.png?raw=true)

A continuación comienza la partida. En la zona de arriba de la pantalla se muestra información con los nombres
de los jugadores y sus puntos, mientras que en la zona de abajo de la pantalla se informa de que se puede salir
del juego pulsando la tecla 'q'. Al inicio de la partida la bola sale desde una desde el centrohacia uno de los 
jugadores. En el momento en el que un jugador marque, la pelota vuelve a salir desde una posición aleatoria del 
centro pero siempre en la dirección del jugador que ha marcado.

![Ejemplo de partida](https://github.com/mnc99/PDIH/blob/main/P2/Screenshots/partida.png?raw=true)

En el momento en el que uno de los jugadores llegue a 10 puntos gana la partida y termina el juego.

![Fin de partida](https://github.com/mnc99/PDIH/blob/main/P2/Screenshots/game%20over.png?raw=true)