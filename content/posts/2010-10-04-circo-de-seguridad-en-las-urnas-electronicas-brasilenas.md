---
title: "Circo de seguridad en las urnas electrónicas brasileñas"
date: 2010-10-04
categories: ["Codicia", "Era digital", "Ontodoncias", "Tecnocracia"]
---

Nos enteramos por La Voz del Interior de que [legisladores cordobeses
presenciaron el sorteo de urnas a
auditar](http://www.lavoz.com.ar/noticias/mundo/legisladores-cordobeses-en-el-sorteo-verificador-de-urnas-de-brasil)
en las elecciones del fin de semana pasado en Brasil, aparentemente
con vistas a la insólita idea de [hacer nuestras elecciones usando
urnas provistas y controladas por el gobierno de otro
país](http://www.lavoz.com.ar/noticias/mundo/brasil-esta-dispuesto-prestarle-las-urnas-electronicas-cordoba).

Dicho sorteo es un supuesto mecanismo de seguridad que parece diseñado
a propósito para ilustrar lo que en círculos especializados se conoce
como “circo de seguridad”: medidas que aparentan estar dirigidas a
mejorar la seguridad de un sistema, pero que en realidad no tienen
ningún efecto. 

En el caso que nos ocupa, la idea es la siguiente: cuando usamos urnas
electrónicas, es muy sencillo introducir en ellas un programa
malicioso que altere los resultados. Como no hay manera de contrastar
lo que la urna dice con lo que los votantes eligieron sin violar el
secreto del sufragio, esa alteración puede pasar completamente
desapercibida.

Es claro que el mismo Tribunal Electoral de Brasil reconoce que este
es un riesgo real, ya que hace una lotería de urnas a auditar, con el
fin de asegurarse de que funcionen como es debido: una vez
distribuidas las urnas a los lugares de votación, se sortea un
porcentaje de ellas al azar para que sean devueltas inmediatamente al
Tribunal. Esas urnas son sometidas a una auditoría que consiste en
operarlas en una elección simulada, en la que la máquina opera bajo
vigilancia y con una impresora. Se supone que si una muestra
representativa de las máquinas en uso demuestran funcionar de acuerdo
a lo esperado, las demás también lo harán.

Lamentablemente, esta suposición carece de sustento, ya que hay varios
mecanismos sencillos mediante los cuales un atacante puede pasar por
alto este control. Veamos algunas, en orden decreciente de
complejidad.

*   Introducir el programa malicioso luego del sorteo

	El sorteo se hace el día anterior a las elecciones, pero adulterar
	el software de una máquina toma muy poco tiempo, unos pocos
	minutos como máximo. Así, basta con esperar hasta luego del sorteo
	para adulterar las urnas que quedan.

	Este ataque es relativamente complejo, porque requiere tener un
	atacante que consiga unos minutos a solas con cada máquina en cada
	lugar de votación, pero no está fuera de escala de la complejidad
	de los esquemas de fraude con papel, con la ventaja de que es
	mucho más difícil de detectar.

*   Desactivar el ataque en las urnas sorteadas

	Una manera mucho más sencilla de pasar por alto el control es
	adulterar las urnas por adelantado, y desactivar el programa
	malicioso en las urnas que salen sorteadas. Esto hace posible que
	una persona que tenga acceso a las urnas previamente a las
	elecciones las modifique con tranquilidad, afectando muchos
	lugares de votación a la vez, instalándole software que puede ser
	desactivado en cuestión de segundos por otras personas que estén
	involucradas en el proceso de llevar las urnas sorteadas en el
	Tribunal Electoral.

*   Hacer que el programa se desactive solo

	El método anterior tiene el inconveniente de que es posible que
	urnas adulteradas lleguen al Tribunal Electoral con el programa
	malicioso activado, ya sea por error humano o por
	imprevistos. Pero en realidad, no es necesario que alguien
	desactive el programa: éste puede detectar si está siendo
	auditado, y alterar su comportamiento.

	Una manera fácil de detectar si la urna está siendo auditada, en
	este caso, es usando el hecho de que las urnas auditadas operan
	con impresora, mientras que las demás no. Basta entonces
	confeccionar el programa de tal modo que sólo altere los
	resultados si detecta que no hay una impresora conectada.

	Una manera más sofisticada consiste en analizar el volumen y ritmo
	de las emisiones de sufragio, así como la distribución de votos y
	la eficacia con la que se emiten. Es muy difícil replicar en una
	auditoría las mismas condiciones que en una mesa real: los
	auditores emiten los votos con un ritmo más regular, se equivocan
	menos al usarla, etc. El programa puede usar esta información para
	decidir si alterar los resultados o no.

*   Instalar el software de manera latente

	Otra alternativa es diseñar el software malicioso de modo que no
	altere el funcionamiento de la urna antes de ser activado mediante
	una combinación secreta de teclas. Las urnas sorteadas se
	comportarán sin inconvenientes, pero los atacantes (alguna de las
	personas que atienden las urnas, o cualquier votante) pueden
	alterar los resultados activando el programa mediante una
	contraseña especial. Como en las urnas auditadas nadie ingresa
	esta contraseña, las urnas auditadas funcionan correctamente,
	mientras que las otras no.

Estas técnicas muestran que el mecanismo implementado por el Tribunal
Electoral, caro y engorroso como es, no brinda ninguna seguridad
contra el riesgo del que supuestamente resguarda, porque los
resultados que obtiene no guardan necesariamente ninguna relación con
lo que efectivamente pasa en las mesas de votación.
