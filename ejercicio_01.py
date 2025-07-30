print("Bienvenido al programa")
producto={}
cantidad=int(input("Ingrese la cantidad de productos que desea agregar: "))
for i in range(cantidad):
    print(f"PRODUCTO NO.{i+1}")
    code=input("Ingrese el código del producto: ")
    name=input("Ingrese el nombre del producto: ")
    categoria=input("Ingrese la categoria del producto: ")
    size=input("Ingrese la talla del producto (S,M,L,XL): ")
    price=int(input("Ingrese el precio unitario del producto: "))
    stock=int(input("Ingrese la cantidad en stock:"))