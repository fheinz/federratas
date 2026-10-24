---
title: "Banca Electrónica: ¿quién nos defiende de nuestros guardianes?"
date: 2006-05-27
categories: ["Era digital", "Tecnocracia"]
---

Los bancos promocionan sus servicios de banca electrónica como seguros en virtud
de las medidas tecnológicas que adoptan. El público, sin embargo, está en pobres
condiciones de evaluar dicha seguridad, y sobre todo queda sin herramientas para
controlar que lo que el mismo banco hace con su cuenta. 

## Me dijo un muchacho que sabe

En la era de Internet, la mayoría de los bancos ofrecen servicios de banca
electrónica. Esencialmente, se trata de programas accesibles desde la red, que
pueden ser usados por los clientes del banco para consultar información y para
realizar transacciones. Por cierto, luego de ver tanta película en la que
delincuentes tecnificados realizan estafas millonarias a través de la red, los
bancos invierten mucho esfuerzo de comunicación en asegurar a sus clientes que
el sistema de banca electrónica es completamente seguro. Sería interesante saber
si invierten el mismo esfuerzo en hacer sistemas que en efecto sean tan seguros
como quieren pintarlos.

Lamentablemente, la seguridad informática es una disciplina tan compleja y
especializada, que la mayoría de los clientes de los bancos no están en
condiciones de evaluar si lo que les dicen tiene sentido o no. Los mismos
empleados de los bancos suelen destacar, por ejemplo, que el sistema es
absolutamente seguro porque utiliza \`\`cifrado SSL de 128 bits''. La industria
de las computadoras ya ha instalado en los usuarios el concepto de que
\`\`mientras más bits, mejor'', de modo que algo con tantos bits debe ser
extremadamente seguro. De hecho el protocolo es muy seguro: si algún malhechor
lograra interceptar una comunicación no cifrada entre el cliente y el banco,
podría obtener información confidencial como saldos de cuenta y sobre todo
palabras claves, que luego le permitirían hacer movimientos de dinero. Si la
comunicación está cifrada con SSL de 128 bits, sin embargo, todo lo que puede
ver es números sin sentido, cuyo significado sólo podría ser desentrañado,
quizás, por alguna de las agencias de espionaje de las grandes potencias, a un
costo que probablemente exceda por varios órdenes de magnitud el saldo de la
cuenta del cliente promedio.

## Vulnerabilidades múltiples

El problema es que SSL sólo protege contra esa avenida de ataque, y no es la
única. Ni siquiera es la más fácil. Como suele ironizar el especialista en
seguridad Enrique Chaparro, asegurar que un sistema es seguro porque usa SSL es
comparable a decir que una casa es segura en virtud de que, en el patio, tiene
una pared de cemento armado de 35 cm de espesor por tres metros de alto por un
metro y medio de ancho. Es cierto: cualquier intruso que pretenda entrar justo
por ahí seguramente no podrá hacerlo, pero basta con que camine un metro hacia
el costado para que el obstáculo insalvable deje de ser tal.

Un delincuente que desea acceder a los datos confidenciales del cliente tiene
muchas alternativas disponibles. Un mecanismo técnico altamente eficaz es la
difusión de gusanos, virus y troyanos por la red. El hecho de que la inmensa
mayoría de las computadoras del planeta estén muy pobremente protegidas contra
estas amenazas hace que a los malhechores les resulte muy fácil instalar
programas que espíen los datos y las actividades de los usuarios a fin de
informar a sus amos. Hay incluso alternativas que nada tienen que ver con la
informática en sí, sino con la llamada \`\`ingeniería social'': casi todos los
usuarios de correo electrónico habrán recibido recientemente mensajes de
entidades crediticias, o de empresas on-line, instándolos a \`\`confirmar sus
datos personales y clave secreta'' en un sitio web falsificado, cuyo único
objetivo es capturar los datos de incautos. Kevin Mitnick, el primer estafador
informático en recibir una condena penal en EEUU, rara vez utilizaba medios
técnicos para obtener claves de acceso. Su herramienta favorita era el teléfono:
llamaba a sus víctimas diciendo, por ejemplo, que estaba realizando \`\`tareas
de mantenimiento de la cuenta'', para lo que necesitaba la clave secreta del
cliente. No es sorprendente que tuviera éxito: un estudio reciente demostró que
un alto porcentaje de los usuarios de computadora están dispuestos a revelar su
clave de acceso a cambio de una barrita de chocolate.

## ¿Cuál es el modelo de amenaza más probable?

Todo esto no quiere decir, por cierto, que no haya que usar SSL: un esquema de
seguridad que no use cifrado de sus comunicaciones por Internet sería muy
vulnerable. Pero todo esquema de seguridad está diseñado alrededor de un modelo
de ataque. En otras palabras, las medidas de seguridad aplicadas tienen por
objetivo obstaculizar ciertas amenazas concretas. El cifrado de las
comunicaciones nos protege de que un tercero espíe los datos que enviamos, pero
¿es esa la amenaza que más debe preocupar al cliente? Al fin y al cabo, la
experiencia nos enseña que la inmensa mayoría de las violaciones de seguridad
informática no proviene de fuente externas, sino internas. ¿Qué medidas toma el
banco para proteger al cliente de maniobras fraudulentas de sus propios
empleados? Teniendo en cuenta que todos los contratos de banca electrónica que
he visto incluyen una cláusula por la que el cliente reconoce como adecuadas las
medidas de seguridad tomadas por el banco y renuncia al derecho de cuestionarlas
en el futuro, hay otro adversario más del que cabe proteger al cliente: el mismo
banco.

Podrá parecer paranoico pensar en que el banco vaya a estafar a sus propios
clientes. Quizás en Argentina lo sea menos, y no faltarán los cínicos que
acotarán que si no lo han hecho hasta ahora es solamente porque el monto de la
estafa potencial no se justifica aún. Pero aún si asumimos que los bancos son
completamente honestos, ¿por qué habrían de resistirse a que su interacción con
las cuentas también estén previstas en las salvaguardas de seguridad? Hoy, si
realizan un pago sin autorización firmada del titular de la cuenta, deben
hacerse responsables por ello. Si la banca electrónica no incluye los mecanismos
adecuados, el banco estaría en condiciones de fraguar una autorización que nunca
existió.

Si el banco le pide al cliente que confíe totalmente en él, esta relación de
confianza debería ser mutua. Mientras el banco tome los debidos resguardos en
contra de posibles abusos por parte del cliente, lo justo es que ofrezca al
cliente la posibilidad de ejercer un control similar sobre el banco. Los
mecanismos para hacerlo, basados esencialmente en sistemas de firma electrónica,
existen y están en uso en varios países, por ejemplo Alemania.

La seguridad no se resuelve con un protocolo de comunicaciones, ni con un
producto informático, sino que debe construirse como un sistema completo,
incluyendo no sólo los elementos técnicos, sino también los humanos. Si
realmente quieren demostrar que son seguros, los sistemas de banca electrónica
deberían ofrecer control a ambos extremos de la transacción, e informar a sus
clientes con seriedad acerca de los mecanismos usados, de la interacción entre
ellos y de los riesgos que apuntan a disminuir.
