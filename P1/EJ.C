#include <stdio.h>
#include <dos.h>

#define BYTE unsigned char

BYTE textColor, textBackground;

void mi_pausa(){
   union REGS inregs, outregs;
	 inregs.h.ah = 8;
	 int86(0x21, &inregs, &outregs);
}

// Función para leer la pulsación de una tecla
int mi_getchar(){
	 union REGS inregs, outregs;
	 int caracter;

	 inregs.h.ah = 1;
	 int86(0x21, &inregs, &outregs);

	 caracter = outregs.h.al;
	 return caracter;
}

// Función para mostrar un caracter por pantalla
void mi_putchar(char c){
	 union REGS inregs, outregs;

	 inregs.h.ah = 2;
	 inregs.h.dl = c;
	 int86(0x21, &inregs, &outregs);
}

// Función para colocar el cursor en una posición determinadas
void gotoxy(int x, int y){
	union REGS inregs, outregs;

	inregs.h.ah = 0x02;
	inregs.h.bh = 0x00;
	inregs.h.dh = y; //Número de fila
	inregs.h.dl = x; //Número de columna

	int86(0x10, &inregs, &outregs);
	return;
}

// Función para fijar el aspecto del cursor (INVISIBLE, NORMAL Y GRUESO)
void setcursortype(int tipoCursor){
	union REGS inregs, outregs;

	inregs.h.ah = 0x01;

	//Establecer el tipo de cursor
	switch(tipoCursor){
		case 0: //Invisible
			inregs.h.ch = 010;
			inregs.h.cl = 000;
			break;
		case 1: //Normal
			inregs.h.ch = 010;
			inregs.h.cl = 010;
			break;
		case 2: //Grueso
			inregs.h.ch = 000;
			inregs.h.cl = 010;
			break;
	}

	int86(0x10, &inregs, &outregs);
	return;

}

// Función para establecer el modo de vídeo
void setvideomode(int modoVideo){
	union REGS inregs, outregs;

	inregs.h.ah = 0x00;
	inregs.h.al = modoVideo;

	int86(0x10, &inregs, &outregs);
	return;
}

// Función para obtener el modo de vídeo actual
int getvideomode(){
	union REGS inregs, outregs;
	int modoVideoAct;

	inregs.h.ah = 0xF;

	int86(0x10, &inregs, &outregs);

	modoVideoAct = outregs.h.al;

	return modoVideoAct;
}

// Función para establecer el color principal del texto
void textcolor(BYTE colorPrinc){
	textColor = colorPrinc;

	return;
}

// Función para establecer el color de fondo del texto
void textbackground(BYTE colorFondo){
	textBackground = colorFondo;

	return;
}

// Función para borrar toda la pantalla
void clrscr(){
	union REGS regs;

	regs.h.ah = 15;
	int86(0x10, &regs, &regs);

	regs.h.ah = 0;
	int86(0x10, &regs, &regs);
	
	return;
}

// Función para escribir un carácter en pantalla con el color indicado
void cputchar(char c, int repeticiones){
	union REGS inregs, outregs;

	inregs.h.ah = 0x09;
	inregs.h.al = c;
	inregs.h.bl = (textBackground << 4) | textColor;
	inregs.h.bh = 0x00;
	inregs.x.cx = repeticiones;

	int86(0x10, &inregs, &outregs);

	return;
}

// Función para obtener un carácter de teclado y mostrarlo por pantalla
int getche(){
	union REGS inregs, outregs;
	int caracter;

	inregs.h.ah = 0x00;
	int86(0x16, &inregs, &outregs);

	caracter = outregs.h.al;
	cputchar(caracter, 1);

	return caracter;
}

// Función para poner un píxel en las coordenadas X Y de un color determinado
void cpixel(int x, int y, BYTE c){
	union REGS inregs, outregs;

	inregs.h.ah = 0x0C;
	inregs.h.al = c; //Color
	inregs.x.cx = x; //Columna
	inregs.x.dx = y; //Fila

	int86(0x10, &inregs, &outregs);

	return;

}

// Función para dibujar un cuadrado en modo texto
void square(int xSupIzq, int ySupIzq, int xinfDcha, int yInfDcha, BYTE ctexto, BYTE cFondo){

	// Obtener la longitud de un lado del cuadrado
	int lado = xinfDcha - xSupIzq;
	int i;

	// Activar el modo texto
	setvideomode(3);

	textcolor(ctexto);
	textbackground(cFondo);
	gotoxy(xSupIzq, ySupIzq);

	for (i = 0; i <= lado; i++) {
		gotoxy(xSupIzq+i,ySupIzq);
		cputchar('*', 1);

		gotoxy(xSupIzq+lado,ySupIzq+i);
		cputchar('*',1);

		gotoxy(xSupIzq,ySupIzq+i);
		cputchar('*', 1);

		gotoxy(xinfDcha-i,yInfDcha);
		cputchar('*',1);
	}

	return;
}

