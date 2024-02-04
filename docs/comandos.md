# Resumen de comandos útiles para trabajar con HAA

1. Lectura de _logs_ en red

    ``` bash
    nc -kulnw0 45678
    ```

2. Lectura de _logs_ de un dispositivo conectado por USB / Serie (Mac osx)

    Comando:

    ``` bash
    screen <puerto USB dispositivo> <Baudrate comunicación>
    ```

    Comando de ejemplo:

    ``` bash
    screen /dev/tty.usbserial-144240 115200
    ```

3. Descargar, desde terminal, la última versión del binario `fullhaaboot.bin`

    ```bash
    curl -LOk https://github.com/RavenSystem/haa/releases/latest/download/fullhaaboot.bin
    ```

4. Realizar _backup_ de un dispositivo ESP

    Comando:

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> read_flash 0x00000 0x100000 <Nombre del archivo _backup_>
    ```

    Comando de ejemplo:

    ``` bash
    python3 -m esptool -p /dev/tty.usbserial-144240 read_flash 0x00000 0x100000 fwbackup.bin
    ```

5. Borrar _Flash_ de un dispositivo ESP

    Comando:

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> erase_flash
    ```

    Comando de ejemplo:

    ``` bash
    python3 -m esptool -p /dev/tty.usbserial-144240 erase_flash
    ```

6. _Flashear_ ESP8266

    Comando:

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> -b 115200 --before=default_reset --after=hard_reset write_flash -fs 1MB -fm dout 0x0 <Archivo HAA para _flasear>
    ```

    Comando de ejemplo:

    ``` bash
    python3 -m esptool -p /dev/tty.usbserial-144240 -b 115200 --before=default_reset --after=hard_reset write_flash -fs 1MB -fm dout 0x0 fullhaaboot.bin
    ```

> [!TIP]
> Para el _flasheo_ de los Chips ESP8266EX me he encontrado con problemas de voltaje. No se muestra ningún error tras finalizar el proceso de grabacón del _firmware_ pero una vez finalizado, no inicia el dispositivo y por ende no genera el AP para proseguir con el proceso de configuración.

6. _Flashear_ ESP32, ESP32-S y ESP32-C

    Comando:

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> -b 460800 --before=default_reset --after=hard_reset write_flash -fs 2MB -fm dio 0x0 <Archivo HAA para _flasear>
    ```

    Comando de ejemplo:

    ``` bash
    python3 -m esptool -p /dev/tty.usbserial-144240 -b 460800 --before=default_reset --after=hard_reset write_flash -fs 2MB -fm dio 0x0 fullhaaboot.bin
    ```
