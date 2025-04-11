precio1 = float(input("Ingrese el precio del producto 1: "))
precio2 = float(input("Ingrese el precio del producto 2: "))
precio3 = float(input("Ingrese el precio del producto 3: "))
subtotal = precio1 + precio2 + precio3
iva = subtotal * 0.15  # 15% IVA
total_pagar = subtotal + iva
print(f"Subtotal: ${subtotal:.2f}")
print(f"IVA (15%): ${iva:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")