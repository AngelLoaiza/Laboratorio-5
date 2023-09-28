importe_total_vendido = float(input("Ingrese el importe total vendido del mes: S/. "))
cantidad_hijos_escolar = int(input("Ingrese la cantidad de hijos en edad escolar: "))

comision = importe_total_vendido * 0.075

bonificacion_hijos = cantidad_hijos_escolar * 50

sueldo_basico = 600
sueldo_bruto = sueldo_basico + comision + bonificacion_hijos

descuento = sueldo_bruto * 0.11

sueldo_neto = sueldo_bruto - descuento

# Mostrar los resultados
print(f"Comisión: S/. {comision:.2f}")
print(f"Bonificación por hijos en edad escolar: S/. {bonificacion_hijos:.2f}")
print(f"Sueldo Bruto: S/. {sueldo_bruto:.2f}")
print(f"Descuento (11%): S/. {descuento:.2f}")
print(f"Sueldo Neto: S/. {sueldo_neto:.2f}")
