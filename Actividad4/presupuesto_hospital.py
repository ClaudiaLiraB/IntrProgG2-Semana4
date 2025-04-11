presupuesto_total = float(input("Ingrese el presupuesto anual del hospital: "))
presupuesto_urgencias = presupuesto_total * 0.37
presupuesto_pediatria = presupuesto_total * 0.42
presupuesto_traumatologia = presupuesto_total * 0.21
print(f"Presupuesto para Urgencias: ${presupuesto_urgencias:.2f}")
print(f"Presupuesto para Pediatría: ${presupuesto_pediatria:.2f}")
print(f"Presupuesto para Traumatología: ${presupuesto_traumatologia:.2f}")