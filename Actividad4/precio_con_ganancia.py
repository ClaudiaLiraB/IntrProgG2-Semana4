precio_compra = float(input("Ingrese el precio de compra del artículo: "))
ganancia = 0.30  # 30%
precio_venta = precio_compra * (1 + ganancia)
print(f"Precio de venta para obtener 30% de ganancia: ${precio_venta:.2f}")