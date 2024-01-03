# Sonoff Basic R4

![basic-r4](https://templates.blakadder.com/assets/device_images/sonoff_BASICR4.webp)

## Control de un Interruptor / Bombilla / Enchufe

El _script_ adjunto se define para gestionar un interruptor, bombilla o enchufe en un circuito "Magic Switch" de Sonoff gestionando un unico interruptor.

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c":{"io":[[[4,6],2],[[5],6,0,2,1,2000],[[9],6]],"l":6,"n":"device-hostname","b":[[9,5]]},"a":[{"0":{"r":[[4]]},"1":{"r":[[4,1]]},"b":[[5],[9]]}]}
```

### Descripción del script

```json
{
  "c": {
    "io": [                   // Configuración de los GPIO's
      [[4, 6], 2],            // Se seleccionan los GPIO 4 y 6 como pines de salida
      [[5], 6, 0, 2, 1, 2000],// Se selecciona el GPIO 5 como:
                              //  - Pin exclusivo de entrada (6)
                              //  - Resistencia pull-up y pull-down deshabilitadas  (0)
                              //  - Entrada normal con detección de pulsos (2)
                              //  - Filtro del botón configurado a nivel "soft" para el sistema anti rebote tras activar/desactivar el interruptor/conmutador
                              //  - Detección máxima del pulso de 2000 ms
      [[9], 6]                // Se selecciona el GPIO 9 como pin exclusivo de entrada con entrada binaria para interruptor/conmutador
    ],
    "l": 6,                   // Se selecciona el GPIO 6 como led de estado del dispositivo
    "n": "device-hostname",   // Hostname del dispositivo
    "b": [[9, 5]]             // Se selecciona el GPIO 9 para activar el modo setup tras mantener pulsado el botón 8 segundos (opción 5)
  },
  "a": [
    {                         // Como no se espifica la variable "t" (tipo de servicio), se configura como un accesorio del tipo switch (valor por defecto)
      "0": {                  // Configuración acción cuando el switch de Homekit está a OFF
        "r": [[4]]            // Se cambia el estado a OFF del relé conectado a la GPIO 4 hasta que vuelva a activarse
      },
      "1": {                  // Configuración acción cuando el switch de Homekit está a ON
        "r": [[4, 1]]         // Se cambia el estado a ON del relé conectado a la GPIO 4 hasta que vuelva a activarse
      },
      "b": [                  // Configuración de los botones, el cual debe ser una array
        [5],                  // Primer botón conectado al GPIO 5 como "pulsación simple" (valor por defecto al no estar especificado)
        [9]                   // Segundo botón conectado al GPIO 9 como "pulsación simple" (valor por defecto al no estar especificado)
      ]
    }
  ]
}
```
