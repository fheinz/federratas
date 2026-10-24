---
title: "Por ejemplo, el Dr. Luis Eduardo Rodríguez no tiene idea de lo que hace"
date: 2012-11-17
categories: ["Era digital", "Tecnocracia"]
---

El Diario judicial decía hace unos días que
[“En la era de Internet, los jueces no cazan una”](http://www.diariojudicial.com/contenidos/2012/09/10/noticia_0012.html).
Con la ayuda del Sr. Sergio Leonardo Rodríguez, Director de Asuntos Penales y
Jurídicos de la Administración Nacional de la Seguridad Social (ANSES) y la
Sra. María José Pérez, Coordinadora de Actuaciones Penales de la ANSES, el
[Dr. Luis Eduardo Rodríguez](http://www.pjn.gov.ar/02_Central/Index2_PP.Asp?ID=3674),
a cargo del Juzgado Nacional en lo Criminal y Correccional Federal Nº 9 parece
querer erigirse en un ejemplo de esta situación, al
[ordenar a los proveedores de Internet que bloqueen el acceso a páginas web que explican cómo desbloquear las notebooks del plan Conectar Igualdad](http://www.prensa.argentina.ar/2012/11/12/35882-por-orden-judicial-bloquean-el-acceso-a-sitios-de-internet.php).

[El fallo](https://docs.google.com/open?id=0B2L9l5VPUiJ9S2dIelhCOHJ5eFk) tiene
muchos aspectos preocupantes, comenzando por la idea de que “el caso de marras
presenta una manifestación de la libertad de expresión, la cual se ha inmiscuido
en el ámbito del orden y la seguridad pública” y que por ello debe ser
reprimido, lo que no tiene el más mínimo sentido. Aún suponiendo que _todos_ los
usos posibles de esa información fueran ilegales[^1], eso no convierte a la
información en sí en ilegal. Por ejemplo, no se me ocurren ejemplos legales de
uso de [bombas molotov](https://es.wikipedia.org/wiki/C%C3%B3ctel_molotov), y
mucho menos de [bombas de caño](https://en.wikipedia.org/wiki/Pipe_bomb), pero
eso no quiere decir que esté prohibido publicar cómo fabricarlas.

Pero aquí quiero concentrarme en la parte de “no cazan una”. En este caso, los
demandantes no tienen idea de lo que están pidiendo, el juez no tiene idea de lo
que está ordenando, y el resultado de la causa es exactamente el contrario al
que estaban persiguiendo (¡lo que en una de esas es bueno!). 

Haciendo alarde de ignorancia técnica, los demandantes solicitan al juez que
ordene a _los proveedores de Internet_ que bloqueen el acceso a una lista de
direcciones web (URLs), y el juez se lo concede. El problema es que los
proveedores de Internet no son los que otorgan o deniegan acceso a páginas web.
Su servicio consiste meramente en llevar paquetes de datos de un lado a otro,
idealmente sin tener la menor idea de cuál es el contenido de esos paquetes:
algunos son pedidos de páginas web, otros son llamadas telefónicas, otros son
correos electrónicos, chat…

La única manera que tendrían los proveedores de Internet de bloquear el acceso a
esas páginas sería _inspeccionando todo el tráfico de los usuarios_, registrando
todas sus comunicaciones para detectar si están intentando acceder a las páginas
prohibidas, lo que constituye una intromisión masiva de los ISP en la vida
privada de los usuarios. De golpe no sólo tienen permiso, sino _obligación_ de
espiar todas las comunicaciones de todo el mundo.

Las consecuencias de la ignorancia no se limitan a crear un mecanismo de
vigilancia masivo que viola la intimidad de todo el mundo. Además es
completamente inefectivo a los fines buscados, por tres razones separadas:

1. Hay muchas más páginas que muestran la misma información, que no son
   bloqueadas, y es trivial crear nuevas páginas con el mismo contenido, de modo
   que quienes buscan esta información siguen teniendo acceso a ella.
2. Aún pese al bloqueo, las mismas páginas siguen estando disponibles mediante
   el simple recurso de usar un servidor _proxy_ (basta ingresar “web proxy” en
   su buscador favorito para encontrarlos).
3. Antes de esta demanda, pocas personas sabían de la existencia de
   instrucciones que permitieran desbloquear las netbook. Hoy, en virtud del
   inevitable
   [Efecto Streisand](https://es.wikipedia.org/wiki/Efecto_Streisand), mucha más
   gente sabe no sólo que existen, sino además dónde buscarlas

Por cierto, si bien el último punto fomenta la divulgación de esta información,
que es exactamente lo contrario de lo que pretendían los demandantes, se trata
del único resultado positivo de la orden judicial.

Para entender por qué, basta con tener en cuenta que si había pocas personas que
sabían cómo se desbloquean las notebooks, los potenciales ladrones de notebook
estaban entre los que sí lo sabían. Muchos padres estaban tranquilos dejando que
sus niños llevaran la notebook encima, pensando que el bloqueo de las notebook
las hacía poco atractivas para el robo, pero esa tranquilidad estaba
injustificada. Al menos ahora, sabiendo que no es así, podrán tomar precauciones
adecuadas para proteger a sus niños de un peligro que desconocían.

[^1]:
    Dos usos concretos que no lo son: 1) Cuando la red no funciona y los
    técnicos no van a tiempo, haciendo que la burocracia en la administración
    del TPM evite el uso previsto del equipo. 2) Cuando el equipo es cedido, al
    final de la escuela y la persona que lo tiene para su uso personal decide
    desactivar el TPM para poder cambiar el BIOS y poner una imagen de booteo
    que le gusta más.
