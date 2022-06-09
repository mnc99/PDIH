# Seminario: Gestor de dispositivos udev de Linux
## Ejercicio: Crear una regla para udev sencilla

En primer lugar, se han creado dos scripts llamados "insertar.sh" y "retirar.sh"
que se van a ejecutar cuando un dispositivo de tipo USB se inserte o se retire
respectivamente. El contenido de ambos scripts es el que se muestra a continuación:

![Scripts](https://github.com/mnc99/PDIH/blob/main/S-reglas-udev/Screenshots/insertar_retirar.png?raw=true)

Una vez hecho esto se ha creado una nueva regla denominada "regla.rules" en /etc/udev/rules.d/ que tiene
el siguiente contenido:

![Regla](https://github.com/mnc99/PDIH/blob/main/S-reglas-udev/Screenshots/regla.rules.png?raw=true)

Ante una acción de tipo "add" de un dispositivo perteneciente al sistema USB se ejecutará insertar.sh
y ante una acción de tipo "unbind" se ejecutará retirar.sh.

Una vez que se ha añadido la regla es necesario recargar los archivos de reglas de systemd-udevd para
que la nueva regla sea añadida.

![Reload](https://github.com/mnc99/PDIH/blob/main/S-reglas-udev/Screenshots/udevadm_reload.png?raw=true)

Si se ejecuta el comando udevadm monitor --environment --udev para monitorizar los sucesos detectados
por udev se obtiene la siguiente información cuando se desconecta un pendrive USB:

![Monitor](https://github.com/mnc99/PDIH/blob/main/S-reglas-udev/Screenshots/udevadm_monitor.png?raw=true)
![Desconectar](https://github.com/mnc99/PDIH/blob/main/S-reglas-udev/Screenshots/udevadm_monitor_unbind.png?raw=true)

Puesto que los scripts creados anteriormente escribían un mensaje cada vez que el dispositivo se conectaba o desconectaba
en un archivo log.txt en /root/ se comprueba el contenido de dicho archivo para corroborar que la regla está funcionando
correctamente:

![Mensajes](https://github.com/mnc99/PDIH/blob/main/S-reglas-udev/Screenshots/cat_log.png?raw=true)

Se puede ver que se escriben los mensajes correspondientes.

**NOTA IMPORTANTE:** Por una razón que desconozco, cuando conecto y desconecto el USB que he usado para hacer las pruebas
en la máquina virtual con Ubuntu Server, el sistema detecta múltiples inserciones y desconexiones sin retirar el USB del puerto
y debido a eso se escriben muchos mensajes en log.txt (en la captura de pantalla de su contenido se muestra que tiene 235 líneas).
Puede ser que se deba a que estoy usando un adaptador de USB-C a USB-A, pero no lo sé. 