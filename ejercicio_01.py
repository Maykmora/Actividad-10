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
        if price>0:
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
    print(f"Producto No.{contador}")
    print(f"\nCodigo: {code}")
    print(f"Nombre: {datos["nombre"]}")
    print(f"Categoria: {datos["categoria"]}")
    print(f"Talla: {datos["talla"]}")
    print(f"Precio: {datos["precio"]}")
    print(f"Stock: {datos["stock"]}")
    contador+=1
