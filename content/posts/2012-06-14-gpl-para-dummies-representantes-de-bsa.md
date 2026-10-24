---
title: "GPL para <del>dummies</del> representantes de BSA"
date: 2012-06-14
categories: ["Codicia", "Era digital", "Ontodoncias"]
---

La General Public License (GPL) es un ejemplo de claridad. La
[versión 3](http://www.gnu.org/copyleft/gpl.html), que es la más complicada de
todas, tiene apenas 18 artículos, todos dedicados a _otorgar permisos que el
usuario de otro modo no tendría_[^1], tiene un preámbulo escrito en lenguaje muy
sencillo explicando su intención, y está construida de tal manera que el
esfuerzo requerido para violarla está fuera de la capacidad de la mayoría de los
usuarios.

Sin embargo, hay gente que aparentemente sigue sin entenderla. Es curioso que
las personas a las que más les cuesta son presuntos especialistas en
“[propiedad intelectual](http://www.gnu.org/philosophy/not-ipr.es.html)” que
llevan ya mucho tiempo dedicados a oponerse a ella, alguno de ellos culpable
incluso de un (bochornoso) libro al respecto. Según los representantes de la
Business Software Alliance (BSA),
[la GPL es peligrosa y hasta abusiva](http://www.carranzatorres.com.ar/index.php?option=com_content&view=article&id=790:iconoce-bien-cual-es-el-verdadero-costo-del-software-libre&catid=108:notas-de-prensa&Itemid=188)[^2],
porque su verdadero costo es que “nos obliga a renunciar por anticipado a los
derechos patrimoniales de autor que la ley reconoce sobre\[sic!\] quien haga
obras derivadas”[^3]. Para llegar a esta conclusión, hacen una lectura de la GPL
que es mucho más digna de [Man Ray](http://en.wikipedia.org/wiki/Man_Ray) que de
un consultor legal.

Por cierto, aquí se aplica la máxima de Upton Sinclair, cuando decía que “es muy
difícil lograr que una persona entienda algo cuando su salario depende de no
entenderlo”. Pero siempre cabe el riesgo de que algún lector poco avisado lea lo
que escriben, y crea entrever un atisbo de verdad escondido entre los vericuetos
de su retórica. Así que me propuse hacer una explicación de la GPL tan sencilla
que hasta alguien que trabaja para la BSA pueda entenderla. Usa
dibujitos[^4]. 

Para ponernos en contexto, vale la pena mirar primero cuáles son las opciones
del usuario cuando usa software cuyo uso está condicionado a la aceptación de un
Contrato de Licencia de Usuario Final (CLUF) como los que usan las empresas
nucleadas en BSA:

{{< figure src="/wp-content/uploads/2012/06/privativo-167x300.png" link="/wp-content/uploads/2012/06/privativo.png" alt="Diagrama mostrando las opciones de un usuario de software privativo" caption="Diagrama mostrando las opciones de un usuario de software privativo" >}}

Según vemos claramente en el diagrama de la izquierda (click para ampliarlo), el
usuario que necesita un programa privativo sólo tiene dos maneras de acceder a
él: o bien paga, acepta un contrato leonino, acepta que se lo cambien
unilateralmente en cualquier momento, _y_ permite que lo auditen todas las veces
que se les dé la gana, o viola la ley, usando una copia trucha. Por cierto, esta
segunda opción no debería ser parte del diagrama, pero dado que la misma BSA
constantemente lamenta la enorme cantidad de gente que opta por esta
alternativa, no queda más remedio que incluirla.

Dos detalles que vale la pena destacar: uno, estas son todas decisiones que el
usuario debe tomar _antes de siquiera usar el programa_, y dos, parte del
contrato leonino antes mencionado (el CLUF) se dedica a prohibir expresamente la
confección de obras derivadas. Aquí tenemos, efectivamente, una renuncia “por
anticipado”, pero no a los derechos patrimoniales sobre una potencial obra
derivada futura, sino a la mera posibilidad de confeccionarla.

Así es que, si necesito mejorar algún aspecto del programa privativo, sólo puedo
hacerlo si el cambio es posible sin acceso al [código fuente]({{< ref
"2006-05-21-codigofuente.md" >}}), y además decido violar la letra del contrato
que acepté[^5], lo que inmediatamente convierte al resultado de la mejora en
software trucho, independientemente de cómo fue adquirido. Y ni hablar de qué
pasa si quiero distribuir el software: eso sólo es posible violando la ley, a lo
que ya estamos acostumbrándonos, pero es mucho más riesgoso que la adquisición
de software por esa vía, porque es mucho más fácil que te descubran.

Abandonemos por un momento el (según la BSA) idílico mundo del software
privativo, e internémonos en las oscuras profundidades del “totalitario”
([BSA dixit](http://www.carranzatorres.com.ar/index.php?option=com_content&view=article&id=788:ilicencia-libre-para-su-software&catid=108:notas-de-prensa&Itemid=188))
mundo del software libre, para ver cuáles son allí las opciones del usuario:

{{< figure src="/wp-content/uploads/2012/06/libre-162x300.png" link="/wp-content/uploads/2012/06/libre.png" alt="Diagrama que describe las opciones de un usuario de software libre" caption="Diagrama que describe las opciones de un usuario de software libre" >}}

Lo primero que notamos aquí es que nada separa al usuario del software que
necesita. Si puede y quiere pagar, paga, de lo contrario tiene otras maneras de
obtenerlo[^6]. El usuario no sólo carece aquí de la tentación de violar la ley,
sencillamente _no tiene manera de hacerlo, aunque quiera_. De hecho, cuando un
programa es libre, la licencia ni siquiera es necesaria: incluso la temida GPL
reconoce en su artículo 9 que el usuario puede obtener y usar copias del
programa sin siquiera tener que aceptarla. En software libre tenemos cero
“[piratería](http://www.gnu.org/philosophy/words-to-avoid.es.html#Piracy)” (para
usar su término). ¡Ya quisiera la BSA!

Lo mismo ocurre cuando el usuario decide que necesita mejorar el programa: si
dispone de los recursos necesarios para hacerlo, sólo tiene que decidirlo: nada
se lo impide, ni siquiera la necesidad de acceder al código fuente.

La licencia recién se vuelve necesaria cuando uno decide que quiere _distribuir_
el resultado de las mejoras que hizo (nótese cuán lejos está este punto del
concepto de “por anticipado). A diferencia del caso privativo, en el software
libre hay varios caminos que permiten publicar la obra derivada sin conflicto.
El caso más sencillo es, por cierto, el del software libre no-copyleft
(distribuido bajo licencias como
[BSD](http://www.opensource.org/licenses/BSD-3-Clause),
[Apache](http://www.apache.org/licenses/LICENSE-2.0.html), etc), que ni siquiera
plantean restricciones a la publicación, seguido por el caso del software
copyleft cuando yo de todos modos quiero distribuirlo como software libre, en el
cual tampoco hay obstáculos de ninguna especie[^7].

¿Pero qué pasa con el software copyleft, incluyendo la “totalitaria” GPL, cuando
_no_ quiero distribuir la obra derivada como software libre? Lejos de lo que
sugieren sus detractores, aún para este caso existen maneras en las que el autor
puede mantener intactos sus preciados derechos patrimoniales.

La primera (y es llamativo que BSA no la mencione jamás) consiste, simplemente,
en reemplazar todo el código ajeno en el programa que quiero distribuir por
código escrito por mí. Es perfectamente lógico: GPL no restringe (ni puede
restringir) la distribución del código escrito por el usuario. Lo que prohíbe es
la distribución de _código GPL_ bajo condiciones no libres. Lo que en realidad
protesta BSA no es que GPL no permite distribuir código propio bajo condiciones
no libres, sino _código ajeno_.

Si tan valiosa es la contribución del usuario, y tanto valora sus propios
derechos patrimoniales sobre ella, todo lo que tiene que hacer es tomar el
programa, identificar todas las partes GPL que contiene, y escribir su propia
versión de ellas. Así, contará con un programa que es enteramente de su autoría,
y podrá distribuirlo bajo las condiciones que se le antoje (y la ley le
permita).

¿Y qué pasa si el usuario no quiere reemplazar el código GPL en el programa?
Nada grave, en realidad, y mucho menos algo que implique renunciar a sus
derechos patrimoniales. Todavía le queda el recurso de negociar condiciones
especiales con los autores de las porciones GPL del programa resultante, lo que
en algunos casos es
[muy sencillo](http://www.mysql.com/about/legal/licensing/oem/) y en otros
[prácticamente imposible](http://kernel.org/). Recién si eso falla, queda
bloqueada la posibilidad de publicación como software no-libre. Y la no
publicación es, por cierto, uno de los derechos patrimoniales del autor, que
siguen quedando intactos.

¿Quién era el “totalitario”, al final?

[^1]:
    Salvo uno, el 8, que establece las condiciones bajo las cuales algunos de
    estos derechos pueden ser rescindidos.

[^2]: Detalle divertido: ¡ese sitio está hecho con software libre!

[^3]:
    Es refrescante, por cierto, ver a gente de la BSA mencionando la confección
    de obras derivadas como algo valioso y necesario para el usuario, que lo es.
    Es una lástima que las empresas que la componen hagan todo lo que está bajo
    su poder para impedir que sus usuarios puedan llevarlas a cabo.

[^4]:
    Y no cualquier dibujito: gráficos hechos por el maravilloso (y _muy_
    paciente) [derechoaleer](http://www.derechoaleer.org/), que usó
    [Inkscape](http://inkscape.org/) para traducir mis garabatos en diagramas
    hermosos. Es software libre, por supuesto, y hasta las tipografías son
    libres. ¡Muchas gracias!

[^5]:
    Algo curioso: en este caso, los que acceden al programa por la vía trucha
    están en mejores condiciones que los que lo adquirieron legítimamente,
    ¡porque nunca aceptaron el contrato!

[^6]:
    Nos referimos aquí, como en el caso privativo, a software que ya existe y
    está publicado. El caso en el que el software no existe aún es más complejo
    para ambos, y lo dejaremos para otro artículo

[^7]:
    Vale la pena aclarar que publicar algo bajo una licencia copyleft _no
    implica_ renunciar a los derechos patrimoniales sobre el programa. Muy por
    el contrario, es una manera de _ejercerlos_. Es curiosa la preferencia de
    BSA por las licencias no-copyleft, ya que en ellas el autor sí renuncia casi
    completamente a ellos. Se trata de un caso de “yo quiero que los demás
    renuncien a sus derechos patrimoniales, así yo puedo imponer derechos
    patrimoniales míos sobre código de ellos”.
