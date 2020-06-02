"""Grupo-4AN: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


		Walder Jose Velasquez Gurdian     - 20002218 - AN

		Luis Andres Garcia Guerrero       - 20006364 - AN

		Stephany Alexandra Quan Aguirre   - 20010374 - AN


JUEGO INTERACTIVO: CONNECT4 - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
#IMPORTAR LIBRERIAS-----------------------------
from time import sleep
import sys
import os
import random as rd

#COLORES Y ESTILOS DE TEXTO---------------------
Blue = (0,0,255)
Blck = (0,0,0)
NBold = '\033[0m'
Bolds = '\033[1m'
Systm = '\033[93m'
Users = '\033[92m'
Red = '\033[91m'

#DATOS INICIALES-------------------------------
RowCnt = 5
Column = 6

#CABECERA--------------------------------------
def Head():
	print(Systm + Bolds + "   ___   ___  _       ___                           _            _  _     ____  ")
	print("  / __\ / __\/ |_    / _ \_ __ ___  _   _  ___  ___| |_ ___    _| || |_  |___ \ ")
	print(" / /   / /   | (_)  / /_)/ '__/ _ \| | | |/ _ \/ __| __/ _ \  |_  ..  _|   __) |")
	print("/ /___/ /___ | |_  / ___/| | | (_) | |_| |  __/ (__| || (_) | |_      _|  / __/ ")
	print("\____/\____/ |_(_) \/    |_|  \___/ \__, |\___|\___|\__\___/    |_||_|   |_____|")
	print("                                    |___/                                       ")
	print("Grupo-4AN: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
	print("	Walder Jose Velasquez Gurdian     - 20002218 - AN")
	print("	Luis Andres Garcia Guerrero       - 20006364 - AN")
	print("	Stephany Alexandra Quan Aguirre   - 20010374 - AN\n")
	print("JUEGO INTERACTIVO: CONNECT4 - - - - - - - - - - - - - - - - - - - - - - - - - - -\n\n" + NBold + Users)

#PROCESO PRINCIPAL-----------------------------
def Main():
	os.system("clear")
	Head()
	print(Systm + Bolds + "	| MENU PRINCIPAL |:\n" + NBold + Users)
	print("	Opcion 1 - Player Vs Player (Juega Con Tus Amigos)")
	print("	Opcion 2 - Player Vs CPU (Prueba Tu Habilidad)")
	print("	Opcion 3 - CPU Vs CPU (Observa Como Juegan)\n")
	print("	Opcion 4 - Instrucciones Del Juego\n")
	print("	Opcion 5 - Salir Del Juego\n\n")

	try:
		Op = int(input("Ingrese La Opcion De Juego Que Desea: "))
	except ValueError:
		Error(1)

	#SALIR DEL PROGRAMA
	if Op == 5:
		print(Systm + Bolds + "\n\nSaliendo Del Juego... Gracias Por Jugar\n" + NBold + Users)
		sys.exit()
	elif Op == 4:
		Help(1)
	else:
		print()
		try:
			RowCnt = int(input("Ingrese El Numero De Filas (>5): "))
		except ValueError:
			Error(1)

		try:
			Column = int(input("Ingrese El Numero De Columnas (>6): "))
		except ValueError:
			Error(1)

		#VERIFICAR TABLERO VALIDO
		if RowCnt < 5 or Column < 6 or RowCnt > 10 or Column > 10:
			Error(1)
		else:
			if Op > 0 and Op < 4:
				Pl1 = ""
				Pl2 = ""
				Board = Create(RowCnt,Column)
				Play(Op,RowCnt,Column,Board,Pl1,Pl2)
				Main()
			else:
				Error(1)

#HELP E INSTRUCCIONES------------------------
def Help(Cod):
	#INSTRUCCIONES
	if Cod == 1:
		os.system("clear")
		Head()
		print(Systm + Bolds + "| INSTRUCCIONES DE JUEGO |\n" + NBold + Users)
		print(Systm + Bolds + "Connect4 " + NBold + Users + "Se Juega En Un Tablero De X Filas y X Columnas, Las Columnas Se Encuentran Enumeradas Para Facilitar La Jugabilidad")
		print("El Objetivo Del Juego Es Alinear Cuatro Fichas Iguales En Diagonal, Horizontal o Verticalmente")

		print(Systm + Bolds + "\n\nDesarrollo Del Juego:\n" + NBold + Users)
		print("Cada Jugador a Su Turno Juega Una De Sus Fichas En La Columna De Su Eleccion")
		print("Físicamente, la rejilla está dispuesta de forma vertical, de forma que las fichas\nson insertadas en una ranura desde arriba y caen hasta la fila más baja no ocupada aun.")
		print("Así, se elige la columna donde se pone, pero no la fila; la ficha que se acaba de\ninsertar cae hasta la fila más baja aún disponible.")
		print("Desde luego, no puede jugarse en una columna.")
		print("\nSi el tablero se llena completamente sin que ningún jugador logre alinear 4 fichas de su color,\nla partida es declarada en empate.\n\n")

		input("Presiona ENTER Para Continuar...")
		Main()
	#HELP SOBRE EL TABLERO
	elif Cod == 2:
		print(Systm + Bolds + "Help: " + NBold + Users + "Trata De Conectar Cuatro Fichas En Cualquier Direccion y Ganaras")

#MOSTRAR ERROR-------------------------------
def Error(N):
	print(Systm + Bolds + "\nERROR! Opcion No Valida...\nReiniciando En 3 Segundos..." + NBold + Users)
	sleep(3)
	Op = 0
	Move = 0
	if N == 1:
		Main()

#CREAR TABLERO ------------------------------
def Create(RowCnt, Column):
	Board = []
	for x in range(RowCnt):
		Row = []
		for y in range(Column):
			Row.append("|")
		Board.append(Row)
	return Board

#IMPRIMIR TABLERO-------------------
def Show(Board):
	#MOSTRAR TABLERO
	for x in range(len(Board)):
		print(str(Board[x]))
	#MOSTRAR NUMERO DE COLUMNAS
	for x in range(len(Board[0])):
		print(Systm + Bolds + "  ", x, end = " " + NBold + Users)
	print("\n")

#EMPATE-----------------------------
def IsTie(Board):
	for x in range(len(Board[0])):
		if Board[0][x] == "|":
			return False
	return True

#GANADOR----------------------------
def IsWinner(board,piece,Column,RowCnt):
	#HORIZONAL
	for c in range(Column-3):
		for r in range(RowCnt):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	#VERTICAL
	for c in range(Column):
		for r in range(RowCnt-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	#PENDIENTE POSITIVA
	for c in range(Column-3):
		for r in range(RowCnt-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	#PENDIENTE NEGATIVA
	for c in range(Column-3):
		for r in range(3, RowCnt):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True
	return False

#PROCEDIMIENTO DE JUEGO PRINCIPAL-------------
def Play(Mod,RowCnt,Column,Board,Pl1,Pl2):
	Pj1 = "X"
	Pj2 = "O"

	os.system("clear")
	Head()
	Help(2)

	#SOLICITAR NOMBRE DE JUGADORES
	print("\n\n")
	if Pl1 == "" or Pl2 == "":
		Pl1 = input("Ingrese El Nombre Del Jugador Uno: ")
		Pl2 = input("Ingrese El Nombre Del Jugador Dos: ")

	#VERIFICAR NOMBRES EN BLANCO
	if Pl1 == "" or Pl1 == " " or Pl2 == "" or Pl2 == " ":
		Pl1 = ""
		Pl2 = ""
		print(Systm + Bolds + "\nERROR! Nombre En Blanco...\nReiniciando En 3 Segundos...\n" + NBold + Users)
		sleep(3)
		Play(Mod,RowCnt,Column,Board,Pl1,Pl2)

	#ELEJIR QUIEN JUEGA PRIMERO
	Turn = int(rd.randint(1,3))
	if Turn == 1:
		Turn = Pj1
	else:
		Turn = Pj2

	#BUCLE DE JUEGO
	while(True):
		os.system("clear")
		Head()
		Help(2)
		#PLAYER VS PLAYER
		if Mod == 1:
			print(Systm + Bolds + "\n| PLAYER Vs PLAYER |\n" + NBold + Users)
			Show(Board)
			print("Player One (" + Pl1 + "): X\nPlayer Two (" + Pl2 + "): O\n")
			print("Es El Turno De Jugar La Ficha: ", Turn)
			try:
				Move = int(input("Ingrese Su Jugada: "))
			except ValueError:
				print(Systm + Bolds + "\nERROR! Jugada No Valida\nReiniciando En 3 Segundos...\n" + NBold + Users)
				sleep(3)
				Play(Mod,RowCnt,Column,Board,Pl1,Pl2)

		#PLAYER VS CPU
		elif Mod == 2:
			print(Systm + Bolds + "\n| PLAYER Vs CPU |\n" + NBold + Users)
			Show(Board)
			print("Player One (" + Pl1 + "): X (YOU)\nPlayer Two (" + Pl2 + "): O\n")
			print("Es El Turno De Jugar La Ficha: ", Turn)
			if Turn == Pj1:
				try:
					Move = int(input("Ingrese Su Jugada: "))
				except ValueError:
					print(Systm + Bolds + "\nERROR! Jugada No Valida\nReiniciando En 3 Segundos...\n" + NBold + Users)
					sleep(3)
					Play(Mod,RowCnt,Column,Board,Pl1,Pl2)
			else:
				Move = rd.randint(0,Column-1)
				print("Ingrese Su Jugada: ",Move)
				sleep(1)

		#CPU VS CPU
		elif Mod == 3:
			print(Systm + Bolds + "\n| CPU Vs CPU |\n" + NBold + Users)
			Show(Board)
			print("Player One (" + Pl1 + "): X\nPlayer Two (" + Pl2 + "): O\n")
			print("Es El Turno De Jugar La Ficha: ", Turn)
			Move = rd.randint(0,Column-1)
			print("Ingrese Su Jugada: ",Move)
			sleep(1)

		#SI NO ES NINGUNA
		else:
			print(Systm + Bolds + "\nERROR! Opcion No Habilitada\nReiniciando En 3 Segundos...\n" + NBold + Users)
			sleep(3)
			Main()

		#DEJAR CAER LA FICHA
		L = len(Board)
		for x in range(L):
			try:
				if Board[L-1-x][Move] == "|":
					Board[L-1-x][Move] = Turn
					break
			except IndexError:
				print(Systm + Bolds + "\nERROR! Jugada No Valida\nReiniciando En 3 Segundos...\n" + NBold + Users)
				sleep(3)
				Play(Mod,RowCnt,Column,Board,Pl1,Pl2)

		#GANADOR
		if IsWinner(Board,Turn,Column,RowCnt):
			if Turn == Pj1:
				Turn = Pl1 + " (" + Pj1 + ")"
			elif Turn == Pj2:
				Turn = Pl2 + " (" + Pj2 + ")"
			os.system("clear")
			Head()
			print(Systm + Bolds + "\n\n| FINISH! El Ganador Es: " + Turn + " |\n\n" + NBold + Users)
			Show(Board)
			Rst = input("¿Desea Volver a Jugar? (S/N): ")
			print(Systm + Bolds + "\nReiniciando En 5 Segundos...\n" + NBold + Users)
			sleep(5)
			if Rst == "S" or Rst == "s":
				Board = Create(RowCnt,Column)
				Play(Mod,RowCnt,Column,Board,Pl1,Pl2)
			else:
				Main()
			break

		#EMPATE
		if IsTie(Board):
			os.system("clear")
			Head()
			print(Systm + Bolds + "\n\n| GAME OVER! Es Un Empate, Juego Terminado... |\n\n" + NBold + Users)
			Show(Board)
			Rst = input("¿Desea Volver a Jugar? (S/N): ")
			print(Systm + Bolds + "\nReiniciando En 5 Segundos...\n" + NBold + Users)
			sleep(5)
			if Rst == "S" or Rst == "s":
				Board = Create(RowCnt,Column)
				Play(Mod,RowCnt,Column,Board,Pl1,Pl2)
			else:
				Main()
			break

		#CAMBIO DE JUGADOR
		if Turn == Pj1:
			Turn = Pj2
		else:
			Turn = Pj1

#PANTALLA DE INICIO-----------------------
def InMain():
	Ld = "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░"
	for x in range(0,len(Ld)+1):
		os.system("clear")
		print(Systm + Bolds + "\n\n\n\n\n")
		L1 = "	 ██░ ██ ▓█████  ██▓     ██▓    ▒███████▒▓█████  ▄████▄  "
		print(L1)
		print("	▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ▒ ▒ ▒ ▄▀░▓█   ▀ ▒██▀ ▀█  ")
		print("	▒██▀▀██░▒███   ▒██░    ▒██░    ░ ▒ ▄▀▒░ ▒███   ▒▓█    ▄ ")
		print("	░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░      ▄▀▒   ░▒▓█  ▄ ▒▓▓▄ ▄██▒")
		print("	░▓█▒░██▓░▒████▒░██████▒░██████▒▒███████▒░▒████▒▒ ▓███▀ ░")
		print("	 ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░░▒▒ ▓░▒░▒░░ ▒░Version 0.1")
		print("	 ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░░░▒ ▒ ░ ▒ ░ ░  ░  ░  ▒   ")
		print("	 ░  ░░ ░   ░     ░ ░     ░ ░   ░ ░ ░ ░ ░   ░   ░        ")
		print("	 ░  ░  ░   ░  ░    ░  ░    ░  ░  ░ ░       ░  ░░ ░      ")
		print("	                               ░               ░        ")
		print(NBold + Users)
		print("	\ -----------------LOADING THE PROGRAM---------------- /")
		print("	"+Ld)
		Ld = Ld.replace("░","█",1)
		sleep(0.1)
	Main()

#PANTALLE DE CARGA-----------------------------
InMain()