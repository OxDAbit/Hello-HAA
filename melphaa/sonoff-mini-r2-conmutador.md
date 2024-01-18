# Control luz en un circuito conmutado con Sonoff Mini R2

<img src="https://templates.blakadder.com/assets/device_images/sonoff_MINIR2.webp" alt="Sonoff-Mini-R2" width="450"/>

> [!NOTE]
> El conexionado del dispositivo para _flashearlo_ se encuentra definido en la [guía Sonoff](../docs/sonoff_pinout.md)
>
> La guía para _flashear_ el dispositivo es [Flasheo HAA](../docs/flash_haa.md)
>
> Información del dispositivo [blakadder](https://templates.blakadder.com/sonoff_MINIR2.html)

## Control de un Interruptor / Bombilla / Enchufe

El _script_ adjunto se define para gestionar un interruptor, bombilla o enchufe en un circuito con un sólo interruptor o con interruptores conmutados.

> [!NOTE]
> Link [blakadder](https://templates.blakadder.com/sonoff_MINIR2.html)

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c":{"io":[[[12,13],2],[[0,4],6,1]],"l":13,"n":"device-hostname","b":[[0,5]]},"a":[{"0":{"r":[[12]]},"1":{"r":[[12,1]]},"b":[[0],[4],[4,0]],"s":0}]}
```

### Descripción del _script_

```json
{
  "c": {
    "io": [                   // Configuración de los GPIO's
      [[12, 13], 2],          // Se seleccionan los GPIO 12 y 13 como pines de salida
      [[0, 4], 6, 1]          // Se seleccionan los GPIO 0 y 4 como pines de entrada con la resistencia de pull-up interna habilitada y señal invertida
    ],
    "l": 13,                  // Se selecciona el GPIO 13 como led de estado del dispositivo
    "n": "device-hostname",   // Hostname del dispositivo
    "b": [[0, 5]]             // Se selecciona el GPIO 0 para activar el modo setup tras mantener pulsado el botón 8 segundos (opción 5)
  },
  "a": [
    {                         // Como no se espifica la variable "t" (tipo de servicio), se configura como un accesorio del tipo switch (valor por defecto)
      "0": {                  // Configuración acción cuando el switch de Homekit está a OFF
        "r": [[12]]           // Se cambia el estado a OFF del relé conectado a la GPIO 12
      },
      "1": {                  // Configuración acción cuando el switch de Homekit está a ON
        "r": [[12, 1]]        // Se cambia el estado a ON del relé conectado a la GPIO 12
      },
      "b": [                  // Configuración de los botones, el cual debe ser una array
        [0],                  // Primer botón conectado al GPIO 0 como "pulsación simple" (valor por defecto al no estar especificado)
        [4],                  // Segundo botón conectado al GPIO 4 como "pulsación simple" (valor por defecto al no estar especificado)
        [4, 0]                // Tercer botón conectado al GPIO 4 (al igual que el segundo) como "pulsación simple" invertida (valor opuesto al tipo 1)
      ],
      "s": 0                  // Estado inicial apagado
    }
  ]
}
```
