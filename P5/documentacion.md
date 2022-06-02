# Práctica 5: Experimentación con el sistema de sonido.
## Ejercicios
### Ejercicio 1: Leer dos ficheros de sonido (WAV o MP3) de unos pocos segundos de duración cada uno. En el primero debe escucharse el nombre de la persona que realiza la práctica. En el segundo debe escucharse el apellido.

Para generar los ficheros en formato WAV se ha usado el programa de línea de comandos disponible
en macOS denominado "say":
- say -o nombre.wav --data-format=LEF32@44100 "Moisés"
- say -o apellidos.wav --data-format=LEF32@44100 "Noguera Carrillo"

El código en R para realizar el ejercicio es el siguiente:

```
# Cargar los archivos wav del nombre y los apellidos
nombre <- readWave('nombre.wav')
nombre
apellidos <- readWave('apellidos.wav')
apellidos
```r