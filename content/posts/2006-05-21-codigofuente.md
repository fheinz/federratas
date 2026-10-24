---
title: "¿Qué es el “código fuente”?"
date: 2006-05-21
categories: ["Era digital", "Ontodoncias"]
---

Cuando hablamos de software, y en particular de Software Libre, a menudo nos
encontramos con la frase “código fuente”. Para las personas que no practican el
arte de construir programas, este concepto suele ser un tanto confuso. En este
artículo intentaré explicar qué es el “código fuente” en términos que puedan ser
comprendidos por cualquier persona interesada en la materia, aunque carezca de
conocimientos técnicos. A partir de allí, será muy sencillo comprender la
importancia de la disponibilidad del código fuente de un programa para que éste
pueda ser considerado “libre”. 

## Lenguajes de máquina

A diferencia de los objetos materiales, que se fabrican, los programas se
_escriben_. Quizás parte de la fascinación que la programación ejerce sobre
quienes la practican se deba a la magia aparente de lograr que una máquina
cumpla las órdenes que le impartimos. Para que pueda entender lo que le
ordenamos, sin embargo, debemos comunicarnos con ella de una manera especial: el
procesador dentro de cada computadora sólo comprende instrucciones escritas en
su propio _lenguaje de máquina_. Existen muchos tipos distintos de procesador, y
cada uno de ellos tiene un lenguaje de máquina distinto, diseñado por su
fabricante. Esa es la razón por la que no es posible ejecutar cualquier programa
en cualquier computadora.

Los programas escritos en lenguajes de máquina son, básicamente, larguísimas
listas de números. Cada uno de estos números representa una operación elemental
(por ejemplo, 1: sumar, 2: restar, 3: almacenar en memoria, etc), o un operando,
o una combinación de ambas cosas. Para que el lector pueda darse una idea
concreta de cómo es un programa codificado en lenguaje de máquina, lo ilustraré
con un ejemplo: lo que sigue es una pequeña porción de un programa, escrito en
el lenguaje de máquina de los procesadores de la familia Intel y funcionando
bajo el sistema operativo GNU/Linux. Este programa imprime la raíz cuadrada de
un número cualquiera. Si el número resulta ser negativo, el programa imprime un
mensaje de error (recordemos que no es posible sacar la raíz cuadrada de un
número negativo):

```
2212858197      1171855596      3673086216      2665537513
250282615       1680082119      3892839557      4294967036
1171856363      605871368       4294901736      610065919
604292868       134514050       4294893544      1438894591
```

Una computadora moderna está en condiciones de ejecutar millones de
instrucciones de máquina como estas por segundo. Construir un programa complejo
a partir de instrucciones tan elementales y codificadas en un formato tan poco
amigable es, sin embargo, una tarea muy complicada para un ser humano. También
es extremadamente difícil entender cómo funciona un programa si sólo disponemos
de él en lenguaje de máquina. Para comprender cómo funciona el programa citado
más arriba no sólo es necesario recordar qué número corresponde a cual
operación, también debemos identificar cuáles partes de los números representan
operaciones, cuáles representan operandos, cuáles datos, y muchas otras cosas
más. Debido a detalles técnicos, modificarlo es mucho más difícil aún, ya que
para eliminar o agregar instrucciones no basta con insertarlas o borrarlas en la
lista: también hay que modificar los valores de muchas de las demás
instrucciones. Por ello, modificar un programa del que sólo tenemos una copia en
lenguaje de máquina, o traducirlo para que funcione en una máquina con un
lenguaje de máquina distinto, es una tarea virtualmente impracticable.

## Lenguajes de programación

Dado que las personas tienen serias dificultades para leer, escribir y modificar
programas en lenguaje de máquina, pero son esas mismas personas las que deben
escribir y mantener los programas, se inventaron los _lenguajes de
programación_. A diferencia de los lenguajes de máquina, que están diseñados con
el único objetivo de facilitar al procesador la ejecución de las instrucciones a
gran velocidad (podríamos llamarlo también _lenguaje de ejecución_), la
finalidad de los lenguajes de programación es facilitar a los seres humanos la
comprensión, la escritura y la modificación de los programas. El objetivo
primordial de un programa expresado en un lenguaje de computación no es ser
ejecutado directamente por una computadora (lo que es imposible), sino
comunicar, de manera comprensible para un ser humano, lo que una computadora
debe hacer para resolver un determinado problema.

Dado que la naturaleza de la computación está íntimamente ligada a las
matemáticas, los lenguajes de programación generalmente son una mezcla un tanto
idiosincrática de notación matemática entrelazada con una gramática
rudimentaria, por lo general basada (remotamente) en el inglés. A modo de
ejemplo, veamos cómo se expresa el mismo programa citado más arriba en un
lenguaje de programación muy difundido, llamado `C`:

```
/* Esta función imprime la raíz cuadrada de su argumento */
static void printsqrt(float x) {
    if (x < 0) /* la raíz de un numero negativo es imaginaria */
        printf("El numero es menor que cero!\n);
    else       /* el numero es positivo, todo bien */
        printf("%f\n", sqrt(x));
}
```

Aún para personas que no conocen el lenguaje `C`, este texto es más comprensible
que el programa en lenguaje de máquina de más arriba, ya que hay algunos
elementos claramente distinguibles.

