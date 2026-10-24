---
title: "Mono: +1; depender de Mono: -1"
date: 2009-07-01
categories: ["Era digital", "Ontodoncias"]
---

[Richard Stallman](http://stallman.org/), iniciador del movimiento de software
libre, y fundador de la [Free Software Foundation](http://fsf.org) ha publicado
un artículo en el que argumenta por qué
[las distribuciones de software libre no deberían depender de Mono o C#](http://www.fsf.org/news/dont-depend-on-mono).
Como ocurre cada vez que Richard dice una verdad incómoda (lo que ocurre un 99%
de las veces que habla o escribe), se produjo un enorme revuelo al respecto, en
particular por parte de los desarrolladores de Mono, que sienten que su trabajo
está siendo criticado.

Pero Richard tiene razón (a las distribuciones no les conviene depender de
[Mono](http://www.mono-project.com/), C# o de
[Portable.NET](http://www.gnu.org/software/dotgnu/pnet.html)), y los
desarrolladores de Mono están equivocados (Richard no está criticando su
trabajo, y de hecho lo elogia). 

Lo que Richard señala es que es peligroso _depender_ de implementaciones de C#
para la distribución. Sin embargo, mientras la distribución no dependa de él,
incluir soporte para ese lenguaje es útil: cuando los usuarios tienen programas
escritos en C# que usaban cuando tenían software privativo, pueden seguir
usándolos bajo GNU/Linux, y eso es indudablemente bueno.

El problema con el lenguaje C# tiene que ver con algo que en Argentina no
existe, pero sí en Estados Unidos, Japón y otros países, las [patentes de
software]({{< ref "2007-01-03-programas-patentados.md" >}}). Microsoft ha
obtenido patentes de software sobre partes importantes de C# y .NET en aquellos
países que son lo suficientemente imprudentes como para permitirlas, y en varias
ocasiones ha mencionado que evalúa la posibilidad de utilizarlas para frenar el
avance de GNU/Linux.

Las patentes de Microsoft sobre C# y .NET no afectan a Linux en sí, ni a la
mayoría de los programas libres, sólo afectan a implementaciones libres de estas
especificaciones. Así, mientras las distribuciones de software libre no
_dependan_ de Mono o Portable.NET, a Microsoft no le conviene iniciar juicio por
violación de patentes: las distribuciones podrían simplemente dejar de incluir
esos programas, y se acabó el problema, y el único que pierde es el mismo
Microsoft, porque pierden una plataforma sobre la que hacer correr sus
programas.

Pero cuando una distribución _depende_ de programas en C#, es decir, cuando
partes importantes de la funcionalidad de la distribución como un todo exigen
que haya una implementación del lenguaje instalada, esas patentes se convierten
en un riesgo serio: si Microsoft iniciara juicio por violación de patentes,
sería posible que un juez les ordene que excluyan a C# de la distribución, con
el consecuente impacto en la funcionalidad del sistema. Es de notar que para que
esto ocurra, ni siquiera hace falta que Microsoft _gane_ el juicio de patentes,
sino simplemente que lo inicie, logre una medida cautelar, y se asegure de que,
si lo va a perder, lo pierda luego de años de costoso litigio.

¿Vale la pena exponerse de esa manera?
