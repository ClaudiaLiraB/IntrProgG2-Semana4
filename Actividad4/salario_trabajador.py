nombre_trabajador = input("Ingrese el nombre del trabajador: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
precio_por_hora = float(input("Ingrese el precio que cobra por hora: "))
sueldo_bruto = horas_trabajadas * precio_por_hora
descuento_renta = sueldo_bruto * 0.05  # 5% de impuesto
salario_neto = sueldo_bruto - descuento_renta
print(f"Nombre del trabajador: {nombre_trabajador}")
print(f"Sueldo bruto: ${sueldo_bruto:.2f}")
print(f"Descuento de renta (5%): ${descuento_renta:.2f}")
print(f"Salario a pagar: ${salario_neto:.2f}")