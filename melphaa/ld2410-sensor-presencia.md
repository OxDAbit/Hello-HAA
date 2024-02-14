# LD2410 detector de presencia humana

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fae01.alicdn.com%2Fkf%2FS61c8e193a1e244548c50b3a2d8016f170%2FHLK-LD2410-24G-FMCW-24GHz-Smart-Human-Presence-Sensing-Radar-Module-LD2410-Millimeter-Wave-Motion-Switch.jpg_Q90.jpg_.webp&f=1&nofb=1&ipt=4a677906f5d40268b39410c4260afb805c0a5b1e40f16412271a9d39fab3fc6c&ipo=images" alt="LD2410" width="450"/>

> [!NOTE]
> El conexionado del dispositivo para _flashearlo_ se realiza conectando el cable USB directamente a la PCB
>
> La guía para _flashear_ el dispositivo es [Flasheo HAA](../docs/flash_haa.md)
>
> Carcasa impresa en 3D para poder ensamblar el sensor [Skadis LD2410](https://www.thingiverse.com/thing:6429958)

## Control del sensor de presencia humana

El _script_ adjunto se define para gestionar un sensor de presencia humana.
Para integrar el sensor con Homekit, se ha recurrido al uso de un Wemos mini D1, al cual se le ha conectado el pin de salida `out` del sensor **LD2410** al pin D2 (GPIO4)

<img src="../images/ld2410.JPG" alt="LD2410 Pinout" width="450"/>

### `Melphaa` _script_ para configurar al dispositivo

```json
{"c":{"io":[[[4],6]],"n":"device-hostname"},"a":[{"t":6,"f0":[{"g":4,"t":0}],"f1":[{"g":4,"t":1}]}]}
```

### Descripción del _script_

```json
{
  "c": {
    "io": [                     // Configuración de los GPIO's
      [[4],6]                   // Se selecciona el GPIO 4 como pin de entrada con la resistencia de pull-up interna deshabilitada (señal 0 no indicada ya que se usa el valor por defecto para aligerar el MELPHAA)
    ],
    "n": "device-hostname"     // Hostname del dispositivo
  },
  "a": [
    {
      "t": 6,                   // Configuración del accesorio como Sensor de Presencia
      "f0": [                   // Gestión del pin cuando el valor del sensor de presencia es OFF.
        {"g": 4,"t": 0}
      ],
      "f1": [                   // Gestión del pin cuando el valor del sensor de presencia es OFF.
        {"g": 4,"t": 1}
      ]
    }
  ]
}
```
