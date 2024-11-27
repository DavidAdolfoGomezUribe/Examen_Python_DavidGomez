def menuOne():
    
    while True:
        try:
    
    
            print(f""" 
          
    ---------------------------------------------------
                CÁLCULO DE IMPUESTOS
    ---------------------------------------------------
    Ingrese el precio base del producto o servicio:
    """)
    
            price = float(input("    :"))
            
            print("""
    ---------------------------------------------------
    Seleccione el tipo de impuesto:
    1. IVA (10%)
    2. Impuesto Especial (5%)
    3. Impuesto Local (8%)
    4. Otro (permite ingresar una tasa personalizada)
    """)
            selector = int(input("    :"))
            
            if selector == 1:
                        
                
                
                
            elif selector == 2:
                pass
            elif selector == 3:
                pass
            
            elif selector == 4:
                print("Ingrese el valor del impuesto (en porcentaje) si seleccionó -Otro-: ")
                
                
    
            print("""
    ---------------------------------------------------
    
    > [Usuario ingresa valor o selecciona uno predefinido]
    ---------------------------------------------------
    ¿Desea agregar otro impuesto?
    1. Sí
    2. No
    ---------------------------------------------------
          """)
            
            
            
            
        except ValueError:
            pass
        except KeyboardInterrupt:
            pass