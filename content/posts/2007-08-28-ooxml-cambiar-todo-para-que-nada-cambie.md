---
title: "OOXML: cambiarlo todo para que nada cambie"
date: 2007-08-28
categories: ["Codicia", "Era digital"]
---

Microsoft y ECMA no se cansan de repetir que el objetivo de
[ECMA 376 (Office Open XML, OOXML)](http://www.ecma-international.org/publications/standards/Ecma-376.htm)
es representar fielmente los millones de documentos que hoy están almacenados en
formatos inaccesibles, como .DOC, .XLS y .PPT. Es interesante ver a Microsoft
finalmente admitiendo que sus formatos tradicionales no son apropiados para
almacenamiento de información que deba sobrevivir el mediano plazo, o a los que
sea necesario acceder desde otros programas.

Dada esta admisión, y el objetivo de permitir acceso a inversiones millonarias
en documentos que están hoy en formatos “heredados” (una manera elegante de
decir “obsoletos), lo lógico hubiera sido que Microsoft participara en el
[esfuerzo de estandarización abierto](http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=office)
que la
[Organization for the Advancement of Structured Information Standards (OASIS)](http://www.oasis-open.org/)
emprendió en 2002 para construir lo que hoy es
[ISO/IEC 26300 (Open Document Format, ODF)](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=43485&ICS1=35&ICS2=240&ICS3=30).
De esa manera, hubieran podido criticar las propuestas allí hechas y proponer
mecanismos para que sus documentos heredados pudieran ser codificados en el
estándar.

Lamentablemente, lo que hizo fue muy distinto: calló durante todo el proceso de
definición de ODF, pese a estar invitada a participar, y recién cuatro años
después presentó un formato definido enteramente dentro de la misma empresa, sin
participación de terceros. Este formato, que hoy se presenta como candidato a
estándar ISO, representa según Microsoft la llave para que los usuarios
preserven millones de documentos para el futuro. Eso sí: el negocio de la
preservación, de la lectura de los datos preservados y de la confección de
programas que los procesen queda vedado, mediante múltiples mecanismos, a todos
sus potenciales competidores. 

### El proceso de traducción está bajo control de Microsoft

Los documentos heredados no están directamente disponibles para todos, como las
comunicaciones de ECMA y Microsoft parecen sostener. Antes de acceder a un
documento que originalmente estaba en formato .DOC, por ejemplo, es necesario
primero guardarlo en formato .DOCX. Dado que sólo Microsoft conoce el formato
.DOC en profundidad, es claro que sólo sus programas estarán en condiciones de
hacer esta traducción.

En otras palabras, la preservación de los datos en el futuro tiene un precio:
sólo aquellos usuarios que estén dispuestos a adquirir licencias de Microsoft
Office 2007 Professional podrán convertir sus viejos documentos al nuevo
formato. Los demás, deberán conformarse con los formatos que Microsoft mismo
reconoce como inadecuados.

### La calidad de la traducción está bajo control de Microsoft

Pero no sólo el mercado de la traducción a ECMA 376 está firmemente en manos de
Microsoft: también lo está el control sobre su calidad. Dado que ellos son
quienes realizan la traducción, pueden escribir sus programas de tal modo que la
traducción sea ligeramente errónea, y compensar los errores cuando los leen.
Como sus programas leen bien los archivos que ellos mismos escriben, y nadie
puede auditar el mecanismo de traducción ni el de lectura, se vuelve muy difícil
demostrar que la traducción es errónea, y así se garantizan que todo sigue
igual: la única manera de leer fielmente los documentos producidos por MS Office
es usando MS Office.

Peor aún, como la lectura está implementada de manera tal de ser fiel a la
traducción, pero no al estándar como está escrito, se aseguran también de que
sea sumamente difícil escribir programas que produzcan OOXML que luego sea leído
correctamente por MS Office. Esto llega tan lejos que podemos afirmar que no
existen documentos acordes a ECMA 376, ya que
[ni siquiera Microsoft los escribe o lee correctamente](http://www.arstdesign.com/articles/OOXML-is-defective-by-design.html).

### Una implementación externa a Microsoft será necesariamente cara e incompleta

Esto se debe no sólo a que
[ECMA 376 contiene numerosos errores, características mal documentadas y comportamientos anómalos](http://www.vialibre.org.ar/2007/08/21/ms-ooxml-compatibilidad-hacia-donde/),
sino también al hecho de que ignora estándares preexistentes. Esto tiene un
enorme impacto en los costos de implementación de un programa que soporte el
formato.

Por ejemplo, ISO 26300 utiliza el estándar
[Scalable Vector Graphics (SVG)](http://www.w3.org/Graphics/SVG/) del
[World Wide Web Consortium (W3C)](http://www.w3.org/) para representar dibujos
vectoriales, [MathML](http://www.w3.org/Math/) para representar fórmulas
matemáticas, etc. Esto garantiza que las representaciones son bien comprendidas,
que los formatos son mantenidos al día, y que hay bibliotecas a las que un
implementador puede recurrir, ahorrándose la inversión de tener que escribirlas
desde cero. De hecho, hay bibliotecas disponibles para procesar ISO 26300 que
resuelven toda la codificación/decodificación, y que pueden ser usados por
cualquiera para sus propios programas. Por el contrario, OOXML recurre a
formatos no estándar para las mismas tareas, llegando al extremo de usar varios
de ellos, incompatibles entre sí, para un único propósito. En lugar de SVG, por
ejemplo, usan tres formatos distintos: Windows Metafile, DrawingML y VML (este
último
[fue propuesto por Microsoft a W3C en 1998](http://www.w3.org/TR/NOTE-VML.html),
fue rechazado, y sin embargo aparece en ECMA 376). Lo mismo pasa con formulas
matemáticas, fechas, mecanismos de cifrado, códigos de país, unidades de medida
y otros: para todo hay que escribir una biblioteca nueva, cuando podríamos
re-usar las que ya tenemos.

### ¿Rescatar los datos para quién?

Dadas estas condiciones, resulta evidente que ECMA 376 no cumple con su promesa
de liberar a los datos de los usuarios de su actual prisión en formatos
obsoletos. Tan sólo es una prisión ligeramente más grande, un poco más holgada,
pero igual de hermética, y en la que sólo pueden entrar los productos de
Microsoft.

Esto no es ninguna sorpresa: se trata de una estrategia deliberada, fomentada
dentro de Microsoft por su propio fundador, como puede leerse en
[un e-mail de Bill Gates que vio la luz durante un juicio por abuso de poder monopólico en el estado de Iowa](http://edge-op.org/iowa/www.iowaconsumercase.org/011607/2000/PX02991.pdf):

> Algo que debemos cambiar es nuestra estrategia — permitir que los documentos
> de Office se vean bien en los navegadores de otras personas es una de las
> cosas más destructivas que podemos hacerle a la compañía.
>
> Debemos dejar de poner esfuerzo en esto, y asegurarnos de que los documentos
> de Office dependan fuertemente de características privativas de Internet
> Explorer.
>
> Cualquier otra cosa es suicidio para nuestra plataforma. Este es un caso en el
> que Office debe evitar hacer algo que destruiría a Windows.

En otras palabras, Microsoft quiere rescatar los datos de los usuarios, pero no
para ellos, sino para sí misma.

### El camino es el de los estándares abiertos

Con algo de suerte, viento a favor y bastante ayuda de su madrina
multimillonaria, es posible que ECMA 376 se convierta en un estándar ISO. ¿Basta
con eso para que podamos confiarle nuestros datos y quedarnos tranquilos de que
ahora son accesibles y perennes? Evidentemente, no. No basta con que un formato
sea estándar, es necesario que sea un estándar _abierto_: con múltiples
implementaciones (en el caso de ECMA 376, sería un gran avance el que hubiera
al menos una), sin restricciones y con documentación completa.

ISO 26300 cumple con todas estas condiciones, y ofrece un camino de salida a la
dependencia de proveedores únicos. ECMA 376, en cambio, merece ser ignorado para
todo fin que no sea ilustrar la definición de “gatopardismo”: cambiarlo todo
para que nada cambie.
