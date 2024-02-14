# ESP01S Relay 1 Channel

<img src="https://templates.blakadder.com/assets/device_images/ESP-01S-Relay-v5.webp" alt="ESP01S-Relay" width="450"/>

> [!NOTE]
> La guía para _flashear_ el dispositivo es [Flasheo HAA](../docs/flash_haa.md)
>
> Información del dispositivo [blakadder](https://templates.blakadder.com/ESP-01S-Relay-v5.html)

## Control de un relé

El _script_ adjunto se define para gestionar el ESP01 como un activador de un relé el cual puede gestionar una bombilla, enchufe,...

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c":{"io":[[[0,1],2],[[3],6,1]],"l":1,"n":"device-hostname","b":[[3,5]]},"a":[{"0":{"r":[[0]]},"1":{"r":[[0,1]]},"b":[[0]],"s":0}]}
```

### Descripción del _script_

```json
{
  "c": {
    "io": [                   // Configuración de los GPIO's
      [[0, 1], 2],            // Se seleccionan los GPIO 12 y 13 como pines de salida
      [[3], 6, 1]             // Se selecciona el GPIO 3 como pin de entrada con la resistencia de pull-up interna habilitada y señal invertida
    ],
    "l": 1,                   // Se selecciona el GPIO 13 como led de estado del dispositivo
    "n": "device-hostname",   // Hostname del dispositivo
    "b": [[3, 5]]             // Se selecciona el GPIO 0 para activar el modo setup tras mantener pulsado el botón 8 segundos (opción 5)
  },
  "a": [
    {                         // Como no se espifica la variable "t" (tipo de servicio), se configura como un accesorio del tipo switch (valor por defecto)
      "0": {                  // Configuración acción cuando el switch de Homekit está a OFF
        "r": [[0]]            // Se cambia el estado a OFF del relé conectado a la GPIO 12
      },
      "1": {                  // Configuración acción cuando el switch de Homekit está a ON
        "r": [[0, 1]]         // Se cambia el estado a ON del relé conectado a la GPIO 12
      },
      "b": [                  // Configuración de los botones, el cual debe ser una array
        [0]                   // Primer botón conectado al GPIO 0 como "pulsación simple" (valor por defecto al no estar especificado)
      ],
      "s": 0                  // Estado inicial apagado
    }
  ]
}
```
