# Automatización apertura/cierre cancela de entrada mediante `ESP8266 Relay Board`

## Objetivo del proyecto

Se requiere automatizar la apertura y el cierre de la puerta de la cancela.
Para ello, la apertura se podrá realizar:

- Desde el pulsador del interfono: mientras está pulsado el cierre de entrada estará abierto y cuando se deje de pulsar se encontrará cerrado
- Desde la aplicación de homekit, la cual aplicará un temporizado de 3 segundos durante los cuales el cierre estará abierto

## Flasheo del dispositivo para instalar HAA

El conexionado para el _flasheo_ del dispositivo está detallado en el documento [ESP Relay Board](../../docs/esp_relay_pinout.md)
Para _flashear_ el dispositivo con el _firmware_ **HAA** se debe seguir la guía [Flash HAA](../../docs/flash_haa.md)

## MELPHAA

El `MELPHAA` utilizado para la confguración del dispositivo, así como su explicación, está documentado en [Melphaa ESP8266 Portero](../../melphaa/esp8266ex-relay-portero.md)

## Montaje

<img src="../../images/portero-conexionado.png" alt="Conexionado Portero" width="450"/>
