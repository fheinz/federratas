---
title:
  "Iniciativa de interoperabilidad de Microsoft: ¿la semana en que se congeló el
  infierno?"
date: 2008-02-29
categories: ["Codicia", "Era digital"]
---

En el transcurso de menos de una semana, Microsoft hizo dos anuncios
espectaculares. Primero anunció
[la publicación de las especificaciones de los formatos heredados de Office](http://www.microsoft.com/interop/docs/OfficeBinaryFormats.mspx)
(los omnipresentes .DOC, .XLS y .PPT); pocos días después, una serie de
[cambios a sus prácticas de negocios con el objetivo de mejorar la interoperabilidad con otros sistemas](http://www.microsoft.com/presspass/press/2008/feb08/02-21ExpandInteroperabilityPR.mspx)
(es decir, que sea más fácil intercambiar datos entre los programas de Microsoft
los de otros proveedores). Estamos hablando de la misma empresa que construyó un
monopolio sobre la base de formatos y protocolos secretos, aquella para la que
compartir ese tipo de información con sus competidores era
[“una locura”](http://www.groklaw.net/pdf/Comes-3078.pdf). ¿A qué se debe este
cambio de actitud? ¿Qué pasó? 

### Pasaron al menos dos cosas

Pocos días más tarde, una de las razones del sorpresivo cambio resultó evidente:
la Unión Europea impuso a Microsoft
[una multa de €899.000.000](http://tecnologia.infobaeprofesional.com/notas/62376-La-Union-Europea-sanciono-a-Microsoft-con-una-multa-record.html)
por no haber cumplido adecuadamente con las órdenes de la corte que, en el 2004,
había encontrado a la empresa culpable de abuso de poder monopólico.

En aquel momento, la UE
[ya había impuesto a Microsoft una multa de €497.000.000](http://www.cnn.com/2004/BUSINESS/03/24/microsoft.eu/),
y le ordenó poner en funcionamiento mecanismos mediante los cuales sus
competidores pudieran obtener la información necesaria para construir programas
interoperables. El plazo para hacerlo era de 120 días pero, cuatro años más
tarde, la corte todavía estaba esperando que Microsoft cumpliera, y de allí la
multa.

Por otro lado, ocurrió que tanto la Unión Europea como otros gobiernos y
organizaciones están dándose cuenta de que la dependencia de Microsoft Office no
es una fatalidad inevitable, que Microsoft
[deliberadamente construye sus aplicaciones de modo que sean incompatibles con el resto del mundo](http://www.opera.com/pressreleases/en/2007/12/13/),
y que la manera de salir del atolladero es asegurarse de usar programas que
almacenen sus datos utilizando estándares abiertos.

La característica distintiva de los estándares abiertos es que cualquiera puede
implementarlos en igualdad de condiciones. Eso permite que distintos proveedores
construyan diferentes programas que comparten un formato pero compiten entre sí
en función de sus prestaciones. De este modo, un organismo que hoy usa el
programa X para su procesamiento de textos, mañana puede decidir que el programa
Y es más bonito, y cambiar de programa sin temor de perder los datos que
almacenó usando X.

No son pocas las administraciones públicas que han decidido, o están
considerando la decisión de utilizar únicamente programas de oficina que
almacenen sus datos en formatos estándar y abiertos. Afortunadamente, desde el
2006 existe un estándar para documentos de oficina:
[Open Document Format, también conocido como ODF, o ISO/IEC 26300](http://es.wikipedia.org/wiki/OpenDocument),
y existen programas de distintos proveedores que lo soportan. Lamentablemente,
Microsoft Office no está entre ellos.

Esto se debe, por cierto, únicamente a una decisión comercial de Microsoft:
siendo que literalmente **cualquiera** puede implementar ODF, no hay ningún
obstáculo a que ellos también lo hagan. Incluso si ODF no les alcanzara, por
alguna razón, siempre estuvieron invitados a la mesa a discutir maneras útiles
de actualizar el estándar. El problema es que soportar ODF significa una seria
amenaza para el modelo de negocios de Office: un usuario que puede almacenar sus
documentos en ODF **puede elegir**, y cabe la posibilidad de que en su próxima
adquisición de software no elija Office, sino
[OpenOffice.org](http://www.openoffice.org/),
[KOffice](http://www.koffice.org/), [Abiword](http://www.abisource.com/) o algún
otro programa de otro proveedor.

Para evitar eso, Microsoft prefirió insistir por todos los medios
([incluyendo algunos más bien non-sanctos](http://ec.europa.eu/idabc/en/document/7186))
en que su propio formato, OOXML, sea reconocido como estándar. OOXML es para
ellos mucho menos peligroso que ODF: si bien tiene un cierto barniz de apertura,
Office 2007 es la única suite de oficina que lo soporta efectivamente, y la
especificación es tan compleja y llena de idiosincrasias que resulta muy costoso
implementarla para cualquiera que no sea Microsoft. Aquí también podemos
reconocer uno de los motivos de los recientes anuncios: la empresa necesita
convencer al mundo de que ha cambiado sus modales
[en el momento en el que OOXML está pasando una dura prueba en el hasta ahora infructuoso camino a convertirse en un estándar](http://tecnologia.infobaeprofesional.com/notas/62280-Microsoft-juega-la-ultima-batalla-en-la-guerra-por-los-formatos.html).

### ¿El vaso está medio lleno, o medio vacío?

Por cierto, las razones por las que Microsoft cambie o no su política de
interoperabilidad pueden ser interesantes desde el punto de análisis, pero son
irrelevantes a la hora de juzgar su efecto: lo importante es que lo haga. Veamos
entonces lo que Microsoft ha anunciado, y hasta qué punto facilita la
interoperabilidad con sus competidores, tal como le ordenó hacer la corte en la
Unión Europea.

Lo primero que uno esperaría encontrar en un anuncio que tiene conexiones
abiertas, portabilidad de datos y soporte a estándares entre sus principios
rectores es, precisamente, una promesa de respetar los estándares existentes.
Por ejemplo, Microsoft podría corregir su navegador, Internet Explorer, y sus
herramientas de desarrollo web, para que respete los estándares de la
[W3C](http://www.w3.org/), quien define los formatos y protocolos de la WWW. Eso
ahorraría a todos los usuarios de Internet los odiosos carteles de “Diseñado
para Explorer” que hoy se encuentran en muchos sitios.

Otro anuncio que parece necesario en este contexto es el abandono del proceso
estandarización de OOXML como formato separado, y el inicio de un esfuerzo para
desarrollar de ISO/IEC 26300 conjuntamente con el resto de la industria.
Lamentablemente, nada siquiera remotamente parecido a esto está en el anuncio.
Microsoft sólo promete documentar la manera en la que implementa estándares,
cuando lo hace, pero no promete respetarlos. De hecho, Microsoft ya dejó claro
que
[no se compromete a respetar el resultado de la estandarización de OOXML](http://blogs.msdn.com/brian_jones/archive/2007/07/12/spreadsheet-formula-bugs.aspx#3849462)
si en él hay alguna cosa que no le convenga, y nada parece haber cambiado en esa
postura.

Más allá de esta primera decepción, Microsoft está publicando, en forma
gratuita, la documentación de sus protocolos y formatos. El problema es que,
quizás fruto de las muchas veces que la comunidad de software libre tuvo que
explicar que libre y gratuito son cosas completamente diferentes, Microsoft
terminó por entenderlo: si bien no hay obstáculos al acceso a esta información,
no queda del todo claro que sea posible **usarla** libremente. Esto se debe a
que las especificaciones constituyen, a los ojos de Microsoft "valiosa propiedad
intelectual", y por lo tanto una cosa es mirarla, y otra tener permiso para
usarla. Para lo último, Microsoft ofrece a desarrolladores y usuarios licencias
en términos "razonables y no discriminatorios". En síntesis, esto quiere decir
que si yo escribo un programa basado en estas especificaciones generosamente
entregadas por Microsoft, es posible que mis clientes, o yo mismo, me encuentre
más adelante teniendo que pagar una licencia a Microsoft ¡por software que ellos
no escribieron!

Para comprobar la validez del último párrafo, vale la pena detenernos en la
"[promesa relacionada a patentes para desarrolladores open source](http://www.microsoft.com/interop/principles/osspatentpledge.mspx)".
Allí dice que Microsoft promete que no ejercerá sus patentes de software para
impedir el desarrollo de programas libres no comerciales que usen los protocolos
y formatos publicados, pero aclara expresamente que la única actividad a la que
esa promesa se aplica es al desarrollo, y no al **uso** del programa, o su
comercialización en cualquier forma.

### El contenido del vaso está podrido

No puedo negar que admiro la tenacidad de Microsoft: aún acorralados por la ley
y por sus propios usuarios, se las arreglan para montar un show de luces y
ofrecernos veneno envuelto para regalo. Y no lo digo yo: lo dice
[el Gartner Group](http://www.informationweek.com/news/showArticle.jhtml?articleID=206900525).

Un detalle interesante, sin embargo, es que la estrategia de Microsoft para
cobrar licencias por programas de otros no funciona en Argentina, ni en la mayor
parte de América Latina. Esto se debe a que está basada principalmente en
patentes de software, que en nuestros países son inválidas gracias a que
nuestras leyes de patentes explícitamente excluyen a los algoritmos y los
programas de computación de la posibilidad de ser patentados. Lamentablemente,
es posible que aquellos países que han firmado tratados de los que EEUU
irónicamente llama de “libre comercio”, como Chile, México y Costa Rica no
tengan tanta suerte.

Mi bola de cristal me dice que se aproxima una nueva ola de presión de parte de
EEUU para intentar forzarnos a aceptar las patentes de software, aún pese al
hecho de que
[los daños que las patentes de software han causado en su propio país](http://endsoftpatents.org/).
Ojalá nuestros representantes tengan la entereza de defender nuestros intereses
en ese trance.
