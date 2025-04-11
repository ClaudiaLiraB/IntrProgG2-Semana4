total_alumnos = int(input("Ingrese el total de alumnos: "))
mujeres = int(input("Ingrese el número de mujeres: "))
varones = total_alumnos - mujeres
porcentaje_mujeres = (mujeres / total_alumnos) * 100
porcentaje_varones = (varones / total_alumnos) * 100
print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
print(f"Porcentaje de varones: {porcentaje_varones:.2f}%")