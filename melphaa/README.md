# _Scripts_ `melphaa`

> [!WARNING]
> Los _scripts_ `melphaa` están creados para poder funcionar a partir de la versión del _firmware_ `haa` **Merlin v12**, por lo que no son válidos para versiones inferiores de `haa`

|Dispositivo|Función|Archivo|MELPHAA|
| --------- | ----- | ----- | ----- |
|Athom RGB Led|Encendido/Apagado tira led y selección de color desde Homekit|[Doc](/melphaa/athom-rgb-led.md)|`{"c":{"io":[[[4,12,14],7],[[0],6,1]],"n":"device-hostname","b":[[0,5]],"q":500},"a":[{"t":30,"g":[12,4,14],"b":[[0]]}]}`|
|ESP01 Relay|Control relé|[Doc](/melphaa/esp01-1C-relay-interruptor.md)|`{"c":{"io":[[[0,1],2],[[3],6,1]],"l":1,"n":"device-hostname","b":[[3,5]]},"a":[{"0":{"r":[[0]]},"1":{"r":[[0,1]]},"b":[[0]],"s":0}]}`|
|Sonoff mini R2|Interruptor con circuito conmutado|[Doc](/melphaa/sonoff-mini-r2-conmutador.md)|`{"c":{"io":[[[12,13],2],[[0,4],6,1]],"l":13,"n":"device-hostname","b":[[0,5]]},"a":[{"0":{"r":[[12]]},"1":{"r":[[12,1]]},"b":[[0],[4],[4,0]],"s":0}]}`|
|Shelly Plus 2PM|Apertura y cierre de persiana|[Doc](/melphaa/sheely-plus-2PM-persiana.md)|`{"c":{"io":[[[12,13,0],2],[[4],6,1],[[5,18],6,0,1],[[35],10,0,3],[[27]]],"l":0,"n":"device-hostname","b":[[4,5]],"ic":[[25,26,100]]},"a":[{"t":45,"o":23,"c":20,"f":70,"0":{"r":[[13],[12,1]],"m":[[2,-10001],[3,-10001]]},"1":{"r":[[13,1],[12]],"m":[[2,-10001],[3,-10001]]},"2":{"r":[[13],[12]],"m":[[2,-10000],[3,-10000]]},"3":{"r":[[13],[12,0,0.2]],"m":[[2,-10001],[3,-10001]]},"4":{"r":[[13,0,0.2],[12]],"m":[[2,-10001],[3,-10001]]},"8":{"m":[[0,101]]},"f0":[[5,0]],"f1":[[18,0]],"f2":[[5],[18]],"es":[{"t":75,"h":2,"ks":0,"j":2,"cd":0.95,"n":2,"dt":[0,56],"vf":0.0000382602,"vo":-0.068,"cf":0.00000949523,"co":-0.017,"pf":0.006097560976,"y1":[{"v":2,"r":1,"0":{"m":[[1,-1]]}},{"v":2.5}]},{"t":75,"h":2,"ks":0,"j":2,"cd":0.45,"n":3,"dt":[0,56],"vf":0.0000382602,"vo":-0.068,"cf":0.00000949523,"co":-0.017,"pf":0.006097560976,"y1":[{"v":2,"r":1,"0":{"m":[[1,-1]]}},{"v":2.5}]},{"t":22,"h":2,"n":5,"g":35,"j":5,"y0":[{"v":75,"r":1,"0":{"m":[[1,-1]]}}]}]}]}`|
