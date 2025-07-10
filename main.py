from funciones import menu,stock_marca,busqueda_precio, actualizar_precio

stock = {
    '001HD': [449990,20], '002HD': [299990,20],
    '003HD': [679990,10], '004HD': [399990,20],'005':[1199990,5]
}


while True:
    try:
        
        menu()
        opc = int(input("Ingrese una opcion: "))
        
        if opc == 1:
            stock_marca(stock)
        elif opc == 2:
            p_min = int(input("Ingrese el precio minimo: "))
            p_max = int(input("Ingrese el precio maximo: "))
            busqueda_precio(p_min,p_max)
        elif opc == 3:
            modelo = input("Ingrese un modelo a actualizar: ")
            p = int(input("Ingrese el nuevo precio: "))
            print("Precio Actualizado!!!")
            actualizar_precio(modelo,p)
        elif opc == 4:
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida, intente nuevamente")
    except ValueError:
        print("Debe ingresar solo un numero, intente nuevamente.")