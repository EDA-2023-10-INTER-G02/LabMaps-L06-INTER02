"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones  y  por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


# Inicializacion de la comunicacion con el controlador
def newController():
    """
    Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


# Funciones para la impresión de resultados


def printAuthorData(author):
    """
    Imprime la información del autor seleccionado
    """
    if author:
        print('Autor encontrado: ' + author['name'])
        print('Promedio: ' + str(author['average_rating']))
        print('Total de libros: ' + str(lt.size(author['books'])))
        for book in lt.iterator(author['books']):
            print('Titulo: ' + book['title'] + '  ISBN: ' + book['isbn'])
        print("\n")
    else:
        print('No se encontro el autor.\n')


def printBooksbyTag(books):
    """
    Imprime los libros que han sido clasificados con
    una etiqueta
    """
    if (books):
        print('Se encontraron: ' + str(lt.size(books)) + ' Libros.')
        for book in lt.iterator(books):
            print(book['title'])
        print("\n")
    else:
        print("No se econtraron libros.\n")


def printBooksbyYear(books):
    """
    Imprime los libros que han sido publicados en un
    año
    """
    if(books):
        print('Se encontraron: ' + str(lt.size(books)) + ' Libros')
        for book in lt.iterator(books):
            print(book['title'])
        print("\n")
    else:
        print("No se encontraron libros.\n")


def printBestBooks(books):
    """
    Imprime la información de los mejores libros
    por promedio
    """
    size = lt.size(books)
    if size:
        print(' Estos son los mejores libros: ')
        for book in lt.iterator(books):
            print('Titulo: ' + book['title'] + '  ISBN: ' +
                  book['isbn'] + ' Rating: ' + book['average_rating'])
        print("\n")
    else:
        print('No se encontraron libros.\n')


def printBooksbyTitle(books,size):
    #lab 6, completar la funcion para imprimir los libros
    """
    Completar la descripcion de printBooksbyTitle
    """
    if books != None:
        book = books["value"]
        print("De los " +str(size) + " libros del catálogo se encontró la siguiente información:\n")
        print("Título: " + book["original_title"])
        print("Autor(es): " + book["authors"])
        print("Año: " + book["original_publication_year"])
        print("ISBN: " + book["isbn"])
        print("Idioma: " + book["language_code"])
        print("Puntuación promedio: " + book["average_rating"] + "\n")
        
    else:
        print("No se encontró el libro :( \n ")

# Menu de opciones


def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Consultar los libros de un año")
    print("4- Consultar los libros de un autor")
    print("5- Consultar los Libros por etiqueta")
    print("6- Consultar los Libros por título")
    print("0- Salir")


# Menu principal
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # Se crea el controlador asociado a la vista
        ctrlr = newController()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(ctrlr)
        print('Libros cargados: ' + str(controller.booksSize(ctrlr)))
        print('Autores cargados: ' + str(controller.authorsSize(ctrlr)))
        print('Géneros cargados: ' + str(controller.tagsSize(ctrlr)))

    elif int(inputs[0]) == 3:
        number = input("Buscando libros del año?: ")
        books = controller.getBooksYear(ctrlr, int(number))
        printBooksbyYear(books)

    elif int(inputs[0]) == 4:
        authorname = input("Nombre del autor a buscar: ")
        authorinfo = controller.getBooksByAuthor(ctrlr, authorname)
        printAuthorData(authorinfo)

    elif int(inputs[0]) == 5:
        label = input("Etiqueta a buscar: ")
        books = controller.getBooksByTag(ctrlr, label)
        printBooksbyTag(books)

    elif int(inputs[0]) == 6:
        #lab 6, conectar con las funciones del controlador e imprimir
        title = input("Nombre del libro a buscar: ")
        info_book = controller.getBooksByTitle(ctrlr, title)
        size = controller.booksSize(ctrlr)
        printBooksbyTitle(info_book,size)
        # controller.titleSize(ctrlr)
        
        pass

    elif int(inputs[0]) == 0:
        break

    else:
        continue
sys.exit(0)
