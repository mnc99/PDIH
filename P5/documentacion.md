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
```
---

### Ejercicio 2: Dibujar la forma de onda de ambos sonidos.

El código para dibujar la onda de los sonidos es el siguiente:

```
# Mostrar la forma de onda de ambos archivos
plot(extractWave(nombre, from = 1, to = 45004))
plot(extractWave(apellidos, from = 1, to = 68514))
```

La forma de onda del sonido asociado al nombre es:

![Onda Nombre](https://github.com/mnc99/PDIH/blob/main/P5/onda-nombre.png?raw=true)

La forma de onda del sonido asociado a los apellidos es:

![Onda Apellidos](https://github.com/mnc99/PDIH/blob/main/P5/onda-apellidos.png?raw=true)
---

### Ejercicio 3: Obtener la información de las cabeceras de ambos sonidos.

Para obtener la información de las cabeceras asociadas a los archivos de audio de los
sonidos se emplea el siguiente código que hace uso de la función str():

```
# Mostrar información de las cabeceras
str(nombre)
str(apellidos)
```
La información obtenida es la siguiente:

```
> str(nombre)
Formal class 'Wave' [package "tuneR"] with 6 slots
  ..@ left     : num [1:45004] 0 0 0 0 0 0 0 0 0 0 ...
  ..@ right    : num(0) 
  ..@ stereo   : logi FALSE
  ..@ samp.rate: int 44100
  ..@ bit      : int 32
  ..@ pcm      : logi FALSE
> str(apellidos)
Formal class 'Wave' [package "tuneR"] with 6 slots
  ..@ left     : num [1:68514] 0 0 0 0 0 0 0 0 0 0 ...
  ..@ right    : num(0) 
  ..@ stereo   : logi FALSE
  ..@ samp.rate: int 44100
  ..@ bit      : int 32
  ..@ pcm      : logi FALSE
```

---