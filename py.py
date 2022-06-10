from os import system

dataLibros = []
carrito = {}

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

def carro(a, b):
    if carrito.get(a) == None:   
        carrito[a] = b
    
    desea = int(input('Desea seguir comprando? (0 para no / 1 para si): '))
    if desea == 1:
        buscarLibro()

def carroActivo():
    total = 0
    for i in carrito.values():
        total += i
    compra = int(input('Comprar los libros seleccionados? (0 para no / 1 para si): '))
    if compra == 1:
        print('\n****** TICKET DE COMPRA ******')
        for i, j in carrito.items():
            print(f'\n{i}: ${j}')
        print(f'El total de su compra es: ${total}')
        input()
        
def buscarLibro():
    archivo = open('archivo.txt', 'a+')
    print ('1: Buscar por Autor')
    print ('2: Buscar por Nombre')
    print ('3: Buscar por Genero')
    eleccion = int (input ('Elija una opcion: '))
 
    if eleccion == 1:  
 
        archivo = open('archivo.txt', 'a+')
        print ('1: Buscar por Autor')
        print ('2: Buscar por Nombre')
        print ('3: Buscar por Genero')
        eleccion = int (input ('Elija una opcion: '))
    
        if eleccion == 1:
            general = 'Autor'
        elif eleccion == 2:
            general = 'Nombre'
        elif eleccion == 3:
            general = 'Genero'
    
        variable = input(f'\nIntroducir {general} del libro: ')

        archivo.seek(0)
        for i in archivo:
            if variable in i:
                nombreLibro, autor, generos, precio = i.strip().split('; ')
                print(f'\nNombre: {nombreLibro}\nAutor: {autor}\nGeneros: {generos}\nPrecio: {precio}\n')
                precioNum = int(precio)
                carrito = int(input('Desea agregar al carrito este libro? (0 para no / 1 para si): '))
                if carrito == 1:
                    carro(nombreLibro, precioNum)
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
    
def reseña():
    archivo = open('archivo.txt', 'a+')
    print ('1) Buscar Reseña')
    print ('2) Agregar Reseña')
    eleccion = int(input('¿Eleccion?:'))
 
    if eleccion == 1:
        nombre = input('Nombre del libro: ')
 
        archivo.seek(0)
        for i in archivo:
            if nombre in i:
                nombreLibro, autor, generos, precio, reseña = i.strip().split('; ')
                print (f'Reseñas: {reseña}')
                 
    elif eleccion == 2:
        reseña = input('Escriba su reseña:')
        libro = input('¿Nombre del libro?:')

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
    print('Opcion 2: Agregar Libro, para vender')
    print('Opcion 3: Eliminar Libro')
    print('Opcion 4: Catalogo')
    print('Opcion 5: Reseñas')
    print('Opcion 6: Puntuar Libro')
    print('Opcion 7: Ir al carrito')
    print('Opcion 8: Salir')
    print('------------------------------------------')
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
    elif opcion == 7:
        carroActivo()
    elif opcion == 8:
        break

