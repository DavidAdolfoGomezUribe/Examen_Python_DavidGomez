from menuDesing.menuDesing import hello

import time


def main():
    while True:
        try:
    
            print(""" 
            
    ---------------------------------------------------
                    CALCULADORA DE IMPUESTOS
    ---------------------------------------------------
    Seleccione una opción:
    1. Calcular impuesto sobre un producto o servicio
    2. Ver lista de tipos de impuestos
    3. Salir
    ---------------------------------------------------

    """)
            selector = int(input("    Seleccione una opcion (1-2-3): "))

            if selector == 1:
                pass
            elif selector == 2:
                pass
            elif selector == 3:
                break
            else:
                print("    Seleccione una opcion valida")
                time.sleep(1)
            
            
        except ValueError:
            pass
        except KeyboardInterrupt:
            pass



main()