# Sonoff Mini R2

## Control de un Interruptor / Bombilla / Enchufe

El _script_ adjunto se define para gestionar un interruptor, bombilla o enchufe en un circuito con un sólo interruptor o con interruptores conmutados.

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c":{"io":[[[12,13],2],[[0,4],6,1]],"l":13,"n":"device-hostname","b":[[0,5]]},"a":[{"0":{"r":[[12]]},"1":{"r":[[12,1]]},"b":[[0],[4],[4,0]],"s":0}]}
```

### Descripción del script

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
    {
      "0": {                  // Configuración acción cuando el switch de Homekit está a OFF
        "r": [[12]]           // Relé conectado a la GPIO 12 con estado "0" (el valor por defecto, al no estar especificado es 0.)
      },
      "1": {                  // Configuración acción cuando el switch de Homekit está a ON
        "r": [[12, 1]]        // Relé conectado a la GPIO 12 con estado "1" (el valor por defecto, al no estar especificado es 0.)
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
