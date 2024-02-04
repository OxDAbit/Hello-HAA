# Alarma de seguridad con Wemos mini D1

<img src="https://templates.blakadder.com/assets/device_images/wemos_D1_Mini_ESP32.webp" alt="Wemos Mini D1" width="450"/>

> [!NOTE]
> El conexionado del dispositivo para _flashearlo_ se realiza conectando el cable USB directamente a la PCB
>
> La guía para _flashear_ el dispositivo es [Flasheo HAA](../docs/flash_haa.md)
>
> Información del dispositivo [blakadder](https://templates.blakadder.com/wemos_D1_Mini_ESP32.html)

## Control de una Alarma de seguridad

El _script_ adjunto se define para gestionar una alarma de seguridad generando un accesorio en paralelo que se utilizará como _trigger_ para activar la alarma tras la vinculación de los sensores de seguridad de la casa como pueden ser los sensores de contacto de puertas y ventas, sensores de presencia,...

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c":{"n":"device-hostname"},"a":[{"t":55,"s":5,"es":[{"0":{"m":[[-1,3]]},"1":{"m":[[-1,1]]}},{"1":{"m":[[-2,16]]},"i":1}]}]}
```

### Descripción del _script_

```json
{
  "c": {
    "n": "device-hostname"    // Hostname del dispositivo
  },
  "a": [
    {
      "t": 55,                // Servicio del tipo "Security System"
      "s": 5,                 // Se configura el estado inicial del dispositivo como "el estado en el que se encontraba antes del reinicio (5)"
      "n": [0,1],             // Se configuran los modos de alarma "En casa" (0), "Fuera de Casa" (1) y "Noche" (2). Se obvia el modo "Desactivado" porque es lo mismo que "En casa"
      "es": [                 // Configuración de servicios extra
        {                     // Configuración interruptor dummy que actuará como cambio de estado en la alarma (Fuera de servicio y OFF), esto se hace para evitar la confirmación desde la App de Homekit
          "1": {              // Configuración para cuando el interruptor se encuentra en estado ON
            "m": [            // Configuración de la notificación de servicio
              [
                -1,           // La configuración se realizará contra el accesorio precedente, es decir, contra la alarma
                1             // Se activa el modo "Fuera de cas"
              ]
            ]
          },
          "0": {              // Configuración para cuando el interruptor se encuentra en estado OFF
            "m": [            // Configuración de la notificación de servicio
              [
                -1,           // La configuración se realizará contra el accesorio precente, es decir, contra la alarma
                3             // Se desactiva la alarma
              ]
            ]
          }
        },
        {                     // Configuración interruptor dummy que actuará como trigger de la alarma
          "i": 1,             // Se configura 1 segundo para retornar el interruptor dummy a OFF
          "1": {              // Estado ON del interruptor dummy (trigger)
            "m": [            // Configuración de la notificación de servicio
              [
                -2,           // Configuración que afectará al primer accesorio de la lista, es decir, la alarma
                14            // Acciona la alarma de forma recurrente hasta que se interactúa con la alarma a través de la App Casa
              ]
            ]
          }
        }
      ]
    }
  ]
}
```
