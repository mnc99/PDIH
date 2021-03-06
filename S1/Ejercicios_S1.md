# Seminario 1: Programación de dispositivos a bajo nivel.
## Ejercicios.
### Ejercicio 1.

El primer ejercicio consiste en la instalación del emulador del sistema operativo MS-DOS. Para ello hay que acceder
a la [web](http://www.dosbox.com/) y, en mi caso, descargar el archivo dmg para instalar en macOS. Una vez instalado
DOSBox simplemente hay que ejecutar la aplicación:

![DOSBox en ejecución](https://github.com/mnc99/PDIH/blob/main/S1/Ejecución-DOSBox.png?raw=true)

Como prueba del funcionamiento de DOSBox, se muestra la ejecución del videojuego DOOM. Una vez que se han descargado los
archivos necesarios para el videojuego basta con ejecutarlo escribiendo DOOM e intro en DOSBox.

![Orden para ejecutar DOOM](https://github.com/mnc99/PDIH/blob/main/S1/Comando%20para%20iniciar%20DOOM.png?raw=true)
![Jugando a DOOM](https://github.com/mnc99/PDIH/blob/main/S1/Jugando%20a%20DOOM.png?raw=true)
---
### Ejercicio 2.

A continuación se va a configurar DOSBox para que monte en la unidad C: el directorio donde de encuentra el entorno de
programación Borland C e indicar en que path se encuentran las utilidades de compilación. En mi caso, todos estos archivos
se encuentran en el directorio DOSBOX que he creado para tal efecto con la siguiente ruta en mi equipo: /Users/mnc99/DOSBOX.

![Directorio DOSBOX](https://github.com/mnc99/PDIH/blob/main/S1/Directorio%20DOSBOX.png?raw=true)

Para configurar DOSBox de modo que la unidad C: se monte en la ruta anterior y que inicie desde C: hay que modificar el archivo
de configuración de DOSBox que se encuentra en la siguiente ruta: /Users/mnc99/Library/Preferences/DOSBox 0.74-3-3 Preferences.
En macOS para poder acceder a esta ruta es necesario mostrar los archivos ocultos dentro del directorio de usuario, de otro modo
el directorio Preferences no es visible (para mostrar los archivos ocultos en un directorio en macOS pulsar Command+Shift+.).

![Modificación del archivo de configuración](https://github.com/mnc99/PDIH/blob/main/S1/Configuración%20DOSBOX.png?raw=true)
---
### Ejercicio 3.

Por último se va a mostrar un ejemplo de un programa en ensamblador que muestra por pantalla la cadena de texto
"Hola Mundo". Para compilar el programa de nombre hola.asm se usa el script C.BAT proporcionado indicando el nombre
del programa. Una vez compilado, se ejecuta indicando el nombre del programa y pulsando Intro:

![Programa hola.asm](https://github.com/mnc99/PDIH/blob/main/S1/Hola%20Mundo%20ASM.png?raw=true)
![Compilación y ejecución hola.asm](https://github.com/mnc99/PDIH/blob/main/S1/Compilar%20y%20Ejecutar%20HolaMundo.png?raw=true)

Se va a realizar una modificación del programa anterior para que muestre el mensaje por pantalla siete veces. Se compila y ejecuta
del mismo modo que se ha descrito anteriormente, con la salvedad de que ahora el nombre del programa es holaLoop.asm

![Programa holaLoop.asm](https://github.com/mnc99/PDIH/blob/main/S1/HolaLoop%20ASM.png?raw=true)
![Compilación y ejecución holaLoop.asm](https://github.com/mnc99/PDIH/blob/main/S1/Compilación%20y%20ejecución%20holaLoop.png?raw=true)

