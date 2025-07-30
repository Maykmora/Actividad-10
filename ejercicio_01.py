print("Bienvenido al programa")
productos={}
cantidad=int(input("Ingrese la cantidad de productos que desea agregar: "))
for i in range(cantidad):
    print(f"PRODUCTO NO.{i+1}")
    while True:
        code=input("Ingrese el código del producto: ")
        if code in productos:
            print("El código ya esta registrado, intentelo de nuevo.")
        else:
            break
    name=input("Ingrese el nombre del producto: ")
    categoria=input("Ingrese la categoria del producto: ")
    size=input("Ingrese la talla del producto (S,M,L,XL): ")
    while True:
        price=int(input("Ingrese el precio unitario del producto: "))
        if price>0:
            break
        else:
            print("El precio debe ser mayor que 0, intente de nuevo.")

    while True:
        stock=int(input("Ingrese la cantidad en stock:"))
        if stock>0:
            break
        else:
            print("El stock debe ser mayor que 0, intente de nuevo.")

    productos[code]={
        "nombre":name,
        "categoria":categoria,
        "talla":size,
        "precio":price,
        "stock":stock
    }

print("\n--LISTA DE PRODUCTOS--")
contador=1
for code,datos in productos.items():
    print(f"\nProducto No.{contador}")
    print(f"\nCodigo: {code}")
    print(f"Nombre: {datos["nombre"]}")
    print(f"Categoria: {datos["categoria"]}")
    print(f"Talla: {datos["talla"]}")
    print(f"Precio: {datos["precio"]}")
    print(f"Stock: {datos["stock"]}")
    contador+=1

print("\n--BÚSQUEDA--")
search=input("Ingrese el código del producto que desea buscar: ")
if search in productos:
    print(f"Nombre: {productos[search]["nombre"]}")
    print(f"Categoria: {productos[search]["categoria"]}")
    print(f"Talla: {productos[search]["talla"]}")
    print(f"Precio: {productos[search]["precio"]}")
    print(f"Stock: {productos[search]["stock"]}")
else:
    print("Código no encontrado en el sistema")

print("\n--PRECIO INVENTARIO--")
suma=0
for code, datos in productos.items():
    i=datos["precio"]
    j=datos["stock"]
    total1=i*j
    suma+=total1
    print(f"{code}: Q.{i} X {j}= Q.{total1}")

print(f"\nEl precio total del inventario es Q.{suma}")

print("\n--PRODUCTOS POR CATEGORIA--")
