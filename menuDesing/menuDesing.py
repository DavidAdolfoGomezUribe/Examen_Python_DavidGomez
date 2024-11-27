from logic.logicMt import tax,specialTax,localTax, personalTax
import pandas as pd
import os
import time 

def menuOne():
    
    priceArray = []
    priceTaxArray =[]
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
                while True:
                    selector = int(input("    :"))
                    
                    if selector == 1:
                        
                        taxTotal = tax(price)
                        
                        priceArray.append(taxTotal)
                        priceTaxArray.append({"IVA(10%)":taxTotal})
                        break
                        
                    elif selector == 2:
                        specialTotal = specialTax(price)
                        
                        priceArray.append(specialTotal)
                        priceTaxArray.append({"Impuesto Especial (5%)": specialTotal})
                        break
                        
                    elif selector == 3:
                        
                        localTotal = localTax(price)
                        
                        priceArray.append(localTotal)
                        priceTaxArray.append({"Impuesto Local (8%)":localTotal})
                        break
                                                            
                    elif selector == 4:
                        personal =float(input("    Ingrese el valor del impuesto (en porcentaje) si seleccionó -Otro-: "))
                        personalTotal = personalTax(price,personal)
                        
                        priceArray.append(personalTotal)
                        priceTaxArray.append({f"Otro ({personal})":personalTotal})
                        break
                    else :
                        print("    Elija una opcion valida")
                    
            
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
                elif solution == 2:
                    break
            
            
            taxTotal = sum(priceArray)

            priceTaxArray.append({"precio base ": price ,"total + impuestos": taxTotal})
            
            dicc = pd.DataFrame(priceTaxArray)
            
            print(f"""
                  
    ---------------------------------------------------
                RESULTADO DEL CÁLCULO
    ---------------------------------------------------
    Precio base: {priceArray[0]}
    Impuesto(s): 
    """)
    
    
            print(f"""{dicc}""")                
                 
    
            print(f""" 
    Total con impuestos:{taxTotal} pesos
    """)


            print(""" 
    ¿Desea hacer otro cálculo?
    1. Sí
    2. No (Regresa al menú principal)
    3. Guardar reporte y salir
    ---------------------------------------------------""")
            
            awnser = int(input("    :"))
            if awnser == 1:
                
                priceArray = []
                priceTaxArray =[]
                
    
                pass
            
            elif awnser == 2:
                break
            
            
            elif awnser == 3:
                
                contador = 1
                
                os.makedirs("databases/", exist_ok=True)
                
                
                output_path = os.path.join("databases/", "Report.xlsx")
                while os.path.exists(output_path):
                    contador += 1
                    output_path = os.path.join("databases/", f"Report{contador}.xslx")
                
                
                dicc.to_excel(output_path, sheet_name="Hoja1", index=False) 
                
                print(f"\n    Reporte guardado exitosamente en {output_path}")
                
                time.sleep(1)
                
                break
            
            
            else:
                print("    Seleccione una opcion valida")
            
            
        except ValueError:
            pass
        except KeyboardInterrupt:
            pass
        
        
        
        
        
        
        
        
        
def menuTwo():
    
            try:
                print(f""" 
    ---------------------------------------------------
                TIPOS DE IMPUESTOS
    ---------------------------------------------------
    1. IVA (10%)
    2. Impuesto Especial (5%)
    3. Impuesto Local (8%)
    4. Otro (Personalizado)

    ¿Desea calcular un impuesto ahora?
    1. Sí (Regresa al cálculo)
    2. No (Regresa al menú principal)
    ---------------------------------------------------
                      
                      """)                
                selector = int(input("    :"))
                
                if selector == 1 :
                    menuOne()
                elif selector == 2 :
                    pass
                else:
                    print("""    Seleccione una opcion valida""")
            
            
            except ValueError:
                pass
            except KeyboardInterrupt:
                pass
        
                
            
        
        # last line of code