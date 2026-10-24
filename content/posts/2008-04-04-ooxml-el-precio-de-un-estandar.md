---
title: "OOXML: el precio de un estándar"
date: 2008-04-04
categories: ["Codicia", "Era digital"]
---

El 2 de abril, [ISO](http://www.iso.org) anunció que ECMA Office Open XML,
también conocido como OOXML,
[obtuvo los votos necesarios para ser aprobado como estándar ISO/IEC 29500](http://www.iso.org/iso/pressrelease.htm?refid=Ref1123).
OOXML es el formato de archivos que Microsoft Office 2007 usa por defecto, y
este anuncio es el desenlace de un proceso que llevó más de un año, durante el
cual Microsoft no escatimó esfuerzos para lograr la bendición de ISO para su
formato, mientras
[una coalición de organizaciones civiles, empresas, organismos públicos e individuos](http://www.noooxml.org/)
intentábamos explicarle al mundo, y sobre todo a ISO, por qué el formato no
merecía ese sello.

Es raro que se den “batallas” de esta envergadura alrededor de algo tan aburrido
como un estándar, y mucho más extraño es ver precisamente a Microsoft
involucrado en ellas. A lo largo de su historia, la política de estándares de la
empresa siempre fue de ignorarlos en todos los casos en los que fuera posible, y
de
[soportarlos deliberadamente mal](http://www.opera.com/pressreleases/en/2007/12/13/)
en aquellos casos en los que fueran imprescindibles. Esta política es la que le
permite mantener cautivos a sus usuarios, que ni siquiera consideran la
posibilidad de comprar productos de otras empresas por temor a no poder acceder
a los datos que ya tienen almacenados en formatos de Microsoft. 

Lo que cambió fue que en los últimos años, las administraciones públicas de
muchos países comenzaron a preocuparse por la perennidad de sus documentos
digitales: cuando un documento (digamos, una partida de nacimiento) tiene una
vida útil mayor a un siglo, es demasiado riesgoso almacenarlo en un formato que
no sabemos si podremos leer dentro de diez años. La solución a este problema es
la estandarización: si los detalles del formato son públicos, y cualquier
proveedor puede construir programas que lean y produzcan documentos en él,
podemos al menos asegurarnos que el acceso seguirá siendo posible. Así, cada vez
más administraciones públicas del mundo (incluyendo recientemente, por ejemplo,
[la de la provincia de Misiones](http://www.ccpm.misiones.gov.ar/index.php?option=com_content&task=view&id=34&Itemid=38))
exigen que sus documentos sean almacenados en un formato estándar abierto.

La reacción inicial de Microsoft a este cambio fue la habitual: ignorarlo. Al
fin y al cabo, ellos eran los “dueños” del formato secreto del que esos mismos
organismos públicos dependían para acceder a millones de documentos, y no había
en el mercado una alternativa estándar usable. Así las cosas, en vez de proveer
lo que sus clientes les pedían, prefirieron hacerse los sordos y esperar a que
se les pase el berrinche.

Mientras Microsoft estaba ocupada tapándose los oídos y cantando
"la-la-la-no-te-escucho" a voz en cuello, sin embargo, el consorcio
[OASIS](http://www.oasis-open.org/) estaba trabajando en proveer precisamente lo
que estos grandes clientes querían:
[ODF (Open Document Format)](http://www.odfalliance.org/), un formato de
archivos de oficina completamente documentado, soportado por
[múltiples proveedores y programas](http://en.wikipedia.org/wiki/OpenDocument_software#Current_support),
y que fue adoptado por ISO como ISO/IEC 26300 en el 2006. Esto cambió las reglas
radicalmente: había en el mercado varios proveedores ofreciendo productos que
satisfacían una demanda crítica de los clientes, y MS no estaba entre ellos.

¿Qué hizo MS entonces? Lógicamente, se puso a trabajar para implementar
urgentemente ISO 26300, para satisfacer las necesidades de sus clientes y
competir limpiamente en términos de precio/prestación por los contratos de la
administración pública, y se encontró con la agradable sorpresa de que ni
siquiera necesitaba escribir mucho código, porque podía incorporar a su programa
bibliotecas enteras de software libre que resolvían la mayor parte del problema.
Agradecidos por estas facilidades, y viendo las ventajas de la competencia en
colaboración en una cancha limpia, Microsoft comenzó a participar en OASIS, para
ayudar a que nuevas versiones de ODF fueran cada vez mejores y permitieran una
interoperabilidad transparente entre los programas de todos los proveedores.

¡Los agarré! Por supuesto que no fue eso lo que hizo. Eso es lo que haría una
Microsoft de un universo paralelo, en el que Patoruzú es usurero, el cigarrillo
cura el cáncer y las películas de Hollywood tienen argumentos originales. Para
Microsoft, adoptar un estándar que no está bajo su propio control implica
someterse a las dos cosas a las que más temen: tener que seguir reglas, y
competir en pie de igualdad, sin poder acudir a la ventaja que les otorga su
posición monopólica. Lo que es peor, significa enfrentar en pie de igualdad a su
adversario más temido: el software libre.

{{< figure src="/wp-content/uploads/2008/04/OOXMLSpec.png" alt="Una pila de gruesas carpetas" caption="La espacificación de OOXML" >}}

Así, la reacción de Microsoft fue apresurarse a buscar algún otro consorcio que
estuviera dispuesto a certificarle alcurnia de estándar abierto al formato que
estaban usando en Office 2007, y lo encontraron en
[ECMA](http://www.ecma-international.org/). Si por esta ruta lograban que ISO
adoptara el formato, ¡finalmente tendrían un producto que ofrecer a las
administraciones públicas que requieren estándares abiertos, sin necesidad de
soportar ningún estándar abierto en serio, y dándoles la posibilidad de excluir
del trato al software libre! El resultado de este esfuerzo fue que, en el
transcurso de un año, ECMA aprobó un estándar de 6000 páginas (la foto adjunta
da una idea de lo que estoy hablando), llamado ECMA 376, y lo presentó a ISO
para su aprobación acelerada, que fue concretada en estos días, en medio de tal
controversia que ISO decidió evitar en su anuncio el tono festivo que
habitualmente usa cuando comunica la adopción de un formato.

Así, la noticia de que Microsoft logró torcer el brazo de ISO para que adoptara
como estándar un formato duplicativo e inmaduro que mantiene intactos sus
privilegios en el mercado no merecería la cobertura de prensa que obtuvo: rara
vez vemos un titular que pregona "El Sol salió esta mañana, igual que ayer". Lo
que sí es una noticia es, sin embargo, el costo que tuvo que pagar Microsoft
para lograrlo.

No estoy hablando de dinero, aunque haya salido a la luz que un empleado de
Microsoft ofreció compensar a varias empresas suecas si apoyaban a OOXML en el
organismo de estandarización de ese país, y resulte al menos sospechoso que los
organismos de estandarización de diez países que hasta este momento jamás se
habían interesado por el tema estandarización de documentos, de repente
encontraran por ahí el dinero necesario para pasar a una categoría de socio más
privilegiada dentro de ISO justo antes de la votación, votar en bloque a favor,
y luego dejar de participar. Dinero es lo que Microsoft tiene, y no importa
cuánto tenga que gastar, no le duele.

El costo que sí les duele es el que debieron pagar en una moneda que les viene
escaseando: reputación. Su formato fue adoptado, pero en medio de escándalos en
los que empleados de la empresa fueron sorprendidos
[ofreciendo sobornos a cambio de apoyo](http://www.infoworld.com/article/07/08/31/Sweden-OOXML-vote-invalid_1.html),
o
[presentándose con tarjetas de negocios de organismos a los que no pertenecían](http://www.openmalaysiablog.com/2008/03/the-elephant-in.html),
o
[mintiendo a los organismos nacionales de estandarización acerca de las reglas de ISO](http://www.robweir.com/blog/2007/08/is-it-safe.html).
La adopción fue realizada a través de un proceso que fue criticado como
inadecuado incluso por aquellos países que no se opusieron al estándar, y
plagado de curiosidades como que los comités de estandarización de países como
[Noruega](http://blog.abrenna.com/formal-protest-against-norways-yes-to-ooxml/)
y Gran Bretaña estén protestando formalmente frente a ISO contra sus propias
organizaciones madres por ignorar su recomendación de rechazar el estándar y
votar por su aprobación de todos modos, mientras que la
[Comisión Europea investiga las acciones de Microsoft ante ISO](http://computerworld.co.nz/news.nsf/news/DFE3C11047741AFACC25741F003379BD),
incluyendo
[las irregularidades reportadas en Polonia](http://polishlinux.org/poland/possible-manipulation-around-ooxml-process-in-poland/),
como parte del proceso antimonopolio de la empresa. En todas partes del mundo
hay denuncias de presiones indebidas a favor del formato, y en nuestras costas
no se apaga el rumor de que fue el apoyo a ODF lo que les costó sus puestos en
la ONTI a Carlos Achiary y José Carllinni.

La sanción de OOXML como estándar ISO, en fin, no hace más que reforzar la
imagen de Microsoft como el gigante patotero que no puede competir en un mercado
equitativo, cree que las reglas sólo están para aplicarlas a los demás, y está
dispuesto a cualquier cosa con tal de mantener sus privilegios. Además, plantea
una pregunta: ¿cómo será la calidad de OOXML, si para lograr su aprobación MS
debió recurrir a los recursos más bajos que se conocen en la historia de la
estandarización?
