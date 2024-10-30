if __name__ == '__main__':
    nombre = (input("Proporciona un nombre: "))
    fecha_cum = " "
    match nombre:
        case "Veronica":fecha_cum = "8 de Julio"
        case "Francisco": fecha_cum = "27 de Septiembre"
        case "Wendoly":fecha_cum = "27 de Septiembre"
        case "Amberley":fecha_cum = "26  de Junio"
        case "Gustavo":fecha_cum = "26 de Agosto"

print(f"El dia de cumpleaaños es: {fecha_cum}")
