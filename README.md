# **Menú Principal: Calculadora de Impuestos**

```bash
---------------------------------------------------
                CALCULADORA DE IMPUESTOS
---------------------------------------------------
Seleccione una opción:
1. Calcular impuesto sobre un producto o servicio
2. Ver lista de tipos de impuestos
3. Salir
---------------------------------------------------
```

------

## **Menú para Calcular Impuesto**

Si el usuario selecciona la opción **1** (Calcular impuesto):

```bash
---------------------------------------------------
             CÁLCULO DE IMPUESTOS
---------------------------------------------------
Ingrese el precio base del producto o servicio:
> [Usuario ingresa valor]
---------------------------------------------------
Seleccione el tipo de impuesto:
1. IVA (10%)
2. Impuesto Especial (5%)
3. Impuesto Local (8%)
4. Otro (permite ingresar una tasa personalizada)
---------------------------------------------------
Ingrese el valor del impuesto (en porcentaje) si seleccionó "Otro":
> [Usuario ingresa valor o selecciona uno predefinido]
---------------------------------------------------
¿Desea agregar otro impuesto?
1. Sí
2. No
---------------------------------------------------
```

------

## **Resultado Final**

Una vez que el cálculo se ha realizado, el programa muestra los resultados:

```bash
---------------------------------------------------
                RESULTADO DEL CÁLCULO
---------------------------------------------------
Precio Base: $[valor]
Impuesto(s):
- IVA (10%): $[valor del IVA]
- Impuesto Especial (5%): $[valor del impuesto especial]
Total con impuestos: $[total]

¿Desea hacer otro cálculo?
1. Sí
2. No (Regresa al menú principal)
---------------------------------------------------
```

------

## **Menú para Ver Lista de Impuestos**

Si el usuario selecciona la opción **2** (Ver lista de impuestos):

```bash
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
```

------

## **Salir del Programa**

Si el usuario selecciona la opción **3** (Salir):

```bash
---------------------------------------------------
               ¡Gracias por usar la Calculadora!
---------------------------------------------------
```



# **Flujo del Menú Principal:**

1. Inicio
   - El programa muestra el menú principal.
   - El usuario debe elegir una opción:
     - Opción **1**: Calcular impuesto sobre un producto o servicio.
     - Opción **2**: Ver lista de tipos de impuestos.
     - Opción **3**: Salir del programa.

------

## **Flujo para Opción 1: Calcular Impuesto sobre un Producto o Servicio**

1. **Ingreso del precio base**
   - El programa solicita al usuario que ingrese el precio base del producto o servicio.
     - Ejemplo: "Ingrese el precio base del producto o servicio:"
2. **Selección del tipo de impuesto**
   - El usuario elige el tipo de impuesto:
     - Opción **1**: IVA (10%)
     - Opción **2**: Impuesto Especial (5%)
     - Opción **3**: Impuesto Local (8%)
     - Opción **4**: Otro (permite ingresar una tasa personalizada)
3. **Ingreso del valor del impuesto (si seleccionó "Otro")**
   - Si el usuario seleccionó "Otro", se le solicita que ingrese el valor del impuesto en porcentaje.
     - Ejemplo: "Ingrese el valor del impuesto (en porcentaje):"
4. **¿Agregar otro impuesto?**
   - El programa pregunta al usuario si desea agregar otro impuesto:
     - Opción **1**: Sí (permite agregar otro impuesto).
     - Opción **2**: No (termina el cálculo y muestra el resultado).
5. **Cálculo del impuesto y total**
   - El programa calcula el monto del impuesto basado en el precio base y las tasas seleccionadas.
   - Muestra los resultados:
     - Precio Base
     - Impuestos aplicados (detallados)
     - Total con impuestos incluidos.
6. **¿Realizar otro cálculo?**
   - Después de mostrar los resultados, el programa pregunta si el usuario desea hacer otro cálculo:
     - Opción **1**: Sí (regresa al inicio de la opción para calcular otro impuesto).
     - Opción **2**: No (regresa al menú principal).

------

## **Flujo para Opción 2: Ver Lista de Tipos de Impuestos**

1. **Mostrar lista de impuestos disponibles**
   - El programa muestra los tipos de impuestos disponibles para el cálculo:
     - IVA (10%)
     - Impuesto Especial (5%)
     - Impuesto Local (8%)
     - Otro (personalizado)
2. **¿Realizar un cálculo ahora?**
   - El programa pregunta si el usuario quiere hacer un cálculo de impuesto ahora:
     - Opción **1**: Sí (regresa a la opción de calcular impuesto).
     - Opción **2**: No (regresa al menú principal).

------

## **Flujo para Opción 3: Salir**

1. Salir del programa
   - El programa muestra un mensaje de despedida y finaliza la ejecución.
     - Ejemplo: "¡Gracias por usar la Calculadora de Impuestos. ¡Hasta luego!"