salario_actual = float(input("Ingrese el salario actual del empleado: "))
incremento = 0.08  # 8%
descuento = 0.025  # 2.5%
nuevo_salario = salario_actual * (1 + incremento) * (1 - descuento)
print(f"El nuevo salario es: ${nuevo_salario:.2f}")