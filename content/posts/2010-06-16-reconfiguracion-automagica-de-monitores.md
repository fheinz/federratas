---
title: "Reconfiguración automágica de monitores"
date: 2010-06-16
categories: ["Era digital", "Perro viejo"]
---

{{< figure src="/wp-content/uploads/2010/06/ws1.jpg" link="/wp-content/uploads/2010/06/ws1.jpg" alt="Foto de mi estación de trabajo" caption="Foto de mi estación de trabajo" >}}Hace
ya años que no uso computadoras “de escritorio”: mi única máquina es la laptop.
Casi todas las laptops modernas saben hacer algo muy útil: cuando le conectás un
monitor en el puerto VGA, podés armar un escritorio extendido, poniendo algunas
ventanas en el monitor, y otras en la pantalla de la laptop. Así, hace un tiempo
ya que me armé el espacio de trabajo que se ve en la foto: sólo tengo que
conectar un cable USB y el cable VGA, y ya tengo acceso a todos los periféricos
de mi escritorio.

En realidad, miento: antes de poder usar el monitor externo, tengo que buscar el
applet de control de geometría del escritorio, abrir la ventana de “configurar
los parámetros de monitor”, encender la salida de monitor, acomodar el
rectángulo que representa al monitor de modo que quede arriba del que representa
la pantalla de la laptop, hacer click en “Aplicar”, confirmar que la imagen se
ve bien, cerrar la ventana… y recién entonces puedo seguir trabajando. Y cuando
quiero quitar la laptop, debo hacer el camino inverso antes de desconectar el
monitor, so pena de que la máquina quede mal configurada.

Lamentando esta triste situación en la lista del
[Grupo de Usuarios de Software Libre de Córdoba](http://grulic.org.ar/), tiramos
un par de ideas, y armamos una solución automágica para el problema. 

Lo primero que tenemos que hacer es guardar el siguiente script en
/usr/local/bin/auto-monitor, cuyo objetivo es comprobar si el monitor está
conectado o no, y reconfigurar el escritorio de manera acorde:

```
#!/bin/sh
for x in /tmp/.X11-unix/*; do
    export DISPLAY=:$(echo $x | sed s#/tmp/.X11-unix/X##)
    user=$(who | grep $DISPLAY | cut -d ' ' -f 1)
    su $user -c 'xrandr --output LVDS1 --auto --output VGA1 --auto --above LVDS1'
done

```

Ahora, todo lo que necesitamos es lograr que ese script se ejecute cada vez que
el monitor se conecta o desconecta de la máquina. Quien se encarga de monitorear
eso en sistemas basados en Linux es udev, de modo que lo que tenemos que hacer
es guardar este archivo como /etc/udev/rules.d/97-auto-monitor.rules, y luego
ejecutar el comando udevadm control --reload-rules:

```
# Run helper every time an external monitor (dis)appears
ACTION=="change", SUBSYSTEM=="drm", RUN+="/usr/local/bin/auto-monitor"

```

¡Listo! Ahora, cada vez que conecto o desconecto el cable del monitor a la
laptop, mi escritorio se reconfigura automágicamente.
