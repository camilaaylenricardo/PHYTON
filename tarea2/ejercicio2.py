productos = {"manzana": 1.2, "naranja": 0.8, "plátano": 1.0}

def calcular_total(productos_seleccionados):
    total = 0
    for producto, cantidad in productos_seleccionados.items():
        if producto in productos:
            total += productos[producto] * cantidad
    return total

productos_seleccionados = {"manzana": 3, "naranja": 2}

total_a_pagar = calcular_total(productos_seleccionados)
print(f"Total a pagar: {total_a_pagar}")