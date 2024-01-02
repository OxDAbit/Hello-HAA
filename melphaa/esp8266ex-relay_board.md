# ESP8266EX Relay Board 10A DC 7-30V

## Control del relé integrado en la PCB

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c": {"io": [[[4], 2],[[0], 6, 1]],"l": 13,"n": "device-hostname","b": [[0, 5]]},"a": [{"0": {"r": [[4]]},"1": {"r": [[4, 1]]},"b": [[0]],"s": 0}]}
```

### Descripción del script

```json
{
  "c": {
    "io": [                   // Configuración de los GPIO's
      [[4], 2],               // Se seleccionan los GPIO 4 como pines de salida
      [[0], 6, 1]             // Se seleccionan los GPIO 0 como el pin de entrada con la resistencia de pull-up interna habilitada y señal invertida
    ],
    "l": 13,                  // Se selecciona el GPIO 13 como led de estado del dispositivo
    "n": "device-hostname",   // Hostname del dispositivo
    "b": [[0, 5]]             // Se selecciona el GPIO 0 para activar el modo setup tras mantener pulsado el botón 8 segundos (opción 5)
  },
  "a": [
    {
      "0": {                  // Configuración acción cuando el switch de Homekit está a OFF
        "r": [[4]]            // Relé conectado a la GPIO 12 con estado "0" (el valor por defecto, al no estar especificado es 0.)
      },
      "1": {                  // Configuración acción cuando el switch de Homekit está a ON
        "r": [[4, 1]]         //  Relé conectado a la GPIO 12 con estado "1" (el valor por defecto, al no estar especificado es 0.)
      },
      "b": [                  // Configuración de los botones, el cual debe ser una array
        [0]                   // Primer botón conectado al GPIO 0 como "pulsación simple" (valor por defecto al no estar especificado)
      ],
      "s": 0                  // Estado inicial apagado
    }
  ]
}
```
