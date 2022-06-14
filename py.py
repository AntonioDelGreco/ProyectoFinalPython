from os import system
dataLibros = []
carrito = {}
reseñas = {'merlin' : 'un libro copado'}
 
def extraccionDatos():

    #!funcion ayuda para la extraccion de los libros en forma de lista

    data = ''
    archivo = open('archivo.txt', 'a+')
    archivo.seek(0)
    data = archivo.readlines()
    archivo.close()
    return data
 
def inscripcion(nombre):

    #!funcion ayuda para saber si ya esta agregado un libro

    for i in extraccionDatos():
        if nombre in i:
            return True
 
def carro(a, b):

    #!funcion ayuda para la compra de libros

    if carrito.get(a) == None:  
        carrito[a] = b
   
    desea = int(input('Desea seguir comprando? (0 para no / 1 para si): '))
    if desea == 1:
        buscarLibro()
 
def carroActivo():

    #!vista del carrito de compras

    total = 0
    for i in carrito.values():
        total += i
    compra = int(input('Comprar los libros seleccionados? (0 para no / 1 para si): '))
    if compra == 1:
        print('------------------------------')
        print('       TICKET DE COMPRA ')
        print('------------------------------')
        print('           BBLIOTECA  ')
        print('')
        print('Costos:')
        for i, j in carrito.items():
            print(f'\n  {i}: ${j}')
        print('')
        print('')
        print (f'El total de su compra es: ${total}')
        print ('')
        print ('¡Gracias por su compra!')
        input()
       
def buscarLibro():

    #!buscar un libro del catalogo
 
    archivo = open('archivo.txt', 'a+')
    print ('*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
    print ('1: Buscar por Autor')
    print ('2: Buscar por Nombre')
    print ('3: Buscar por Genero\n')
    print ('*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
    eleccion = int (input ('Elija una opcion: '))
   
    if eleccion == 1:
        general = 'Autor'
    elif eleccion == 2:
        general = 'Nombre'
    elif eleccion == 3:
        general = 'Genero'

    print('+---------------------------------------')
    variable = input(f'\nIntroducir {general} del libro: ')
    print ('')
    print('+-------------------------')
 
    archivo.seek(0)
    for i in archivo:
        if variable in i:
            nombreLibro, autor, generos, precio = i.strip().split('; ')
            print(f'\nNombre: {nombreLibro}\nAutor: {autor}\nGeneros: {generos}\nPrecio: {precio}\n')
            precioNum = int(precio)
    input ()
   
    if  eleccion == 2:
        print('..................................................')
        carrito = int(input('Desea agregar al carrito este libro? (0 para no / 1 para si): '))
        print ('................................')
        if carrito == 1:
            carro(nombreLibro, precioNum)
 
    archivo.close()
   
def agregarlibro ():

    #!agregar un libro al catalogo

        archivo = open('archivo.txt', 'a+')
        print ('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
        nombre = input('Nombre del libro: ')
        dataLibros.append(nombre)
        dataLibros.append(input ('Autor/es del libro: '))
        dataLibros.append(input ('Genero/s del libro (si es nas de uno separarlo con ","): '))
        dataLibros.append(input ('¿Precio que al que quiere venderlo? '))
        print ('')
        print ('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print ('')
        if inscripcion(nombre):
            print('+--------------------------------------------------------')
            print('¡Su libro ya esta registrado, ingrese uno distinto!')
            print('+-------------------------------------')
            input()
        else:
            formato = '; '.join(dataLibros)
            archivo.write(formato + '\n')
            print('+---------------------------------')
            print ('¡Registro Exitoso!')
            print('+--------------------')
            input ()
            archivo.close()
 
   
def busquedaDeLibros(nombre):
    
    #!funcion ayuda para la busqueda de libros

    archivo = open('archivo.txt', 'r')
    archivo.seek(0)
    for i in archivo:
        if nombre in i:
            return True
 
def reseña ():
   
    #!breve opinion acerca del libro 

    print ('+------------------------------+\n')
    print ('1) Buscar Reseña')
    print ('2) Agregar Reseña\n')
    print ('+--------------------+\n')
    eleccion = int(input('¿Eleccion?:'))
 
    if eleccion == 1:

        #!buscando breve opinion acerca del libro 

        print ('+------------------------------\n')
        nombre = input('Nombre del libro: ')
        print ('+--------------------\n')
        if busquedaDeLibros(nombre):
            for j in reseñas:
                if j == nombre:
                    print(f'{nombre}:\n{reseñas.get(nombre)}')
                else:
                    print ('+--------------------------')
                    print ('El libro no tiene reseña')
                    print ('+-------------------')
        else:
            print ('+-------------------------------')
            print ('El libro no esta registrado')
            print ('+-------------------')
         
        input()
   
    elif eleccion == 2:

        #!haciendo breve opinion acerca del libro 

        print ('+------------------------------')
        libro = input('¿Nombre del libro?:')
        print ('+-------------------')
       
        if reseñas.get(libro) == None:
            print ('')
            reseña = input('Escriba su reseña:')
            print ('')
            reseñas[libro] = reseña
        else:
            print('')
            print('Este libro ya posee una reseña ¿Desea cambiarla?')
            print('')
            eleccion2 = int(input('1 = si : 0 = No: '))
            if eleccion2 == 1:
                reseña = input('Escriba su reseña:')
                reseñas[libro] = reseña
            else:
                return '+----------------\n''¡Gracias!''+----------------\n'
 
def catalogo ():

    #!muestra todos los libros del archivo

    dataLibros = extraccionDatos()
    for i in dataLibros:
        nombreLibro, autor, generos, precio = i.strip().split('; ')
        print(f'\nNombre: {nombreLibro}\nAutor: {autor}\nGeneros: {generos}\nPrecio: {precio}\n')
    input()  
 
def eliminarLibro():

    #!elminacion de libros

    dataLibros = extraccionDatos()
    archivo = open('archivo.txt', 'w')
    print('+---------------------------------------------------------')
    libroBuscado = input('Ingrese el nombre del libro que desea eliminar: ')
    print ('-------------------------------------------')
    for i in dataLibros:
        if libroBuscado in i:
            dataLibros.remove(i)
            for j in dataLibros:
                archivo.write(j)
            break
    archivo.close()
     
while True:

    #!menu de opciones

    system('cls')
    dataLibros.clear()
    print('\n+---+---+---+---+---+---+---+---+---+---+\n| B | i | b | l | i | o | t | e | c | a |\n+---+---+---+---+---+---+---+---+---+---+\n')
    print('+------------------------------------------+')
    print('Opcion 1: Comprar/Buscar Libro')
    print('Opcion 2: Agregar Libro')
    print('Opcion 3: Eliminar Libro')
    print('Opcion 4: Catalogo')
    print('Opcion 5: Reseñas')
    print('Opcion 6: Ir al carrito')
    print('Opcion 7: Salir')
    print('+------------------------------------------+')
    opcion = int(input ('\nElegir Opcion: '))
 
    if opcion == 1:
        buscarLibro()
    elif opcion == 2:
        agregarlibro ()
    elif opcion == 3:
        eliminarLibro()
    elif opcion == 4:
        catalogo()
    elif opcion == 5:
        reseña()
    elif opcion == 6:
        carroActivo()
    elif opcion == 7:
        break
