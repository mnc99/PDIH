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

### Ejercicio 2.

A continuación se va a configurar DOSBox para que monte en la unidad C: el directorio donde de encuentra el entorno de
programación Borland C e indicar en que path se encuentran las utilidades de compilación. En mi caso, todos estos archivos
se encuentran en el directorio DOSBOX que he creado para tal efecto con la siguiente ruta en mi equipo: /Users/mnc99/DOSBOX.

Para configurar DOSBox de modo que la unidad C: se monte en la ruta anterior y que inicie desde C: hay que modificar el archivo
de configuración de DOSBox que se encuentra en la siguiente ruta: /Users/mnc99/Library/Preferences/DOSBox 0.74-3-3 Preferences.
En macOS para poder acceder a esta ruta es necesario mostrar los archivos ocultos dentro del directorio de usuario, de otro modo
el directorio Preferences no es visible (para mostrar los archivos ocultos en un directorio en macOS pulsar Command+Shift+.).