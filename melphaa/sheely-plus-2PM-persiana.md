# Persiana exterior con Shelly Plus 2 PM

<img src="https://templates.blakadder.com/assets/device_images/shelly_plus_2PM.webp" alt="Shelly-plus-2pm" width="450"/>

> [!NOTE]
> El conexionado del dispositivo para _flashearlo_ se encuentra definido en la [guía Shelly OTA](../docs/flash_ota_shelly.md)
>
> La guía para _flashear_ el dispositivo es [Flasheo HAA](../docs/flash_haa.md)
>
> Información del dispositivo [blakadder](https://templates.blakadder.com/shelly_plus_2PM.html)

## Automatizar persianas exteriores

El _script_ adjunto se define para gestionar la apertura y cierre de una persiana exterior con una configuración de 23 segundos de apertura y 20 segundos de cierre.

### `Melphaa` _script_ para subir al dispositivo

```json
{"c":{"io":[[[12,13,0],2],[[4],6,1],[[5,18],6,0,1],[[35],10,0,3],[[27]]],"l":0,"n":"device-hostname","b":[[4,5]],"ic":[[25,26,100]]},"a":[{"t":45,"o":23,"c":20,"f":70,"0":{"r":[[13],[12,1]],"m":[[2,-10001],[3,-10001]]},"1":{"r":[[13,1],[12]],"m":[[2,-10001],[3,-10001]]},"2":{"r":[[13],[12]],"m":[[2,-10000],[3,-10000]]},"3":{"r":[[13],[12,0,0.2]],"m":[[2,-10001],[3,-10001]]},"4":{"r":[[13,0,0.2],[12]],"m":[[2,-10001],[3,-10001]]},"8":{"m":[[0,101]]},"f0":[[5,0]],"f1":[[18,0]],"f2":[[5],[18]],"es":[{"t":75,"h":2,"ks":0,"j":2,"cd":0.95,"n":2,"dt":[0,56],"vf":0.0000382602,"vo":-0.068,"cf":0.00000949523,"co":-0.017,"pf":0.006097560976,"y1":[{"v":2,"r":1,"0":{"m":[[1,-1]]}},{"v":2.5}]},{"t":75,"h":2,"ks":0,"j":2,"cd":0.45,"n":3,"dt":[0,56],"vf":0.0000382602,"vo":-0.068,"cf":0.00000949523,"co":-0.017,"pf":0.006097560976,"y1":[{"v":2,"r":1,"0":{"m":[[1,-1]]}},{"v":2.5}]},{"t":22,"h":2,"n":5,"g":35,"j":5,"y0":[{"v":75,"r":1,"0":{"m":[[1,-1]]}}]}]}]}
```

### Descripción del _script_

```json
{
  "c": {
    "io": [                   // Configuración de los GPIO's
      [[12, 13, 0], 2],       // Se seleccionan los GPIO 12, 13 y 0 como pines de salida
      [[4], 6, 1],            // Se selecciona el GPIO 4 como pin de entrada con la resistencia de pull-up interna habilitada
      [[5, 18], 6, 0, 1],     // Se selecciona el GPIO 5 y 18 como pin de entrada sin resistencia pull-up / pull-down interna habilitada y señal invertida
      [[35], 10, 0, 3],       // Se selecciona el GPIO 35 como entrada ADC sin resistencia pull-up / pull-down interna habilitada con rango atenuado a 11dB
      [[27]]                  // Se selecciona el GPIO 27 como GPIO deshabilitado
    ],
    "l": 0,                   // Se selecciona el GPIO 0 como led de estado del dispositivo
    "n": "device-hostname",   // Hostname del dispositivo
    "b": [[4, 5]],            // Se selecciona el GPIO 4 para activar el modo setup tras mantener pulsado el botón 8 segundos (opción 5)
    "ic": [[25, 26, 100]]     // Configuración i2C con GPIO 25 como SCL, GPIO 26 como SDA y una frecuencia de 100Hz
  },
  "a": [
    {
      "t": 45,                // Servicio del tipo "Window Covering"
      "o": 23,                // Tiempo de apertura de 23 segundos
      "c": 20,                // Tiempo de cierre de 20 segundos
      "f": 70,                // Factor de corrección entre la posición de la persiana el estado de apertura y cierre real
      "0": {                  // Configuración acción de cierre de persiana desde el estado STOP
        "r": [[13], [12, 1]], // Se cambia estado de las GPIO 13 a OFF y la GPIO 12 a ON
        "m": [                // Configuración de notificaciones
          [2, -10001],        // Servicio 2 deshabilitado
          [3, -10001]         // Servicio 3 deshabilitado
        ]
      },
      "1": {                  // Configuración acción de apertura de persiana desde el estado STOP
        "r": [[13, 1], [12]], // Se cambia estado de las GPIO 13 a ON y la GPIO 12 a OFF
        "m": [                // Configuración de notificaciones
          [2, -10001],        // Servicio 2 deshabilitado
          [3, -10001]         // Servicio 3 deshabilitado
        ]
      },
      "2": {                  // Configuración acción de STOP ya sea durante la apertura o cierre
        "r": [[13], [12]],    // Se cambia estado de las GPIO 13 a OFF y la GPIO 12 a OFF
        "m": [                // Configuración de notificaciones
          [2, -10000],        // Servicio 2 habilitado
          [3, -10000]         // Servicio 3 habilitado
        ]
      },
      "3": {                  // Configuración acción de cierre mientras se está abriendo la persiana
        "r": [[13], [12, 0, 0.2]], // Se cambia estado de las GPIO 13 a OFF y la GPIO 12 con valor 0 y espera de 0.2 segundos antes de volver al estado anterior
        "m": [                // Configuración de notificaciones
          [2, -10001],        // Servicio 2 deshabilitado
          [3, -10001]         // Servicio 3 deshabilitado
        ]
      },
      "4": {                  // Configuración acción de apertura mientras se está cerrando la persiana
        "r": [[13, 0, 0.2], [12]], // Se cambia estado de las GPIO 13 con valor 0 y espera de 0.2 segundos antes de volver al estado anterior y la GPIO 12 OFF
        "m": [                // Configuración de notificaciones
          [2, -10001],        // Servicio 2 deshabilitado
          [3, -10001]         // Servicio 3 deshabilitado
        ]
      },
      "8": {                  // Configuración acción de obstrucción detectada
        "m": [                // Configuración de notificaciones
          [0, 101]            // 
        ]
      },
      "f0": [[5, 0]],         // GPIO 5 configurada para el cierre de persiana como pulsación simple opuesta
      "f1": [[18, 0]],        // GPIO 18 configurada para la apertura de persiana como pulsación simple opuesta
      "f2": [[5], [18]],      // GPIO 5 y GPIO 18 configurada para el STOP de persiana durante la apertura o cierre como pulsación simple
      "es": [                 // Configuración de servicios extra
        {                     // Configuración primer servicio extra
          "t": 75,            // Servicio del tipo "Medidor de consumo"
          "h": 2,             // Servicio oculto en la aplición Homekit pero visible en la App HAA Managers
          "ks": 0,            // 
          "j": 2,             // 
          "cd": 0.95,         // 
          "n": 2,             // 
          "dt": [0, 56],      // 
          "vf": 0.0000382602, // 
          "vo": -0.068,       // 
          "cf": 0.00000949523,// 
          "co": -0.017,       // 
          "pf": 0.006097560976,// 
          "y1": [
            {
              "v": 2,
              "r": 1,
              "0": {
                "m": [
                  [1, -1]
                ]
               }
            },
            {
              "v": 2.5
            }
          ]
        },
        {                     // Configuración segundo servicio extra
          "t": 75,            // Servicio del tipo "Medidor de consumo"
          "h": 2,             // Servicio oculto en la aplición Homekit pero visible en la App HAA Manager
          "ks": 0,
          "j": 2,
          "cd": 0.45,
          "n": 3,
          "dt": [0, 56],
          "vf": 0.0000382602,
          "vo": -0.068,
          "cf": 0.00000949523,
          "co": -0.017,
          "pf": 0.006097560976,
          "y1": [
            {
              "v": 2,
              "r": 1,
              "0": {
                "m": [[1, -1]]
              }
            },
            {
              "v": 2.5
            }
          ]
        },
        {                     // Configuración tercer servicio extra
          "t": 22,            // Servicio del tipo "Sensor de Temperatura"
          "h": 2,             // Servicio oculto en la aplición Homekit pero visible en la App HAA Manager
          "n": 5,             // Configuración del tipo de "Chip" como "Chip virtual"
          "g": 35,            // Sensor de temperatura conectado en el GPIO 35
          "j": 5,             // Frecuencia de consulta al sensor de 5 segundos
          "y0": [             // Confguración de la Wildcard para cuando el sensor alcance una temperatura concreta
            {
              "v": 75,        // Límite a 75º
              "r": 1,         // Repetición configurada a 1 segundo
              "0": {          // Array de acciones
                "m": [[1, -1]]// Servicio 1
              }
            }
          ]
        }
      ]
    }
  ]
}
```
