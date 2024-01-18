# _Flasheo_ de dispositivos con `haa`

A continuación se detallan los pasos a seguir para poder _flashear_ cualquier dispositivo con el _firmware_ `haa`

## Pasos previos

1. Descargar e instalar `python` en su versión más actual (en el momento de redactar este _paper_ está en la v3.11) desde la página web oficial [Python](https://www.python.org/downloads/)
2. Instalar el módulo `esptool` [Github](https://github.com/espressif/esptool)

    ``` bash
    python3 -m pip install --upgrade pip
    python3 -m pip install esptool
    ```

3. Crear un _script_ en `python`, o descargarlo del [repositorio](../src/detect_usb.py), con el nombre que queramos (Ex: `usb_detect.py`) y que contenga el código adjunto a continuación. Este _script_ nos servirá en los próximos pasos para detectar el puerto USB al que se conecta el dispositivo:

    ```python
    import glob
    print(glob.glob('/dev/tty.*'))
    ```

4. Conectar el dispositivo vía RS-232 al ordenador
5. Identificar el _chip_ qué queremos _flashear_ para conocer el modelo en concreto mediante el comando:

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> flash_id
    ```

    Tras la ejecución del comando, se obtendrá una información como la detallada a continuación, la cual nos servirá para saber que archvivos descargar y qué comandos utilizar para poder _flashear_ el dispositivo (El tipo de dispositivo viene detallado en la línea `Chip is ESP...`):

    ``` bash
    esptool.py v4.7.0
    Found 4 serial ports
    Serial port /dev/cu.usbserial-144240
    Connecting...
    Detecting chip type... Unsupported detection protocol, switching and trying again...
    Connecting...
    Detecting chip type... ESP8266
    Chip is ESP8266EX
    Features: WiFi
    Crystal is 26MHz
    MAC: c8:c9:a3:2f:a8:f8
    Stub is already running. No upload is necessary.
    Manufacturer: 5e
    Device: 4016
    Detected flash size: 4MB
    Hard resetting via RTS pin...
    ```

> [!TIP]
> Para el _flasheo_ de los Chips ESP8266EX me he encontrado con problemas de voltaje. No se muestra ningún error tras finalizar el proceso de grabacón del _firmware_ pero una vez finalizado, no inicia el dispositivo y por ende no genera el AP para proseguir con el proceso de configuración.

6. Descargar `fullhaaboot.bin` (página de [descarga](https://github.com/RavenSystem/haa/releases/latest/download/fullhaaboot.bin))

## _Flasheo_ del dispositivo

1. Mantener pulsado el botón del dispositivo y conectar el conversor **RS-232**
2. Creamos un _backup_ del _firmware_ original del dispositivo desde el terminal:

    ```bash
    python3 -m esptool -p <puerto USB dispositivo> read_flash 0x00000 0x100000 <Nombre del archivo _backup_>
    ```

    Resultado mostrado tras la ejecución del comando:

    ```bash
    esptool.py v2.8
    Serial port /dev/tty.usbserial-14310
    Connecting....
    Detecting chip type... ESP8266
    Chip is ESP8285
    Features: WiFi, Embedded Flash
    Crystal is 26MHz
    MAC: 70:03:9f:47:e8:0b
    Uploading stub...
    Running stub...
    Stub running...
    1048576 (100 %)
    1048576 (100 %)
    Read 1048576 bytes at 0x0 in 95.8 seconds (87.5 kbit/s)...
    Hard resetting via RTS pin...
    ```

3. Quitamos la alimentación del dispositivo
4. Mantener pulsado el botón del dispositvo y volver a conectar la alimentación
5. Borramos el _firmware_ del dispositivo:

    ```bash
    python3 -m esptool -p <puerto USB dispositivo> erase_flash
    ```

    Resultado mostrado tras la ejecución del comando:

    ```bash
    esptool.py v2.8
    Serial port /dev/tty.usbserial-143240
    Connecting....
    Detecting chip type... ESP8266
    Chip is ESP8285
    Features: WiFi, Embedded Flash
    Crystal is 26MHz
    MAC: 24:a1:60:10:0e:79
    Uploading stub...
    Running stub...
    Stub running...
    Erasing flash (this may take a while)...
    Chip erase completed successfully in 1.2s
    Hard resetting via RTS pin...
    ```

6. Quitamos la alimentación del dispositivo
7. Mantener pulsado el botón del dispositvo y volver a conectar la alimentación
8. Subimos el _firmware_ del HAA ejecutando el comando adjunto desde la carpeta dónde tenemos ubicado el archivo `fullhaaboot.bin`

    - Comando para los ESP8266

    ```bash
    python3 -m esptool -p <puerto USB dispositivo> -b 115200 --before=default_reset --after=hard_reset write_flash -fs 1MB -fm dout 0x0 <Archivo HAA para _flasear>
    ```

    - Comando para el _flasheo_ de ESP32, ESP32-C y ESP32-S

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> -b 460800 --before=default_reset --after=hard_reset write_flash -fs 2MB -fm dio 0x0 <Archivo HAA para _flasear>
    ```

9. Quitamos la alimentación del dispositivo y volvemos a conectarlo
10. Tras el _flasheo_ y el reinicio del dispositivo, este arrancará generando un red WiFi con el prefijo **HAA-**.
    Establecemos conexión WiFi con dicha red y accederemos a la dirección IP `192.168.4.1:4567`
11. Una vez conectado a nuestra red WiFi, el dispositivo se conectará al Github oficial para comprobar si hay alguna versión más actual para descargar, en caso afirmativo la descargará e instalará.
    Para leer los _logs_ del dispositvo dónde se indican los pasos que está realizando se puede ejecutar el comando adjunto:

    ``` bash
    nc -kulnw0 45678
    ```

12. Se prosigue con el proceso de configuración, detallado en el documento [config_haa.md](../docs/config_haa.md)
