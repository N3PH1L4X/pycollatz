#!/usr/bin/env python3

## Se necesita instalar la libreria matplotlib
from matplotlib import pyplot as plt

## Funciones de calculo
def impar(numero):
    numero = (numero * 3) + 1
    return int(numero)

def par(numero):
    numero = numero / 2
    return int(numero)

def numero_mas_alto(arreglo):
    mas_alto = 0
    for x in range(0, len(arreglo)):
        if(arreglo[x] > mas_alto):
            mas_alto = arreglo[x]
    return int(mas_alto)

## Idioma / Language
idioma = "es" ## You can set the script in english by changing from 'es' to 'en'

## Variables
eleccion = ''
n = 0
numero_ingresado = 0
n_calculos = 0
n_unos = 0
anterior = 0
maximo = 0
arreglo_resultados = [] ## Donde se almacenan los numeros calculados en cada ejecucion
resultado_formato = "" ## Variable para almacenar el numero calculado transformado a string
arreglo_resultados_formato = [] ## Arreglo que se imprime con los numeros formateados para tener separador de miles

## Numero de veces que se repetirá el bucle final 1=>4
cantidad_repeticion_bucle_final = 5 ## Puedes cambiarlo si lo deseas

## Banners
if idioma == "es":
    print("""
                ____      _ _       _       
    _ __  _   _ / ___|___ | | | __ _| |_ ____
    | '_ \| | | | |   / _ \| | |/ _` | __|_  /
    | |_) | |_| | |__| (_) | | | (_| | |_ / / 
    | .__/ \__, |\____\___/|_|_|\__,_|\__/___|
    |_|    |___/    Hecho por: Jose Lopez (N3PH1L4X)
                    https://github.com/N3PH1L4X

    Este script está pensado para ejemplificar,
    explicar y demostrar la conjetura de Collatz,
    tambien conocida como 3N+1


    """)
elif idioma == "en":
    print("""
                ____      _ _       _       
    _ __  _   _ / ___|___ | | | __ _| |_ ____
    | '_ \| | | | |   / _ \| | |/ _` | __|_  /
    | |_) | |_| | |__| (_) | | | (_| | |_ / / 
    | .__/ \__, |\____\___/|_|_|\__,_|\__/___|
    |_|    |___/    Made by: Jose Lopez (N3PH1L4X)
                    https://github.com/N3PH1L4X

    This script is intended to exemplify,
    explain and demonstrate the Collatz conjecture,
    also known as 3N+1


    """)

while True:
    try:
        if n_calculos == 0:
            if idioma == "es":
                numero_ingresado = int(input("Ingrese un numero: "))
            elif idioma == "en":
                numero_ingresado = int(input("Insert a number: "))
            n = numero_ingresado
    except KeyboardInterrupt:
        if idioma == "es":
            print("\nTerminando...")
        elif idioma == "en":
            print("\nQuitting...")
        break
    except:
        if idioma == "es":
            print("Error: debe ingresar un numero entero. Reintentando...")
        elif idioma == "en":
            print("Error: must insert an integer. Retrying...")
        continue

    if n_unos == cantidad_repeticion_bucle_final:
        if idioma == "es":
            print("\nNumero ingresado: ", '{:,}'.format(numero_ingresado).replace(',', '.'), "\nNumero de ciclos 1=>4: ", '{:,}'.format(n_unos).replace(',', '.'), "\nNumero maximo alcanzado: ", '{:,}'.format(maximo).replace(',', '.'), "\nNumero de calculos realizados: ", '{:,}'.format(n_calculos).replace(',', '.'), "\n")
        elif idioma == "en":
            print("\nInserted number: ", '{:,}'.format(numero_ingresado).replace(',', '.'), "\nNumber of 1=>4 cycles: ", '{:,}'.format(n_unos).replace(',', '.'), "\nHighest number calculated: ", '{:,}'.format(maximo).replace(',', '.'), "\nNumber of calculations made: ", '{:,}'.format(n_calculos).replace(',', '.'), "\n")

        try:
            if idioma == "es":
                eleccion = str(input("¿Desea mostrar el grafico de comportamiento? s/N: "))
            elif idioma == "en":
                eleccion = str(input("Would you like to show the behaviour graph? y/N: "))
        except KeyboardInterrupt:
            if idioma == "es":
                print("\nTerminando...")
            elif idioma == "en":
                print("\nQuitting...")
            break

        if (eleccion == "s") or (eleccion == "S") or (eleccion == "y") or (eleccion == "Y"):
            x = range(0, int(len(arreglo_resultados)))
            plt.plot(x, arreglo_resultados)
            if idioma == "es":
                plt.title('Grafico de comportamiento')
                plt.xlabel('Pasos')
            elif idioma == "en":
                plt.title('Behaviour graph')
                plt.xlabel('Steps')
            plt.ylabel('Extension')
            plt.yticks([0,1,2,4, maximo * 0.25, maximo * 0.50, maximo * 0.75, maximo])
            plt.xticks([0, int(len(arreglo_resultados) * 0.25), int(len(arreglo_resultados) * 0.50), int(len(arreglo_resultados) * 0.75), int(len(arreglo_resultados))])
            plt.show()

        try:
            if idioma == "es":
                eleccion = str(input("¿Desea calcular otro numero? s/N: "))
            elif idioma == "en":
                eleccion = str(input("Do you want to calculate another number? y/N: "))
        except KeyboardInterrupt:
            if idioma == "es":
                print("\nTerminando...")
            elif idioma == "en":
                print("\nQuitting...")
            break

        if (eleccion == "s") or (eleccion == "S") or (eleccion == "y") or (eleccion == "Y"):
            ## Regresar a default todas las variaibles
            eleccion = ''
            n = 0
            numero_ingresado = 0
            n_calculos = 0
            n_unos = 0
            anterior = 0
            maximo = 0
            arreglo_resultados = []
            resultado_formato = ""
            arreglo_resultados_formato = []
            print("\n")
            continue
        else:
            if idioma == "es":
                print("\nTerminando...")
            elif idioma == "en":
                print("\nQuitting...")
            break
    else:
        ## Calcular pares
        if n % 2 == 0:
            if n_calculos == 0:
                arreglo_resultados.append(n)

            anterior = n
            n = par(n)
            anterior = n

            maximo = max(arreglo_resultados)

            n_calculos = n_calculos + 1
            arreglo_resultados.append(n)

            resultado_formato = str('{:,}'.format(n).replace(',', '.'))
            arreglo_resultados_formato.append(resultado_formato)

            if n_calculos != 0:
                if n == 1:
                    n_unos = n_unos + 1

        ## Calcular impares
        elif (n % 2 != 0) and (n > 0):
            if n_calculos == 0:
                arreglo_resultados.append(n)

            anterior = n
            n = impar(n)
            anterior = n

            maximo = max(arreglo_resultados)

            n_calculos = n_calculos + 1
            arreglo_resultados.append(n)

            resultado_formato = str('{:,}'.format(n).replace(',', '.'))
            arreglo_resultados_formato.append(resultado_formato)
            
            if n_calculos != 0:
                if n == 1:
                    n_unos = n_unos + 1