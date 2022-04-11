# Seminario: Módulos Cargables del Kernel (LKM)
## Ejercicio: Crear un LKM sencillo para Linux

### Paso 1: Preparar el sistema operativo

Para poder desarrollar LKMs para Linux el sistema operativo debe tener todo lo necesario para
compilar código del kernel, por lo que hay que instalar las cabeceras de Linux con los comandos
siguientes:

![Cabeceras de Linux](https://github.com/mnc99/PDIH/blob/main/S-LKM/Screenshots/cabeceras-linux.png?raw=true)
---

### Paso 2: Código del LKM

El LKM desarrollado es muy simple. Fundamentalmente consta de dos funciones: gandalf_init() y kenobi_exit()
que se ejecutarán cuando el LKM se inicie y se cierre respectivamente. Ambas usan la función
printk() para escribir en el archivo /var/log/kern.log un mensaje de texto. Para identificar cuáles son las
funciones de inicio y de salida del módulo se hace uso de los macros module_init() y module_exit(). Adicionalmente,
el LKM puede recibir un parámetro de entrada para mostrar en los mensajes de texto. El valor por defecto del parámetro
es "world".

El código del LKM se encuentra en el archivo *myLKM.c* situado en esta misma carpeta.
---

### Paso 3: Compilar el LKM

Una vez que el código del LKM está desarrollado, hay que compilarlo. Para ello, se ha empleado un archivo MakeFile
que realiza el proceso de compilación de manera automática. Si todo sale bien, al compilar el LKM se genera un archivo
de extensión .ko con el nombre del módulo, en este caso, *myLKM.ko*.

![Compilación del LKM](https://github.com/mnc99/PDIH/blob/main/S-LKM/Screenshots/Compilar%20LKM.png?raw=true)
---

### Paso 4: Insertar LKM

A continuación, para que el LKM pueda ser usado, hay que cargarlo en el kernel. Gracias a las herramientas del módulo
del kernel este proceso se puede realizar de forma muy sencilla usando la orden *insmod*:

![Inserción del LKM](https://github.com/mnc99/PDIH/blob/main/S-LKM/Screenshots/Insertar%20LKM.png?raw=true)

Tal y como se muestra en la imagen, al listar todos los módulos cargados en el kernel con el comando *lsmod* se puede
ver que el LKM *myLKM* ya se ha insertado en el kernel.
---

### Paso 5: Eliminar LKM

Por último, para asegurar que el LKM funciona correctamente y que muestra un mensaje cuando se sale de él, se va a eliminar del kernel
con el comando *rmmod*:

![Eliminar LKM](https://github.com/mnc99/PDIH/blob/main/S-LKM/Screenshots/Eliminar%20LKM.png?raw=true)

Si se muestra de nuevo la lista del módulos cargados, ya no aparece *myLKM*:

![Lista de LKMs](https://github.com/mnc99/PDIH/blob/main/S-LKM/Screenshots/Lista%20LKM.png?raw=true)
---

### Paso 6: Comprobar /var/log/kern.log

Para comprobar que el LKM ha funcionado como se esperaba, se pasa a comprobar el contenido del archivo
*/var/log/kern.log* con los logs del kernel:

![Logs del Kernel](https://github.com/mnc99/PDIH/blob/main/S-LKM/Screenshots/Logs%20Kernel.png?raw=true)

Tal y como se aprecia en la imagen, el LKM ha escrito un mensaje en el momento en el que fue insertado y
otro cuando se eliminó.