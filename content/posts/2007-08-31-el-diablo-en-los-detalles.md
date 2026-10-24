---
title: "El diablo en los detalles"
date: 2007-08-31
categories: ["Era digital", "Tecnocracia"]
---

Hace unos días, participé de una demo de
[la urna electrónica de Smartmatic-Sequoia](http://www.smartmatic.com/solutions_03.htm),
que una empresa local organizó en el marco de la edición 2007 de
[Congreso USUARIA](http://www.congresousuaria.org.ar/). La experiencia resultó
ser muy ilustrativa de los problemas que típicamente presentan la introducción
de sistemas de voto electrónico.

Comenzaré por decir que el sistema que estaban mostrando era francamente de lo
mejorcito que he visto en urnas electrónicas: el dispositivo era pequeño, daba
la impresión de ser sólido, la manera de usarlo era razonablemente sencilla, e
incluso imprimía boletas para ingresarlas en una urna y permitir el recuento
manual. Lamentablemente, como pasa casi siempre, el diablo está en los
detalles. 

### Cómo se vota

{{< figure src="/wp-content/uploads/2007/08/Boleta1.jpg" link="/wp-content/uploads/2007/08/Boleta1-Hires.jpg" alt="Boleta número 1" caption="Boleta número 1" >}}

El procedimiento para votar consta de varios pasos. Primero, el presidente de
mesa oprime un pulsador que habilita la máquina a emitir un voto. Esto es
importante, para evitar que alguien vote dos veces mientras nadie mira.

Una vez habilitada la urna, el votante interactúa con ella mediante dos
dispositivos de entrada/salida: una pantalla sensible al tacto, y una especie de
bandeja electrónica, también sensible al tacto, que está conectada a la urna.
Sobre la bandeja hay una hoja de papel, en la que están impresas las boletas que
representan las opciones disponibles al votante. Para seleccionar una opción, el
votante oprime un pequeño óvalo verde que se encuentra a un costado de la
opción, y conectada a ésta por una línea impresa. Cada opción elegida se refleja
en la pantalla, que muestra una copia de la imagen que el votante ve en la
bandeja.

Una vez elegidas todas las opciones, y verificado que las que se ven en pantalla
son las que eligió, el votante oprime un botón en ésta, que dice “votar”. La
urna muestra entonces un cartel que pide confirmación para emitir el voto, o
cancelación. Si el votante confirma, la impresora térmica emite una boleta que
contiene una imagen de cada una de las opciones elegidas. El votante puede
entonces introducir la boleta en una urna de cartón, que sirve para auditar
luego que los resultados coinciden.

### Primeras dudas

Revisando los pasos de más arriba, comienzan a aparecer algunas dudas. Dudas
menores, como la razón por la que la elección de una boleta se hace apuntando
_al lado_ de la boleta, y no a la boleta misma, o cuán fácil será enseñarle este
procedimiento a personas mayores o que no tienen experiencia de operar
equipamiento digital. También dudas un poco más fuertes: el precio de imprimir
cada boleta en papel térmico es mucho mayor que hacerlo usando impresión
tradicional, amén de que las impresiones térmicas tienen una vida útil muy corta
y muy dependiente de las condiciones ambientales.

También está el problema de que estos sistemas son mucho más frágiles que el
mecanismo actual. Las impresoras térmicas son dispositivos delicados, que aún en
las condiciones controladas de un cajero automático causan muchos dolores de
cabeza, mucho más aún en el contexto de una escuela que apenas está
acondicionada. ¿Qué haremos cuando una boleta salga mal impresa? ¿Cuando se
trabe el papel? ¿Cuando falle la energía por un tiempo prolongado?

Una inspección detallada de la boleta muestra una característica significativa:
la cabecera de la boleta tiene un código alfanumérico de esos que huelen a
criptografía desde cientos de metros de distancia. Es fácil imaginarse que ese
código puede usarse para verificar la integridad del voto, y vaya uno a saber
qué más.

Para no tener que imaginar nada, le pregunté a la persona que me estaba
mostrando la urna qué datos estaban codificados allí. La respuesta fue “¡La idea
es que eso sea secreto, así nadie puede hacer trampa!”

### Ahora sí estamos en problemas

Seguramente el buen señor estaba tratando de hacerme sentir seguro, pero
consiguió todo lo contrario. No era para menos: acababa de admitir que, a su
juicio, _quien sabe el secreto puede hacer trampa_.

Lógicamente, objeté que eso era un problema, porque lamentablemente hay
_alguien_ que conoce el secreto: la empresa fabricante y los empleados que
programaron la urna. Así las cosas, no es que _nadie_ puede hacer trampa: el
fabricante puede, probablemente también algunos de sus empleados, y también
cualquier persona u organización a quien puedan revelárselo, ya sea
vendiéndoselo, bajo extorsión, o por otras razones. Nuevamente una respuesta
inquietante: “Eso es cuestión de opiniones”.

Pensé en explicarle al señor que no se trata de opiniones, sino de un principio
elemental de seguridad informática, pero me di cuenta de que la conversación ya
no estaba bien encaminada, y de que este es un ejemplo típico del mayor problema
del voto electrónico: la confianza. Las empresas que venden urnas electrónicas
no parecen estar dispuestas a explicar por qué debemos confiar en sus productos,
simplemente nos piden que confiemos en que van a funcionar bien, y que van a ser
custodios dignos de los actos eleccionarios.

### Una última prueba

Curioso como soy, no pude evitar un experimento más. Pedí que me habilitaran
nuevamente para votar, y elegí una vez más los mismos candidatos. El resultado
fue esta nueva boleta:

{{< figure src="/wp-content/uploads/2007/08/Boleta2.jpg" link="/wp-content/uploads/2007/08/Boleta2-Hires.jpg" alt="Boleta número 2" caption="Boleta número 2" >}}

Una inspección minuciosa de ambas boletas revela que, si bien las opciones son
idénticas, el código que acompaña a cada una es diferente:

{{< figure src="/wp-content/uploads/2007/08/Boleta1-Cabecera.jpg" alt="Cabecera de boleta número uno" caption="Cabecera de boleta número uno" >}}
{{< figure src="/wp-content/uploads/2007/08/Boleta2-Cabecera.jpg" alt="Cabecera de boleta número dos" caption="Cabecera de boleta número dos" >}}

Esto no es sorprendente ni sospechoso: se me ocurren centenares de razones
legítimas por las que puede ser necesario que no haya boletas idénticas. Se
trata simplemente de que si el código de cada boleta es diferente, eso quiere
decir que la información representada por el código es más que las opciones del
votante. ¿Cuál es esa información? Si eso es un secreto, ¿cómo asegurarnos de
que no puede ser usada, por ejemplo, para identificar al emisor del voto
[como ocurrió en Ohio](http://www.vialibre.org.ar/2007/08/20/el-voto-secreto-no-tan-secreto/)?
Si no conocemos el algoritmo con el que fue generado, ¿cómo sabemos que es
seguro, o que
[no puede ser crackeado en un día usando hardware comprado por Internet](http://nsa.unaligned.org/)?

Por cierto, esto no se resuelve quitando el código (una solución que no lo
tuviera probablemente sería aún más vulnerable a falsificación de boletas), ni
se trata de pensar que las empresas que venden urnas electrónicas son parte de
una conspiración maligna. Lo esencial es que no podemos confiar en el acto
eleccionario, a menos que éste cuente con múltiples mecanismos de auditoría y de
control ciudadano.

Es importante que estos mecanismos puedan ser ejercidos por cualquier persona,
y no solamente por una elite de criptógrafos. Si los ciudadanos comunes no
podemos ejercer ese control, si debemos confiar a ciegas en que la matemagia
criptográfica y la integridad empresarial aseguran que no hubo fraude y
sanseacabó, nuestro voto pierde toda relevancia.
