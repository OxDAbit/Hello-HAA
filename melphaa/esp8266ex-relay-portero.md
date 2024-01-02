# ESP8266EX Relay Board 10A DC 7-30V

## Apertura de puerta desde el interfono

`MEPLHAA` está diseñado para gestionar la PCB detallada en el [ESP8266EX Wi-Fi 10A DC 7-30V](../docs/esp_relay_pinout.md)
Se mantiene abierta la puerta todo el rato que esté activo el pulsador del interfono y mantendrá abierta la puerta durante 3 segundos si se activa desde Homekit

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c":{"io":[[[4],2],[[0],6,1]],"l":13,"n":"portero"},"a":[{"0":{"r":[[4,1,4]]},"1":{"r":[[4]]},"t":4,"i":4,"b":[[0,1],[0,0]],"s":0}]}
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
    "n": "portero"            // Hostname del dispositivo
  },
  "a": [
    {
      "t": 4,                 // Servicio del tipo "Mecanismo de Bloqueo"
      "i": 4,                 // Tiempo de espera antes de devolver el mecanismo a su estado anterior en Homekit
      "0": {                  // Configuración acción cuando el switch de Homekit está a OFF
        "r": [[4, 1, 4]]      // Se cambia el estado a ON del relé conectado a la GPIO 4 con una duración de 4 segundos
      },
      "1": {                  // Configuración acción cuando el switch de Homekit está a ON
        "r": [[4]]            // Se cambia el estado a OFF del relé conectado a la GPIO 4 hasta que vuelva a activarse
      },
      "b": [                  // Configuración de los botones, el cual debe ser una array
        [0,1],                // Primer botón conectado al GPIO 0 como "pulsación simple"
        [0,0]                 // Segundo botón conectado al GPIO 0 como "pulsación simple" invertida (valor opuesto al tipo 1)
      ],
      "s": 0                  // Estado inicial apagado
    }
  ]
}
```
