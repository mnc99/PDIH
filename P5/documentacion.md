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

### Ejercicio 4: Unir ambos sonidos en uno nuevo.

Para unir ambos sonidos y generar uno nuevo basta con usar la función pastew:

```
# Unir ambos archivos en uno nuevo
nombre_completo <- pastew(apellidos, nombre, output = "Wave")
nombre_completo
listen(nombre_completo)
```

---

### Ejercicio 5: Dibujar la forma de onda de la señal resultante.

Para dibujar la forma de onda resultante de unir ambos sonidos se usa la función plot
usada anteriormente:

```
# Mostrar la forma de onda del nuevo sonido
plot(extractWave(nombre_completo, from = 1, to = 113518))
```
La forma de onda obtenida es:

![Onda Nombre y Apellidos](https://github.com/mnc99/PDIH/blob/main/P5/onda-nombre-completo.png?raw=true)

---

### Ejercicio 6: Pasar un filtro de frecuencia para eliminar las frecuencias entre 10000Hz y 20000Hz

Para pasar un filtro de frecuencia al sonido que une el nombre y los apellidos se usa la función bwfilter:

```
f <- nombre_completo@samp.rate #44100
f
nombre_completo_mezcla <- bwfilter(nombre_completo, f = f, channel = 1, n = 1,
                                   from = 10000, to = 20000, bandpass = TRUE,
                                   listen = FALSE, output = "Wave")
nombre_completo_mezcla
listen(nombre_completo_mezcla)
plot(extractWave(nombre_completo_mezcla, from = 1, to = 113518))
```

La forma de onda de la señal con las frecuencias entre 10000Hz-20000Hz eliminadas es:

![Onda Filtro Frecuencia](https://github.com/mnc99/PDIH/blob/main/P5/onda-nombre-completo-filtro.png?raw=true)

---

### Ejercicio 7: Almacenar la señal obtenida como un fichero WAV denominado “mezcla.wav”.

Para almacenar la señal obtenida en un fichero WAV llamado "mezcla.wav" se usa la función writeWave:

```
writeWave(nombre_completo_mezcla, file.path("mezcla.wav"))
```

---

### Ejercicio 8: Cargar un nuevo archivo de sonido, aplicarle eco y a continuación darle la vuelta al sonido. Almacenar la señal obtenida como un fichero WAV denominado “alreves.wav”.

El nuevo archivo de sonido se denomina "fuerza.wav" y contiene la frase: "Que la Fuerza de acompañe" característica de las películas de Star Wars.
Para generar el archivo se ha empleado el mismo comando que en el ejercicio 1:
- say -o fuerza.wav --data-format=LEF32@44100 "Que la Fuerza te acompañe"

Todos los pasos necesarios para realizar el ejercicio se muestran en el código siguiente:

```
# Cargar un nuevo archivo wave
fuerza <- readWave('fuerza.wav')
fuerza

# Aplicar eco al sonido
fuerzaEco <- echo(fuerza, f = 22050, amp = c(0.8,0.4,0.2),delay = c(1,2,3),
                  output = "Wave")
fuerzaEco@left = 10000 * fuerzaEco@left
listen(fuerzaEco)

# Darle la vuelta al sonido
fuerzaEcoAlReves <- revw(fuerzaEco, output = "Wave")
fuerzaEcoAlReves
plot(extractWave(fuerzaEcoAlReves, from = 1, to = 153946))
listen(fuerzaEcoAlReves)

#Almacenar el nuevo sonido generado
writeWave(fuerzaEcoAlReves, file.path("alreves.wav"))
```

La forma de onda de la señal es la siguente:

![Onda Al Reves](https://github.com/mnc99/PDIH/blob/main/P5/onda-al-reves.png?raw=true)

---