from os import system

dataLibros = []

def extraccionDatos():
    data = ''
    archivo = open('archivo.txt', 'a+')
    archivo.seek(0)
    data = archivo.readlines()
    archivo.close()
    return data

def inscripcion(nombre):
    for i in extraccionDatos():
        if nombre in i:
            return True

def reseña ():
    print ('1) Buscar Reseña')
    print ('2) Agregar Reseña')
    eleccion = int(input('¿Eleccion?:'))

    if eleccion == 1:
        nombre_libro = input ('Nombre del libro:')
        for i in x.keys():
            if nombre_libro == i:
                print (nombre_libro, x.values())
              
    elif eleccion == 2:

        reseña = input('Escriba su reseña:')
        libro = input('¿Nombre del libro?:')
        reseñas[libro] = reseña

def buscarlibro ():
    archivo = open('archivo.txt', 'a+')
    print ('1: Buscar por Autor')
    print ('2: Buscar por Nombre')
    print ('3: Buscar por Genero')
    print ('4: Buscar por Precio')
    eleccion = int (input ('Elija una opcion: '))
 
    if eleccion == 1:  
        nombreAutor = input ('Introducir nombre del autor: ')
 
        archivo.seek(0)
        for i in archivo:
            if nombreAutor in i:
                nombreLibro, autor, generos, precio = i.strip().split('; ')
                print(f'\nNombre: {nombreLibro}\nAutor: {autor}\nGeneros: {generos}\nPrecio: {precio}\n')
            input()
 
    elif eleccion == 2:
        nombredelLibro = input ('Introducir nombre del libro: ')
 
        archivo.seek(0)
        for i in archivo:
            if nombredelLibro in i:
                nombreLibro, autor, generos, precio = i.strip().split('; ')
                print(f'\nNombre: {nombreLibro}\nAutor: {autor}\nGeneros: {generos}\nPrecio: {precio}\n')
            input()
 
    elif eleccion == 3:
        genero1 = input ('Introducir genero 1:')
        genero2 = input ('Introducir genero 2:')
        genero3 = input ('Introducir genero 3:')
 
        archivo.seek(0)
        for i in archivo:
            if genero1 in i:
                nombreLibro, autor, generos, precio = i.strip().split('; ')
                print(f'\nNombre: {nombreLibro}\nAutor: {autor}\nGeneros: {generos}\nPrecio: {precio}\n')
    archivo.close()
    
def agregarlibro ():
        archivo = open('archivo.txt', 'a+')
        nombre = input('Nombre del libro: ')
        dataLibros.append(nombre)
        dataLibros.append(input('Autor/es del libro: '))
        dataLibros.append(input('Genero/s del libro (si es nas de uno separarlo con ","): '))
        dataLibros.append(input ('Precio que al que quiere venderlo? '))
        
        if inscripcion(nombre):
            print('Su libro ya esta registrado, ingrese uno distinto')
            input()
        else:
            formato = '; '.join(dataLibros)
            archivo.write(formato + '\n')
            archivo.close() 
    
def catalogo ():
    dataLibros = extraccionDatos()
    for i in dataLibros:
        nombreLibro, autor, generos, precio = i.strip().split('; ')
        print(f'\nNombre: {nombreLibro}\nAutor: {autor}\nGeneros: {generos}\nPrecio: {precio}\n')
    input()   

def eliminarLibro():
    dataLibros = extraccionDatos()
    archivo = open('archivo.txt', 'w')
    libroBuscado = input('Ingrese el nombre del libro que desea eliminar: ')
    for i in dataLibros:
        if libroBuscado in i:
            dataLibros.remove(i)
            for j in dataLibros:
                archivo.write(j)
            break
    archivo.close()
        
while True:
    system('cls')
    dataLibros.clear()
    print('\n+---+---+---+---+---+---+---+---+---+---+\n| B | i | b | l | i | o | t | e | c | a |\n+---+---+---+---+---+---+---+---+---+---+\n')
    print('------------------------------------------')
    print('Opcion 1: Buscar Libro')
    print('Opcion 2: Comprar un libro')
    print('Opcion 3: Agregar Libro, para vender')
    print('Opcion 4: Eliminar Libro')
    print('Opcion 5: Catalogo')
    print('Opcion 6: Reseñas')
    print('Opcion 7: Puntuar Libro')
    print('Opcion 8: Salir')
    print('------------------------------------------')
    opcion = int(input ('\nElegir Opcion: '))

    if opcion == 1:
        buscarlibro()
    elif opcion == 2:
        #compraLibro()
        merca = 1
    elif opcion == 3:
        agregarlibro ()
    elif opcion == 4:
        eliminarLibro()
    elif opcion == 5:
        catalogo()
    elif opcion == 6:
        reseña()
    elif opcion == 7:
        hola = 1
    elif opcion == 8:
        break

