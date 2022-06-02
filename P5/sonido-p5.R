# Ejercicios P5 (PDIH)

# Comandos usados para generar los archivos -wav:
# say -o nombre.wav --data-format=LEF32@44100 "Moisés"
# say -o apellidos.wav --data-format=LEF32@44100 "Noguera Carrillo"
# say -o fuerza.wav --data-format=LEF32@44100 "Que la Fuerza te acompañe"

# Paquetes necesarios
library(tuneR)
library(seewave)
library(audio)

# Establecer directorio de trabajo
setwd("/Users/mnc99/Desktop/PDIH/Sonido")
# Solo en macOS
setWavPlayer('/usr/bin/afplay')

# Cargar los archivos wav del nombre y los apellidos
nombre <- readWave('nombre.wav')
nombre
apellidos <- readWave('apellidos.wav')
apellidos

# Mostrar la forma de onda de ambos archivos
plot(extractWave(nombre, from = 1, to = 45004))
plot(extractWave(apellidos, from = 1, to = 68514))

# Mostrar información de las cabeceras
str(nombre)
str(apellidos)

# Unir ambos archivos en uno nuevo
nombre_completo <- pastew(apellidos, nombre, output = "Wave")
nombre_completo
listen(nombre_completo)
# Mostrar la forma de onda del nuevo sonido
plot(extractWave(nombre_completo, from = 1, to = 113518))

# Eliminar las frecuencias entre 10000Hz y 20000Hz
f <- nombre_completo@samp.rate #44100
f
nombre_completo_mezcla <- bwfilter(nombre_completo, f = f, channel = 1, n = 1,
                                   from = 10000, to = 20000, bandpass = TRUE,
                                   listen = FALSE, output = "Wave")
nombre_completo_mezcla
listen(nombre_completo_mezcla)
plot(extractWave(nombre_completo_mezcla, from = 1, to = 113518))
writeWave(nombre_completo_mezcla, file.path("mezcla.wav"))

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
