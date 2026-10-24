---
title: "MS-OOXML: ¿compatibilidad hacia dónde?"
date: 2007-08-21
categories: ["Codicia", "Era digital"]
---

En 2006, la
[Organización Internacional para la Estandarización (ISO)](http://www.iso.org)
sancionó el estándar
[ISO/IEC 26300 (Open Document Format, ODF)](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=43485&ICS1=35&ICS2=240&ICS3=30)
para el almacenamiento e intercambio de documentos de oficina (procesamiento de
textos, hojas de cálculo, filminas para presentaciones). Este estándar alberga
la promesa de terminar la crónica pesadilla de compatibilidad que aqueja a estos
documentos, que hasta ahora sólo pueden ser compartidos sin pérdida de
información entre personas que usan idénticas versiones del mismo programa.
ISO 26300 está gozando de [amplia adopción](http://www.odfalliance.org/), tanto
por parte de usuarios como de implementadores.

Lamentablemente, uno de los implementadores, precisamente el que tiene mayor
participación en el mercado, se niega a adoptarlo. Microsoft argumenta que
ISO 26300 es insuficiente para representar fielmente el inmenso cuerpo existente
de documentos codificados en formatos binarios de Microsoft Office. Por eso
propone, a través de [ECMA](http://www.ecma-international.org/), el formato
[ECMA 376 (Office Open XML, OOXML)](http://www.ecma-international.org/publications/standards/Ecma-376.htm)
como estándar para la representación XML de dichos documentos.

Nadie duda de la utilidad de representar fielmente los documentos ya existentes,
pero no debemos olvidar que una representación sólo tiene sentido si es posible
interpretarla: los jeroglíficos egipcios sólo eran dibujos enigmáticos hasta el
descubrimiento de la
[Piedra de Rosetta](http://es.wikipedia.org/wiki/Piedra_de_Rosetta). 

Para poder determinar si ECMA 376 alcanza su objetivo de representar fielmente
los documentos de MS Office, entonces, la pregunta que debemos hacernos es: ¿es
posible, utilizando la información contenida en ECMA 376 y sin ayuda de
Microsoft, construir un programa que pueda _reproducir_ fielmente un archivo que
originalmente estaba codificado, por ejemplo, en formato .DOC?

### El problema a resolver

MS-OOXML representa la admisión, por parte de Microsoft, de que sus clientes no
están conformes con formatos binarios cuya especificación es secreta. Esa
disconformidad es fácil de explicar: el hecho de que el formato sea secreto
quiere decir que sólo la empresa que conoce el secreto puede ofrecer programas
que preserven toda la información contenida en el archivo, lo que tiene varias
consecuencias negativas para el usuario:

Dependencia de un proveedor monopólico

Al no tener competencia, Microsoft está en condiciones de dictar precios,
plazos, e incluso decisiones que deberían ser exclusivamente del cliente, como
por ejemplo la plataforma de hardware o, mucho más importante,
[su política de seguridad respecto de datos almacenados en las computadoras](http://boston.internet.com/news/article.php/1485861).

Fragilidad

Si pierde acceso a los programas de Microsoft, el cliente pierde acceso a _sus_
datos. Este acceso puede perderse por muchas razones, desde la insolvencia del
cliente hasta la desaparición de Microsoft, pasando por la posibilidad de que el
cliente viva en un país sobre el que el gobierno de EEUU declara un embargo o
incluso en virtud de
[errores de programación por parte de Microsoft](http://www.theregister.co.uk/2003/04/16/office_2000_sr1_registration_bug/).

El "impuesto Microsoft"

Debido al [efecto de red](http://es.wikipedia.org/wiki/Ley_de_Metcalfe), el
cliente a menudo se ve forzado a comprar o actualizar software de Microsoft
aunque no lo necesite, con el único objeto de leer los archivos que les envían
otras personas, empresas o reparticiones públicas que usan estos formatos.

Es claro, entonces, que el problema a resolver es representar los archivos
binarios de Microsoft Office _de tal modo que puedan ser fielmente reproducidos
por programas de otro proveedor_.

De lo contrario, si sólo los programas de Microsoft pueden hacerlo, hemos
invertido un esfuerzo enorme para terminar exactamente en la misma situación de
antes: partimos de un escenario en el que únicamente los programas de Microsoft
pueden reproducir con fidelidad archivos binarios, mientras que otros programas
pueden reproducirlos sólo imperfectamente, para llegar a otro en el que
únicamente programas de Microsoft pueden reproducir con fidelidad archivos XML,
mientras que otros programas puede reproducirlos sólo imperfectamente.

### Primera falla: los archivos originales siguen siendo inaccesibles

Un malentendido muy común acerca de ECMA 376 es la noción de que automáticamente
protege la inversión de los usuarios en millones de documentos codificados en
formatos de MS Office. Esto no es cierto: un programa que soporta MS-OOXML no
puede leer archivos en formato .DOC, o .XLS, o .PPT.

Un archivo de MS-Office recién es accesible en formato ECMA 376 una vez que fue
convertido a éste, y aquí tenemos el primer obstáculo: la única manera de
convertir, por ejemplo, del formato .DOC al formato .DOCX es usando
MS Office 2007 o posterior, ya que sólo Microsoft conoce los secretos necesarios
para realizar la conversión con fidelidad. Peor aun: por una decisión de
mercadeo de Microsoft, sólo las versiones profesionales (en otras palabras, las
más caras) de MS Office 2007 son capaces de hacer la conversión.

Queda claro entonces que ECMA 376 no es suficiente _en sí mismo_ para asegurar
la compatibilidad para atrás, sino que dicha compatibilidad depende, además, de
la calidad y disponibilidad de los conversores que Microsoft confeccione.

### Segunda falla: ¡el XML tampoco es accesible!

Microsoft argumenta que ECMA 376 es necesario porque no es posible traducir
algunas características de los formatos de MS Office a ODF. Lamentablemente,
dado que sólo Microsoft conoce todas las características de MS Office, es
imposible determinar la veracidad de esta afirmación. Sin embargo, la pobre
manera en la que MS-OOXML resuelve estas peculiaridades sugiere, en realidad,
que no lo intentaron con suficiente ahínco.

#### ¿Intraducible?

Es conocido que hay palabras intraducibles de un idioma a otro. Los alemanes,
por ejemplo, tienen el sustantivo “Gemütlichkeit”, que no tiene equivalente en
nuestra lengua. Tracemos un paralelo entre esta situación y la de .DOC, MS-OOXML
y ODF: supongamos que .DOC es Alemán, y que MS-OOXML y ODF son distintas maneras
de traducirlo al Castellano. ¿Qué pasa cuando queremos traducir la frase “Das
Haus ist gemütlich”?

Dado que la palabra “gemütlich” no tiene traducción al Castellano, la propuesta
de MS-OOXML es traducirlo como “La casa es (intraducible del Alemán:
gemütlich)”. Es cierto que de esta manera no se pierde ninguna fidelidad
respecto de la frase original. Lamentablemente, sigue siendo imposible entender
cómo es la casa a menos que uno sepa Alemán.

Una alternativa más útil sería, en cambio, traducirlo como “la casa induce
bienestar”. Hemos tenido que reestructurar la gramática de la frase, adaptarla
de modo que sea más afín al contexto castellano, reemplazar el verbo “ser” por
“inducir”, pero hemos logrado representar fielmente el sentido original de tal
modo que cualquier persona que sepa Castellano puede entenderlo.

En otras palabras: MS-OOXML no se toma el trabajo necesario para que podamos
entenderlo.

#### Ejemplo: fechas incorrectas

Uno de los aspectos más bochornosos de OOXML es su manejo de fechas. De acuerdo
a ECMA 376, el año 1900 debe ser considerado bisiesto pese a que, según el
calendario gregoriano que es la base de
[ISO 8601](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=40874&ICS1=1&ICS2=140&ICS3=30)
(representación de fechas), no lo fue.

Aparentemente,
[este tratamiento erróneo del año 1900 se debe a un error de programación en la difunta hoja de cálculo Lotus 1-2-3](http://support.microsoft.com/kb/214326).
Cuando Microsoft diseñó Excel, decidió duplicar este error, para evitar
incompatibilidad con Lotus 1-2-3, y hoy pretende inmortalizarlo en un estándar
internacional.

Amén de la contradicción con estándares preexistentes, esta “solución” al
problema es un innecesario obstáculo a la compatibilidad: al definir las fechas
de modo erróneo, se vuelve muy difícil convertir fechas de OOXML a otros
formatos.

Este problema podría haber sido salvado fácilmente por Microsoft, proponiendo
que se agregue a las hojas de cálculo de OOXML un atributo
“LotusLeapYearBug=true”. Las planillas traducidas a OOXML desde el formato .XLS
tendrían este atributo y observarían el comportamiento erróneo, mientras que las
nuevas no lo tendrían y manejarían las fechas del modo correcto.

#### Ejemplo: tipos de borde

Una de las funciones de Microsoft Word permite al usuario especificar una
decoración para el borde de las páginas. Lamentablemente, esta característica
fue muy pobremente diseñada: sólo permite que el usuario elija de entre un
conjunto predeterminado de diseños para el borde, identificadas por nombre:
“apples” produce un borde de manzanas, “babyPacifier” produce un borde de
chupetes para bebé, etc. ECMA 376 dedica más de cincuenta páginas (2414 a 2465
en
[el PDF originalmente publicado](http://web.mit.edu/~stevenj/www/ecma376.html))
a enumerar y proveer ejemplos de las distintas imágenes posibles.

Por cierto, esta no es la única manera de especificar un borde, y de hecho dista
muchísimo de ser la mejor manera de hacerlo. Peor aún: dado que las imágenes a
usar son parte de MS Office, están bajo derecho de autor de Microsoft, de modo
que es imposible hacer un programa que reproduzca fielmente documentos que
contengan esta característica sin obtener previamente una licencia de Microsoft.

Mucho más sencillo y general hubiera sido hacer que el conversor de formato de
.DOC a .DOCX recodificara la especificación de borde de tal modo que incluyera
en el archivo una copia de las imágenes a usar en el borde. Esto no sólo sería
lo suficientemente general como para ser implementado por cualquiera, sino que
reduciría el tamaño de la especificación en 50 páginas (¡casi el 1%!), y tendría
el beneficio adicional de permitir a los usuarios utilizar también imágenes
distintas de las predefinidas por MS Word.

#### Ejemplo: autoSpaceLikeWord95, truncateFontHeightsLikeWP6 y otros

En varios casos, MS-OOXML recurre a referencias al comportamiento de otros
programas para definir el significado de una directiva. Un ejemplo es la
etiqueta autoSpaceLikeWord95, que indica que los caracteres asiáticos que
componen el párrafo deben ser presentados con el mismo esquema de espacios que
usaba el programa MS Word 95. Lamentablemente, Microsoft es la única que conocen
el funcionamiento de ese esquema. Una persona que intente interpretar fielmente
esta etiqueta trabajando fuera de Microsoft no tiene más remedio que adivinar
cómo funcionaba ese programa, tarea que es entre muy difícil e imposible.

Microsoft argumenta que el soporte de esa etiqueta es opcional, y que por lo
tanto no es necesario interpretarla correctamente para satisfacer el estándar:
basta con ignorarla. El problema es que un programa que la ignore evidentemente
no alcanzará el objetivo de "representar fielmente" el documento, mientras que
Microsoft sí puede hacerlo.

La estrategia de recurrir a estas etiquetas, una vez más, no es la única y mucho
menos la mejor manera de traducir la codificación binaria de MS Office a XML.
Mucho más correcto hubiera sido utilizar una etiqueta genérica de espaciado de
caracteres, que permitiera especificar exactamente cómo deben ser colocados. De
esa manera, el comportamiento indocumentado de Word 95 quedaría oculto dentro
del programa de conversión, y cualquier programa que interpretara correctamente
las directivas de espaciamiento podría reproducir el documento con fidelidad.

### ECMA 376 está mal especificado, y es innecesario

Hemos explorado algunos ejemplos que ilustran el pobre diseño de ECMA 376, y
cómo esas falencias conspiran contra el objetivo que MS-OOXML se puso a sí
mismo: hacer posible la representación fidedigna del historial de documentos
codificados en formatos binarios de MS Office. También hemos visto que estas
falencias no son inevitables, y que es posible resolverlas sin entorpecer la
posibilidad de terceros de implementar e interoperar con el estándar. Quedaron
sin mencionar una multitud de otras taras innecesarias del formato, como el uso
de máscaras de bits, conflictos de validación de XML, conflictos con varios
estándares preexistentes y muchas más.

Queda establecido así que ECMA 376 no alcanza su propio objetivo. Queda aún por
determinar, en realidad, si la existencia de este estándar está justificada: ¿es
necesario un estándar nuevo al solo efecto de "representar fielmente" documentos
preexistentes, o es posible hacerlo usando ODF, que ya es un estándar ISO?

Microsoft no ha conseguido mostrar nada que MS-OOXML haga mejor que ODF. Incluso
aspectos exóticos del formato, como “autoSpaceLikeWord95”, deberían ser
codificables de una manera más general en ODF, por ejemplo usando el atributo
“style:font-independent-line-spacing”. Si bien es posible que quienes diseñaron
ODF no hayan tenido en cuenta alguna peculiaridad incómoda de los formatos de
MS Office (a ninguna persona en su sano juicio se le ocurre hacer una
especificación de fechas que contradiga el calendario, por ejemplo), esos son
detalles que fácilmente pueden resolverse produciendo una nueva revisión de
ISO 26300 para que las contemple.

De hecho, hubiera sido interesante que Microsoft hubiera participado activamente
en el proceso de estandarización de ISO 26300, pidiendo que se incluyeran los
elementos necesarios para preservar las idiosincrasias de MS Office, en vez de
callar en ese momento, y hoy pedir un estándar hecho exclusivamente a su medida,
que nadie más puede implementar, y que ni siquiera alcanza al objetivo propuesto
por ellos mismos.
