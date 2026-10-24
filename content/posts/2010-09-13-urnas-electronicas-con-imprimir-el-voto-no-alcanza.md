---
title: "Urnas electrónicas: con imprimir el voto no alcanza"
date: 2010-09-13
categories: ["Era digital", "Tecnocracia"]
---

En los diálogos que estoy teniendo en los últimos días con periodistas y
políticos sobre el uso de urnas electrónicas propuestas para las próximas
elecciones en la provincia de Córdoba, a menudo escucho el argumento de que son
auditables porque imprimen una boleta que cae en un receptáculo interno, de modo
que es posible hacer un recuento.

A primera vista, el argumento suena razonable y, por supuesto, una urna que
imprime boletas es preferible a una que sólo hace un registro electrónico. El
problema es que, como siempre, el problema se esconde en los detalles. En
particular, las urnas usadas en las elecciones de Marcos Juárez utilizan las
impresoras de tal modo que representan una seria vulnerabilidad a la confianza
en los resultados. Veamos los detalles, y cómo distintos tipos de actores
podrían explotar esta vulnerabilidad En esta nota, me limitaré a analizar esta
única vulnerabilidad, lo que no quiere decir que no haya otras muchas
vulnerabilidades posibles.. 

## El proceso

En un resumen simplificado, votar con las urnas usadas en Marcos Juárez funciona
de la siguiente manera:

1. el votante obtiene del presidente de mesa una “tarjeta chip” que lo habilita
   para emitir un único voto en la urna;
2. el votante se acerca a la urna e inserta la tarjeta chip, lo que habilita la
   pantalla táctil;
3. el votante usa la pantalla táctil para elegir una de las opciones por cada
   “tramo” de la elección;
4. luego de elegida la última opción, el sistema muestra una pantalla que resume
   todas las opciones elegidas, y pide al votante confirmación de que el resumen
   es correcto;
5. si el votante dice que no es correcto, el sistema permite repetir el proceso
   de selección, incluyendo la pantalla de resumen y consulta de confirmación;
6. cuando el votante confirma que el resumen es correcto, imprime una boleta
   similar a un ticket de supermercado con las opciones del votante, se la
   muestra al votante por algunos segundos detrás de una ventana transparente
   que le impide tocarla, y lo deja caer en la urna para un eventual recuento;
7. la urna queda lista para el próximo votante, la tarjeta chip ya no puede ser
   usada para emitir votos hasta que el presidente de mesa la re-habilite.

El procedimiento suena sólido, pero hay algo en el penúltimo paso que lo
invalida: la urna muestra la boleta al votante, e indefectiblemente la deja caer
en la urna. ¿Qué pasa si la boleta impresa por la urna no coincide con el
resumen aprobado por el votante?

## Explotando el problema

Una divergencia entre lo elegido por el votante y lo que se ve en la boleta es
perfectamente posible: la coincidencia o no entre lo que muestra la pantalla y
lo que muestra la boleta no es en virtud de ninguna ley de la naturaleza, sino
el fruto de la manera en la que la urna está programada: se la puede programar
para que coincidan, o para que no, o para que a veces coincidan y a veces no.
Esta posibilidad abre al menos dos avenidas de ataque a una elección realizada
con estas urnas.

### Robar votos

La primera avenida es explotable por quienes controlan las urnas, tanto la
empresa proveedora, como las personas que instalan, reparan o administran las
urnas y todas aquellas que tengan acceso a las urnas por los pocos segundos
necesarios para alterar su programación de tal modo que (durante la elección,
pero no durante las pruebas) ignoren la voluntad de cierto número de votantes, y
emitan votos distintos a los elegidos. La programación podría alterarse también
para que, cuando cambie el voto, deje caer la boleta directamente en la urna sin
darle tiempo al votante a leer con cuidado la boleta.

¿Qué recursos tiene el votante cuando esto sucede? Por supuesto, puede reclamar
al presidente de mesa, pero ¿qué puede hacer éste? ¿de qué pruebas cuenta el
votante de que el voto impreso no correspondía a su voluntad? El voto ya está en
la urna, mezclado con los demás. Es imposible saber si el votante dice la verdad
o no.

¿Qué hacemos ante una denuncia de este tipo? Esencialmente, tenemos dos
opciones:

1. Podemos desatenderlas, asumiendo que las urnas funcionan siempre
   correctamente. Si elegimos esta opción, la seguridad ofrecida por las boletas
   impresas desaparece, ya que la urna tiene licencia para imprimir el voto que
   se le dé la gana, y una operación de robo de votos como la descripta tendría
   éxito.
2. Podemos atenderlas. En ese caso, toda urna en la que uno o más votantes
   denuncien que la urna no respetó su voluntad debería ser sacada de
   circulación, y todos los votos emitidos hasta ese momento declarados
   inválidos, ya que no sabemos cuántos de los votos impresos allí efectivamente
   son correctos porque no podemos confiar en que todos los anteriores votantes
   efectivamente hayan controlado bien la impresión.

### Sabotear la elección

La segunda opción suena, por cierto, más segura. Lamentablemente, es
precisamente la que abre la segunda avenida de ataque, que puede ser usada para
crear una crisis de legitimidad. A diferencia del primer ataque, que es
atractivo para partidos que pueden asegurarse una victoria ganando pocos puntos
porcentuales, este ataque es interesante para grupos radicales minoritarios, sin
chances de ganar las elecciones y que, por lo tanto, prefieren sabotearlas.

Un grupo por el estilo, con un caudal de votos de unos pocos votos por mesa, no
necesita modificar nada en las urnas. Todo lo que debe hacer es instruir a sus
miembros para que elijan a los candidatos de algún partido mayoritario en la
urna, pero inmediatamente eleven una queja ante el presidente de mesa diciendo
que la boleta impresa no coincidía con su elección. Como estamos asumiendo que
tomamos la decisión de que ese tipo de denuncias invalida la urna, nos
encontramos con que la elección fracasa por el gran número de urnas objetadas.

## ¿Se puede arreglar?

Es difícil resistir a la tentación de imaginar pequeños cambios que podríamos
hacer a la urna y el procedimiento para resolver el problema. No voy a entrar
ahora en detalle de cuáles serían esas alternativas, y cómo cada una de ellas
falla de manera más o menos catastrófica: hay mucha literatura especializada que
muestra que no conocemos aún criterios objetivos, medibles, que puedan
demostrarnos que una urna electrónica es segura: el uso de computadoras en la
emisión del voto tiene el potencial de eliminar algunas posibilidades de fraude,
pero también el de introducir otras, más baratas y difíciles de detectar que las
del sistema de urnas de cartón y boletas de papel.

En todo caso, una manera eficaz de sacarnos de encima estas dudas y problemas es
reconocer la importancia de que el votante exprese su voluntad sin que ésta deba
ser interpretada y mediada por tecnología. La informática puede aportar mucho a
la rapidez y transparencia en los comicios si es aplicada en la instancia
adecuada: el escrutinio, ya sea el de cada mesa o el centralizado.
