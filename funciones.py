productos = {
    '001HD': ['HP', 15.6, '8GB', 'DD', '1TB', 'Intel Core i5', 'Nvidia GTX1050'],
    '002HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    '003HD': ['ASUS', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    '004HD': ['Acer', 15.6, '8GB', 'DD', '1TB', 'Intel Core i3', 'Graficos Integrados'],
    '005HD': ['MSI', 17, '32GB', 'NVME M.2', '2TB', 'AMD Ryzen 9', 'Nvidia RTX5090']
}

stock = {
    '001HD': [449990,20], '002HD': [299990,20],
    '003HD': [679990,10], '004HD': [399990,20],'005':[1199990,5]
}

def menu():
    print("~~Bienvenido a Pybooks~~")
    print("---Menu Principal---")
    print("1) Stock por marca.")
    print("2) Busqueda por precio.")
    print("3) Actualizar precio.")
    print("4) Salir.")

def stock_marca(stock):
    marca_a_buscar = input("Ingrese marca a buscar: ").upper()
    for id_producto, info_producto in productos.items():
        marca = info_producto[0].upper()
        if marca == marca_a_buscar:
            cantidad = stock[id_producto]
            print(f"El stock es de {cantidad[1]}")

def busqueda_precio(p_min,p_max):
    
    lista = []
    p_min = int(input("Ingrese el precio minimo: "))
    p_max = int(input("Ingrese el precio maximo: "))
    
    for modelo, datos in productos.items():
        precio = stock.get()



def busqueda_precio(p_min,p_max):
    
    while True:
        try:
            p_min = int(input("Ingrese el precio mínimo: "))
            p_max = int(input("Ingrese el precio máximo: "))
            break
        except ValueError:
            print("Debe ingresar valores enteros!!")
    
    lista = []
    
    for modelo, datos in productos.items():
        precio = stock.get(modelo, [None, None])[0]
        cantidad = stock.get(modelo, [None, None])[1]
        
        if precio is not None and p_min <= precio <= p_max and cantidad > 0:
            modelo_formateado = f"{datos[0]}--{modelo}"
            lista.append(modelo_formateado)
    if lista:
        lista.sort()
        print(f"Modelos en el rango de precio entre {p_min} y {p_max}:")
        for modelo in lista:
            print(f"- {modelo}")
    else:
        print("No hay notebooks en ese rango de precios.")

def actualizar_precio(modelo,p):
    while True:
        lista = []
        if modelo in productos.values():
            p.append()
        otro = input("Desea actualizar otro precio (s/n)?: ").lower()
        if otro == "no":
            break