// Función para crear dibujos sencillos en pantalla
void draw(){
	int i;

	// Establecer el modo gráfico CGA.
	setvideomode(4);

	for (i = 1; i <= 100; i++){
		cpixel(i,1,i%4);
		cpixel(i,i,i%4);
		cpixel(1+i,100-i,i%4);
		cpixel(1,i,i%4);
		cpixel(i,100,i%4);
		cpixel(i,50,i%4);
		cpixel(100,i,i%4);
		cpixel(50,i,i%4);

	}

	return;
}

int main(){

	int tecla;
	int modoVideoAct;
	BYTE colorPrinc;
	BYTE colorFondo;
	
	
	//1.Colocar el cursor en una posición determinada en pantalla
	printf("1.Colocar el cursor en una posicion determinada en pantalla (Coordenadas --> (40,25))\n");
	gotoxy(40,15);
   mi_pausa();

   //2.Cambiar el aspecto del cursor.
   printf("\n2.Cambiar el aspecto del cursor (INVISIBLE, NORMAL Y GRUESO.)");

   printf("\nCursor invisible: ");
   setcursortype(0);
   mi_pausa();

   printf("\nCursor normal: ");
   setcursortype(1);
   mi_pausa();

   printf("\nCursor grueso: ");
   setcursortype(2);
   mi_pausa();

   //3.Establecer el modo de vídeo.
   printf("\n3.Establecer el modo de video.");

   setvideomode(4);
   printf("\nModo Grafico (320x200)");
   mi_pausa();

   setvideomode(1);
   printf("\nModo Texto (40x25)");
   mi_pausa();

   setvideomode(7);
   printf("\nModo Texto (80x25 2 colores)");
   mi_pausa();

   setvideomode(3);
   printf("\nModo Texto (80x25 16 colores)");
   mi_pausa();

   //4.Obtener el modo de vídeo actual
   printf("\n4.Obtener el modo de video actual.");

   modoVideoAct = getvideomode();

   switch (modoVideoAct) {
   	case 0:
   		printf("\nEl modo de video actual es: Modo Texto (40x25 16 colores)");
   		break;
   	case 1:
   		printf("\nEl modo de video actual es: Modo Texto (40x25 16 colores)");
   		break;
   	case 2:
   		printf("\nEl modo de video actual es: Modo Texto (80x25 16 colores)");
   		break;
   	case 3:
   		printf("\nEl modo de video actual es: Modo Texto (80x25 16 colores)");
   		break;
   	case 4:
   		printf("\nEl modo de video actual es: Modo Gráfico (320x200 4 colores)");
   		break;
   	case 5:
   		printf("\nEl modo de video actual es: Modo Gráfico (320x200 4 colores)");
   		break;
   	case 6:
   		printf("\nEl modo de video actual es: Modo Gráfico (640x200 2 colores)");
   		break;
   	case 7:
   		printf("\nEl modo de video actual es: Modo Texto (80x25 2 colores)");
   		break;
   	case 13:
   		printf("\nEl modo de video actual es: Modo Gráfico (320x200 16 colores)");
   		break;
   	case 14:
   		printf("\nEl modo de video actual es: Modo Gráfico (640x200 16 colores)");
   		break;
   	case 15:
   		printf("\nEl modo de video actual es: Modo Gráfico (640x350 2 colores)");
   		break;
   	case 18:
   		printf("\nEl modo de video actual es: Modo Gráfico (640x480 16 colores)");
   		break;
   	case 19:
   		printf("\nEl modo de video actual es: Modo Gráfico (320x200 256 colores)");
   		break;
   }

   mi_pausa();
	
   //5.Seleccionar el color del texto
   printf("\n5.Establecer el color del texto.");
   colorPrinc = 2;
   printf("\nSe ha establecido como color de texto el verde");
   textcolor(colorPrinc);
   mi_pausa();

   //6.Seleccionar el color de fondo del texto
   printf("\n6.Establecer el color de fondo del texto.");
   colorFondo = 4;
   printf("\nSe ha establecido como color de fondo el rojo");
   textbackground(colorFondo);
   mi_pausa();
   
   //7.Borrar toda la pantalla
   printf("\n7.Borrar toda la pantalla.");
   mi_pausa();
   clrscr();
   printf("\nPantalla borrada.Pulsa una tecla...");
   mi_pausa();
	
	
   //8.Mostrar un caracter por pantalla con el color indicado
   printf("\n8.Mostrar un caracter por pantalla con el color indicado");

   printf("\nEscribe un caracter: ");
   tecla = mi_getchar();

   printf("\nSe ha pulsado la tecla: ");
   cputchar((char) tecla, 1);
   mi_pausa();

   //9.Leer un carácter desde teclado y mostrarlo por pantalla.
   printf("\n9.Leer un caracter desde teclado y mostrarlo por pantalla.");
   textcolor(15);
   textbackground(0);

   printf("\nPulsa una tecla: ");
   printf("\nHas pulsado la tecla: %c", (char) getche());
   mi_pausa();
	
	printf("\n****EJERCICIOS OPCIONALES****\n");

	printf("\n10.Dibujar un recuadro en la pantalla en modo texto.");
	mi_pausa();
	square(20,1, 30, 11, 0, 2);
	mi_pausa();

	printf("\n\n11.Mostrar dibujos sencillos en modo grafico");
	mi_pausa();
	draw();
	mi_pausa();

	return 0;
}