Quizás lo más notable para el lego sean las notas aclaratorias en castellano,
entre los símbolos `/\*` y `\*/`. Estos textos (llamados _comentarios_) no
afectan la función del programa, pero sí son importantes para dejar plasmada la
intención del programador. En otras palabras, cumplen el rol de “notas
adhesivas”, en las que el programador aclara el objetivo de cada parte del
programa. Esto es muy útil cuando otro programador intenta comprender cómo
funciona el programa, o incluso cuando el mismo programador debe revisar ese
mismo programa un tiempo después de haberlo escrito.

Más allá de los comentarios, es relativamente sencillo advertir que la sentencia
`if (x < 0)` determina si el valor de la variable `x` es menor que cero.
Dependiendo del resultado, el procesador ejecutará la sentencia que está entre
el `if` y el `else`, de lo contrario la que que sigue al `else`. También es
fácil identificar los mensajes que serán mostrados al usuario, aunque el segundo
de ellos `("%f\\n)` contenga en realidad una codificación propia e idiosincrática
del lenguaje `C`: son los que están entre comillas. También es verosímil, para
quienes hablan inglés, que el nombre de la función `sqrt()` es una abreviatura de
_square root_, o “raíz cuadrada”.

El mismo programa puede escribirse en distintos lenguajes de programación. Por
ejemplo, en el lenguaje Python:

```
def printsqrt(x=0):
    """Esta función imprime la raíz cuadrada de su argumento"""
    if (x < 0): # la raíz de un numero negativo es imaginaria
        print "El numero es menor que cero!"
    else:       # el numero es positivo, todo bien
        print math.sqrt(x)
```

O en el lenguaje Smalltalk:

```
"Esta función imprime la raíz cuadrada de su argumento"
printsqrt: x
    (x < 0)
        ifTrue:  "la raíz de un numero negativo es imaginaria"
            [Transcript show:'El numero es menor que cero!']
        ifFalse: "el numero es positivo, todo bien"
            [Transcript show: x sqrt]
```

De un lenguaje de programación a otro, las convenciones cambian, y también
algunos aspectos técnicos, pero en todos ellos reconocemos elementos comunes, y
sobre todo vemos que su objetivo es facilitar la confección, comprensión y
modificación del programa, al permitir que el programador trabaje en un nivel de
abstracción que es confortable a una mente humana.

## Compilación

Los programas escritos en un lenguaje de programación no son comprensibles
directamente por una computadora. Recordemos que éstas sólo saben obedecer
instrucciones codificadas en su lenguaje de máquina. Antes de poder ejecutar un
programa escrito en un lenguaje de programación, debemos traducirlo al lenguaje
de la máquina sobre la que queremos que corra. Para cada combinación de
procesador, lenguaje y sistema operativo existen traductores automáticos,
llamados _compiladores_. Se trata de programas que leen un programa escrito en
un lenguaje de programación y, a partir de él, generan uno escrito en el
lenguaje de ejecución adecuado para una determinada combinación de procesador y
sistema operativo. El programa en lenguaje de máquina que vimos más arriba, de
hecho, es el resultado de pasar el texto del programa C que vimos a continuación
por un compilador llamado “gcc”.

Aquí se vuelve evidente otra gran ventaja de los lenguajes de programación sobre
el lenguaje de máquina: si mi programa está expresado en un lenguaje de máquina,
sólo podré ejecutarlo en máquinas equipadas con un determinado tipo de
procesador. Por el contrario, si lo escribí en un lenguaje de programación, en
principio basta con hacerlo traducir por el compilador adecuado para que el
programa pueda correr sobre el procesador que yo quiera.

## ”Código fuente”

En inglés, se conoce al programa escrito en lenguaje de programación como
“_source code_”, y al programa expresado en lenguaje de máquina como “_object
code_” (código objeto) o “_executable code_” (código ejecutable). En castellano,
a menudo se traduce “_source code_” con la frase “código fuente”, que no es
completamente fiel a la intención de la expresión inglesa. Tendría más precisión
técnica traducirlo como “texto original” del programa, ya que se trata del texto
tal como lo escribió el programador, mientras que el código ejecutable es el
fruto de una traducción automática realizada por un compilador.

Si bien es posible ejecutar un programa en la computadora adecuada contando sólo
con el código ejecutable, cuando se trata de comprender el funcionamiento de un
programa, de modificarlo, o de hacerlo funcionar en una máquina diferente, es
imprescindible disponer de su texto original, es decir de su “código fuente”.

## Código fuente y Software Libre

Para ser considerado libre, un programa debe ser distribuido de tal modo que el
usuario pueda, entre otras cosas, estudiar el modo de funcionamiento del
programa, adaptarlo a sus necesidades y distribuir, bajo las mismas condiciones,
programas derivados. Para que estas libertades sean practicables, no basta con
que la licencia del programa las permita. Además, es necesario que el código
fuente del programa esté a disposición del usuario, ya que de lo contrario las
tareas de comprender, adaptar y mejorar el programa se vuelven tan complicadas
que es casi lo mismo que si estuvieran prohibidas. Por eso la definición de
Software Libre elaborada por la Free Software Foundation aclara que un programa
no puede ser considerado libre si su código fuente, su texto original, no está
disponible.
