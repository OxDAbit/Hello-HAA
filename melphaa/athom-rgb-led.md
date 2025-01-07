# Athom RGB LED Controller

<img src="https://templates.blakadder.com/assets/device_images/athom_LS5050C-TAS.webp" alt="Athom-RGB" width="450"/>

> [!NOTE]
> El conexionado del dispositivo para _flashearlo_ se encuentra definido en la [Guía Athom](../docs/athom_pinout.md)
>
> La guía para _flashear_ el dispositivo es [Flasheo HAA](../docs/flash_haa.md)
>
> Información del dispositivo [blakadder](https://templates.blakadder.com/athom_LS5050C-TAS.html)

## Control de una tira led con conector RGB (Azul, Verde, Rojo, Negro)

El _script_ adjunto se define para gestionar una tira led, tanto el encendido y apagado como el cambio de color de la misma.

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c":{"io":[[[4,12,14],7],[[0],6,1]],"n":"device-hostname","b":[[0,5]],"q":500},"a":[{"t":30,"g":[12,4,14],"b":[[0]]}]}
```

### Descripción del _script_

```json
{
    "c": {
      "io": [                   // Configuración de los GPIO's
        [[4, 12, 14], 7],       // Se seleccionan los GPIO 4, 12 y 14 como pines de salida
        [[0], 6, 1]             // Se selecciona el GPIO 0 como pin de entrada con la resistencia de pull-up interna habilitada y señal invertida
      ],
      "n": "device-hostname",   // Hostname del dispositivo
      "b": [[0, 5]],            // Se selecciona el GPIO 0 para activar el modo setup tras mantener pulsado el botón 8 segundos (opción 5)
      "q": 500                  // Se configura una frecuencia PWM de 500 Hz
    },
    "a": [
      {                         // Como no se espifica la variable "t" (tipo de servicio), se configura como un accesorio del tipo switch (valor por defecto)
        "t": 30,                // Servicio del tipo "Lightbulb"
        "g":[12,4,14],          // Configuración GPIO correspondiente al RGB
        "b":[[0]]               // Primer botón conectado al GPIO 0 como "pulsación simple"
      }
    ]
}
```
