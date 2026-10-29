---
title: "Automagical Monitor Reconfiguration"
date: 2010-06-16
categories: ["Era digital", "Perro viejo"]
---

{{< figure src="/wp-content/uploads/2010/06/ws1.jpg"
    link="/wp-content/uploads/2010/06/ws1.jpg"
	alt="A laptop computer connected to a keyboard and external monitor"
	caption="A photo of my workstation"
>}}

It has been years since I last used a "desktop" computer: my only
machine is a laptop. Almost all modern laptops are capable of a very
nifty trickl: if you connect a monitor to the VGA port, you can set up
an extended desktop, placing some windows on the monitor and others on
the laptop screen. Thus, some time ago, I set up the workspace seen in
the photo: I only need to plug in a USB cable and the VGA cable, and I
have access to all my desktop peripherals.

Actually, that's a lie. Before I can use the external monitor, I must
hunt down the display geometry applet. Then I need to open the
"configure monitor settings" window, enable the monitor output, and
arrange the rectangle representing the monitor so it sits above the
one that represents the laptop screen.  Then I need to click on
"Apply," confirm that the image looks right, close the window&hellip;
and only then am I allowed to get back to work. And of course, when I
want to take the laptop with me, I must reverse the entire process
before disconnecting the monitor, lest the machine remain poorly
configured.

Lamenting this sorry state of affairs on the [Free Software Users
Group of Córdoba](http://grulic.org.ar/)'s mailing list, we tossed
around a few ideas and put together an automagical solution to the
problem.

The first step is to save the following script in
`/usr/local/bin/auto-monitor`. Its purpose is to check whether the
monitor is connected or not and, if it is, to reconfigure the desktop
accordingly:

```
#!/bin/sh
for x in /tmp/.X11-unix/*; do
    export DISPLAY=:$(echo $x | sed s#/tmp/.X11-unix/X##)
    user=$(who | grep $DISPLAY | cut -d ' ' -f 1)
    su $user -c 'xrandr --output LVDS1 --auto --output VGA1 --auto --above LVDS1'
done

```

Now, all we need to do is to ensure that this script executes every
time the monitor is connected or disconnected. In Linux-based systems,
`udev` is responsible for monitoring such events. So we save the
following file as `/etc/udev/rules.d/97-auto-monitor.rules` and
execute the command `udevadm control --reload-rules`:

```
# Run helper every time an external monitor (dis)appears
ACTION=="change", SUBSYSTEM=="drm", RUN+="/usr/local/bin/auto-monitor"

```

Done! Now, every time I plug or unplug the monitor cable from my laptop,
my desktop reconfigures itself automagically.
