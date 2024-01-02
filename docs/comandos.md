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

3. Borrar _Flash_ de un dispositivo ESP

    Comando:

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> erase_flash
    ```

    Comando de ejemplo:

    ``` bash
    python3 -m esptool -p /dev/tty.usbserial-144240 erase_flash
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

5. _Flashear_ ESP8266

    Comando:

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> -b 115200 --before=default_reset --after=hard_reset write_flash -fs 1MB -fm dout 0x0 <Archivo HAA para _flasear>
    ```

    Comando de ejemplo:

    ``` bash
    python3 -m esptool -p /dev/tty.usbserial-144240 -b 115200 --before=default_reset --after=hard_reset write_flash -fs 1MB -fm dout 0x0 fullhaaboot.bin
    ```

6. _Flashear_ ESP32, ESP32-S y ESP32-C

    Comando:

    ``` bash
    python3 -m esptool -p <puerto USB dispositivo> -b 460800 --before=default_reset --after=hard_reset write_flash -fs 2MB -fm dio 0x0 <Archivo HAA para _flasear>
    ```

    Comando de ejemplo:

    ``` bash
    python3 -m esptool -p /dev/tty.usbserial-144240 -b 460800 --before=default_reset --after=hard_reset write_flash -fs 2MB -fm dio 0x0 fullhaaboot.bin
    ```
