precio_actual_gaseosa = float(input("Ingrese el precio actual de la gaseosa (3 litros): S/. "))
cantidad_unidades_adquiridas = int(input("Ingrese la cantidad de unidades adquiridas: "))

nuevo_precio_gaseosa = precio_actual_gaseosa * 0.95

importe_compra = nuevo_precio_gaseosa * cantidad_unidades_adquiridas

descuento = importe_compra * 0.07

importe_a_pagar = importe_compra - descuento

cantidad_caramelos_obsequio = cantidad_unidades_adquiridas * 2

print(f"Nuevo Precio de la Gaseosa (3 litros): S/. {nuevo_precio_gaseosa:.2f}")
print(f"Importe de la Compra: S/. {importe_compra:.2f}")
print(f"Descuento (7%): S/. {descuento:.2f}")
print(f"Importe a Pagar: S/. {importe_a_pagar:.2f}")
print(f"Caramelos de Obsequio: {cantidad_caramelos_obsequio} unidades")