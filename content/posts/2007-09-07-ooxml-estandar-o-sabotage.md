---
title: "OOXML: ¿estándar o acto de sabotaje?"
date: 2007-09-07
categories: ["Codicia", "Era digital"]
---

Es difícil describir los esfuerzos de Microsoft para lograr que
[ECMA 376 (Office Open XML, OOXML)](http://www.ecma-international.org/publications/standards/Ecma-376.htm)
fuera aprobado por [ISO](http://www.iso.org/) sin recurrir al adjetivo
“desesperados”. En cada instancia, la transnacional de software demostró estar
dispuesta a
[subvertir todas las reglas de comportamiento civilizado](http://www.consortiuminfo.org/standardsblog/article.php?story=20070828095140796)
con tal de salirse con la suya. ¿De qué otra manera describir a las acciones de
una empresa que no sólo llega al extremo de
[comprar los votos que no puede conseguir mediante persuasión](http://ec.europa.eu/idabc/en/document/7186),
sino que además lo hace de manera tan torpe como para que los descubran,
exponiendo al prestigioso Instituto Sueco de Estándares (SIS) al bochorno
internacional de tener que
[declarar inválido su propio voto](http://www.betanews.com/article/Swedish_Standards_Vote_on_OOXML_Declared_Invalid_SIS_to_Abstain/1188577813)?
¿Cómo explicar la sorpresiva inscripción de
[11 nuevos miembros participantes en JCT 1](http://www.consortiuminfo.org/standardsblog/article.php?story=20070831072521575)
(el comité a cargo de la evaluación de OOXML) justo a tiempo para la votación,
[nueve de los cuales votaron a favor](http://www.consortiuminfo.org/standardsblog/article.php?story=20070903110826712)?
¿Por qué sometieron al escrutinio público un formato
[claramente inmaduro](http://www.grokdoc.net/index.php/EOOXML_objections)?

La pregunta más interesante de esta historia, sin embargo, es otra: ¿qué es lo
que impulsa a Microsoft cometer semejantes tropelías para forzar la adopción de
OOXML como estándar ISO? Al fin y al cabo, la participación de mercado de los
programas de oficina de Microsoft es equivalente a un monopolio, y ellos mismos
no se cansan de alardear de que constituyen el “estándar de mercado”. Hasta
ahora, las externalidades de red y una política de mercadeo que combinó la
saturación publicitaria con la tolerancia de las copias truchas les bastaron
como herramientas para imponer sus formatos, sin necesidad de la bendición de
organismos burocráticos y participativos como ISO. ¿Qué cambió? ¿Cómo pasó
Microsoft de ignorar a ISO a pretender cooptarla? 

### Los clientes se están avivando

Durante muchos tiempo, los usuarios de computadoras aceptaron la
incompatibilidad de datos entre programas como algo inevitable. Era algo
parecido a lo que pasaba con las distintas normas de cintas de vídeo, o con el
problema que habían enfrentado al no poder escuchar más sus discos de vinilo
cuando se popularizó el CD. Nada podía hacerse respecto del hecho de que si
escribo un documento con el programa A, el único programa con el que lo puedo
leer bien es A.

A principios de los '90, la popularización de Internet trajo muchas maravillas a
nuestros hogares. Tantas, que la mayor de ellas demoró mucho en volverse
evidente: el hecho de que todos podemos usar Internet, independientemente de la
computadora o el software que usemos. Un correo electrónico enviado desde
cualquier programa puede ser leído por cualquier otro, independientemente del
fabricante de la máquina o el autor del software. Un sitio web puede ser
visitado usando cualquier máquina que tenga un navegador, independientemente de
cuáles programas sean los que manejan el sitio.

Esta es, por cierto, la característica que define a Internet. Antes de ella,
existían ya muchas redes informáticas, pero todas ellas eran de una manera u
otra “propiedad” de alguna compañía, y las máquinas de un fabricante tenían
muchas dificultades para comunicarse con las de cualquier otro. Internet
demostró, por construcción, que era posible establecer un conjunto de protocolos
y formatos estándar que permitieran codificar y transmitir los datos de tal
manera que no estuvieran atados a un determinado proveedor, y esa es la clave de
su éxito.

No podía pasar mucho tiempo sin que algunos usuarios comenzaran a preguntarse
por qué esta independencia entre los datos y los programas no era más
generalizada. En particular, muchas empresas y administraciones públicas cayeron
en la cuenta de que esa dependencia representa un riesgo inaceptable: perder
acceso al programa (por ejemplo, porque la empresa que lo producía lo
discontinúa) significa perder el acceso a los datos.

Así, es comprensible que cada vez más organizaciones estatales y privadas estén
fijando
[políticas de adquisición de software que exigen el soporte de formatos y protocolos estándar y abiertos](http://flosspols.org/deliverables/D04HTML/FLOSSPOLS-D04-openstandards-v6.html).
El año pasado, al cabo de un proceso que duró cinco años, ISO sancionó el
estándar
[ISO/IEC 26300 (Open Document Format, ODF)](http://www.iso.org/iso/en/CatalogueDetailPage.CatalogueDetail?CSNUMBER=43485&ICS1=35&ICS2=240&ICS3=30),
que define un formato de archivos interoperable para almacenar archivos de
texto (ODT), planillas de cálculo (ODS) y presentaciones (ODP). Ya existen
programas de distintos proveedores que soportan ODF, y los usuarios de
cualquiera de ellos pueden compartir datos con los usuarios de cualquier otro.

### La vaca atada

Esto no le gusta nada a Microsoft. De hecho, ya Internet le había caído bastante
pesada: ellos tenían planes de construir una red a la que sólo se pudiera
acceder usando Windows, y el inesperado éxito de Internet los dejó con la
cuchara en la mano, esperando una lluvia de sopa que nunca llegó.

A eso se debió que Microsoft recurriera a prácticas de mercadeo que le valieron
condenas por abuso de poder monopólico en
[EEUU](http://www.usdoj.gov/atr/cases/f200400/200457.htm) y en
[Europa](http://news.com.com/Europe+plays+hardball+with+Microsoft/2009-1016_3-5178068.html),
al sólo efecto de forzar la penetración de Internet Explorer. El objetivo era
lograr que los usuarios tuvieran en su escritorio, por defecto, un navegador que
deliberadamente se aparta de los estándares y muestra mejor los sitios
desarrollados con herramientas de Microsoft que los que están hechos con otras
herramientas.

Pero si la interoperabilidad de páginas web
[ya es un problema para Microsoft](http://edge-op.org/iowa/www.iowaconsumercase.org/011607/2000/PX02991.pdf),
la de documentos de oficina es una amenaza directa a su fuente principal de
ingresos: la venta de licencias a usuarios que no pueden darse el lujo de
negarse a pagar, porque tienen miles de documentos guardados en formatos de
MS Office, y no pueden leerlos fielmente con otros programas. Para estos
usuarios, un formato estándar representa la promesa de salir de la dependencia:
es cierto que deberán hacer un esfuerzo de conversión de formatos pero, una vez
saltado este obstáculo, podrán nuevamente elegir entre varios proveedores, en
vez de tener que someterse a lo que Microsoft quiera entregar y cobrar.

Precisamente por eso, Microsoft prefiere hacer el ridículo frente a la comunidad
mundial de informática y negocios antes que dar soporte a un formato estándar
verdaderamente abierto e interoperable. Literalmente, se les va la vida en ello.

### Juegos de palabras

¿Que hacer entonces en un contexto en el que los usuarios corporativos
(justamente los más dependientes de Microsoft hasta ahora) exigen soluciones
estándar e interoperables? La respuesta lógica parecería ser “darle a los
clientes lo que piden”. Pero Microsoft vive en el País de las Maravillas, y
prefiere la solución de Humpty Dumpty: cambiar el significado de las palabras.
Cuando Microsoft dice palabras como “estándar”, “interoperabilidad” o “abierto”,
están usando significados distintos de los que usa el resto del mundo.

La función de un estándar es, esencialmente, facilitar las comunicaciones entre
entidades distintas. Gracias a que existen estándares de pesos y medidas, una
empresa china puede comprar una tonelada de soja a un agricultor argentino y
saber exactamente qué va a recibir. Gracias a que existen estándares de pasos de
rosca, podemos comprar tornillos a un proveedor y tuercas a otro, sabiendo que
todo va a funcionar.

Presionados para soportar formatos estándar internacionales, Microsoft decidió
que sólo lo harían si se trata del suyo propio: un formato que, según su propia
caracterización, está diseñado con el único propósito de facilitar la
comunicación _con ellos mismos_. OOXML se ocupa solamente de preservar la
información almacenada entre distintas versiones de MS Office, sin prestar
atención al problema de interoperabilidad con otros programas (y puede
argumentarse que algunas de las características de OOXML están pensadas
precisamente para obstaculizarla). En otras palabras: un estándar que no
estandariza.

Microsoft esperaba que, utilizando a ECMA para introducir su formato en el
proceso _fast-track_, diseñado para revisar formatos estables y maduros, ISO
pasaría por alto el hecho de que no es necesario un estándar internacional para
que una persona se comunique con sí misma, y no tendría en cuenta las múltiples
falencias del formato. Convirtiendo a OOXML en un estándar ISO, Microsoft podría
hacer una mofa del concepto, anunciando que sus programas soportan un estándar
internacional, y al mismo tiempo negándole a sus clientes el real beneficio de
la estandarización, la interoperabilidad.

Afortunadamente, ISO demostró hasta ahora estar a la altura de las
circunstancias, y si bien las maniobras de Microsoft lograron distorsionar los
resultados,
[esa distorsión sigue sin ser suficiente para descarrilar el proceso de estandarización](http://www.iso.org/iso/pressrelease.htm?refid=Ref1070).
