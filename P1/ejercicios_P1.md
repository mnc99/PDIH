# Práctica 1: Entrada/Salida utilizando interrupciones con lenguaje C
## Ejercicio: Programar funciones similares a las proporcionadas por la librería conio.lib
### Función gotoxy(int x, int y)

Mediante esta función es posible colocar el cursor en cualquier posición en pantalla dada por los
valores de X e Y.

![Código gotoxy](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/gotoxy.png?raw=true)
![Ejecución gotoxy](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20gotoxy.png?raw=true)
---

### Función setcursortype(int tipoCursor)

Gracias a esta función se puede modificar el tamaño del cursor (invisible, normal, grueso) indicando como
parámetro el tipo de cursor deseado.

![Código setcursortype](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/setcursortype.png?raw=true)
![Ejecución setcursortype](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20setcursortype.png?raw=true)
---

### Función setvideomode(int modoVideo)

A través de esta función se puede establecer el modo de vídeo que se desee indicando el número asociado
al modo correspondiente como parámetro. En los ejemplos de ejecución se ha variado entre los modos de
vídeo: Modo Gráfico (320x200), Modo Texto (40x25), Modo Texto (80x25 con 2 colores) y Modo Texto (80x25 con 16 colores).

![Código setvideomode](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/setvideomode.png?raw=true)
![Ejecución setvideomode 1](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20setvideomode%201.png?raw=true)
![Ejecución setvideomode 2](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20setvideomode%202.png?raw=true)
![Ejecución setvideomode 3](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20setvideomode%203.png?raw=true)
![Ejecución setvideomode 4](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20setvideomode%204.png?raw=true)
---

### Función getvideomode()

Función muy sencilla que únicamente indica el modo de vídeo establecido actualmente. En este caso, el modo de vídeo coincide
con el último establecido durante la ejecución: Modo Texto (80x25 con 16 colores).

![Código getvideomode](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/getvideomode.png?raw=true)
![Ejecución getvideomode](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20getvideomode.png?raw=true)
---

### Funciones textcolor(BYTE colorPrinc) y textbackground(BYTE colorFondo)

Mediante la llamada a textcolor y a textbackground se establece el color principal y de fondo del texto respectivamente.
No involucran ninguna interrupción. En el ejemplo se ha establecido como color de texto el verde (código 2) y como color
de fondo el rojo (código 4).

![Código textcolor y textbackground](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/textcolor%20y%20textbackground.png?raw=true)
![Ejecución textcolor y textbackground](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20textcolor%20y%20textbackground.png?raw=true)
---

### Función clrscr()

La función clrscr se encarga de borrar todo lo que se esté mostrando en la pantalla en ese momento. Se muestra una imagen
de la pantalla antes de llamar a la función y después.

![Código clrscr](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/clrscr.png?raw=true)
![Ejecución clrscr antes](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20clrscr%20(antes).png?raw=true)
![Ejecución clrscr](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20clrscr.png?raw=true)
---

### Función cputchar(char c, int repeticiones)

Esta función muestra un carácter dado como parámetro el número de repeticiones indicado. Para mostrar su funcionamiento
se escribe un carácter desde teclado y se muestra con el color y las repeticiones indicadas.

![Código cputchar](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/cputchar.png?raw=true)
![Ejecución cputchar](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20cputchar.png?raw=true)
---

### Función getche()

La función getche obtiene un carácter de teclado y lo muestra por pantalla.

![Código getche](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/getche.png?raw=true)
![Ejecución getche](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20getche.png?raw=true)
---

## Ejercicios opcionales: Funciones square y draw

### Función square(int xSupIzq, int ySupIzq, int xinfDcha, int yInfDcha, BYTE ctexto, BYTE cFondo)

Con la llamada de la función square se dibuja un recuadro en la pantalla en modo texto. Se reciben como parámetros
las coordenadas en pantalla de la esquina superior izquierda y derecha del recuadro y los colores principal y secundario
del carácter que se va a usar para dibujar el recuadro (en el ejemplo '*'). El color principal usado es el negro y el
color de fondo el verde.

![Código square](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/square.png?raw=true)
![Ejecución square](https://github.com/mnc99/PDIH/blob/main/P1/Screenshots/Ejecución%20square.png?raw=true)
---