tiempo_lunes = float(input("Ingrese el tiempo del lunes: "))
tiempo_miercoles = float(input("Ingrese el tiempo del miércoles: "))
tiempo_viernes = float(input("Ingrese el tiempo del viernes: "))
tiempo_promedio = (tiempo_lunes + tiempo_miercoles + tiempo_viernes) / 3
print(f"Tiempo promedio de carrera: {tiempo_promedio:.2f} (unidades de tiempo)")