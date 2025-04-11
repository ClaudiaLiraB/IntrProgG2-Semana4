nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
descuento = precio_producto * (porcentaje_descuento / 100)
precio_final = precio_producto - descuento
print(f"Producto: {nombre_producto}")
print(f"Precio final: ${precio_final:.2f}")