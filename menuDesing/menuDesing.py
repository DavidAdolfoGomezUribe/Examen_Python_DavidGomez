from logic.logicMt import tax,specialTax,localTax, personalTax


def menuOne():
    
    priceArray = []
    while True:
        try:
    
    
            print(f""" 
          
    ---------------------------------------------------
                CÁLCULO DE IMPUESTOS
    ---------------------------------------------------
    Ingrese el precio base del producto o servicio:
    """)
    
            price = int(input("    :"))
            
            priceArray.append( price)
                
            while True:    
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
                    
                    ivaTotal = tax(price)
                    
                    priceArray.append(ivaTotal)
                    break
                    
                elif selector == 2:
                    specialTotal = specialTax(price)
                    
                    priceArray.append(specialTotal)
                    break
                    
                    
                elif selector == 3:
                    
                    localTotal = localTax(price)
                    
                    priceArray.append(localTotal)
                    break
                
                elif selector == 4:
                    personal =float(input("    Ingrese el valor del impuesto (en porcentaje) si seleccionó -Otro-: "))
                    personalTotal = personalTax(price,personal)
                    
                    priceArray.append(personalTotal)
                    break
                    
        
                print("""
    
    ---------------------------------------------------
    ¿Desea agregar otro impuesto?
    1. Sí
    2. No
    ---------------------------------------------------
          """)  
                solution = int(input("    :"))
                
                if solution == 1:
                    pass
                if solution == 2:
                    break
            
            
            taxTotal = sum(priceArray)
            print(f"""
                  
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Precio base {priceArray[0]}
    Impuesto(s):
    - iva (10%){priceArray}
    - Impuesto Especial (5%): $[valor del impuesto especial]
    Total con impuestos:{taxTotal}
    """)


            print(""" 
    ¿Desea hacer otro cálculo?
    1. Sí
    2. No (Regresa al menú principal)
    ---------------------------------------------------""")
            
            awnser = int(input("    :"))
            if awnser == 1:
                pass
            elif awnser == 2:
                break
            else:
                print("    Seleccione una opcion valida")
            
            
            
            
            
            
            
            
            
        except ValueError:
            pass
        except KeyboardInterrupt:
            pass