---
title: "Software vs. Copyright (dejá, no me defiendas más)"
date: 2010-05-12
categories: ["Codicia", "Era digital", "Ontodoncias"]
---

## Un noviazgo auspicioso

Por muy razonable que a mucha gente le parezca el hecho de que el
software esté sometidoEs común leer que el software está “protegido”
por derecho de autor.  Lamentablemente, quienes usan esa imagen suelen
olvidar decir _de cuáles riesgos_ está siendo protegido, y por lo
tanto resulta difícil decidir si la protección contribuye a
contrarrestar esos riesgos o no. Decir que el software está sometido
al derecho de autor refleja más fielmente lo que está ocurriendo: todo
software está bajo derecho de autor, independientemente de los deseos
de sus autores y usuarios. al copyright,[^1] se trata en realidad de
una decisión arbitraria, adoptada como resultado de las negociaciones
que, en los '70, se realizaron para encontrar un marco regulatorio
apropiado para los programas de computadora.

En defensa de esta decisión, diré que subyace a ella una observación
correcta de la naturaleza de los programas como construcciones
culturales, no técnicas, como obras que se escriben y no productos que
se manufacturan. Esta observación es crucial, en cuanto reconoce la
capacidad expresiva de los programas de computadora, caracterizándolos
como el vehículo idóneo para comunicar algoritmos, de la misma manera
que las partituras permiten comunicar música o las ecuaciones permiten
comunicar ciertas verdades matemáticas.

Tratar al software como la obra expresiva que es tiene consecuencias
importantes y beneficiosas para la sociedad. Implica, por ejemplo, que
el derecho a la libertad de expresión se aplica tanto a quienes se
expresan en código como a quienes lo hacen en Castellano o en notación
musical.  Reconocer al software como parte de nuestra cultura, a la
que los Derechos Humanos nos garantizan acceso, plantea la necesidad
de que el régimen al que se lo someta tenga como objetivo primordial
fomentar su difusión para ponerlo al alcance del público.

Otra implicación importante es que el objeto de la regulación es la
obra (el programa) y no su función: si yo escribo un programa para que
la computadora realice determinada tarea, otras personas pueden
escribir otros, distintos, que resuelvan el mismo problema sin que
haya conflictos legales. La actual controversia en Estados Unidos
sobre las patentes de software, muestra las consecuencias que hubiera
tenido considerar al software, erróneamente, como producto y no como
obra: en ese país, es posible obtener una patente sobre “utilizar un
programa para resolver el problema _X_”, y a partir de ese momento el
titular de la patente es la única persona con derecho a escribir
programas que resuelvan _X_.Un detalle interesante es que tal patente
se puede obtener _incluso si quien la solicita no ha escrito aún el
programa, ni tiene intenciones de escribirlo_.

## Un matrimonio conflictivo

Si bien el reconocimiento de la naturaleza expresiva de la
programación hace evidente que las patentes no son el marco
regulatorio adecuado para el software, esto no quiere decir que el
copyright necesariamente lo sea o, al menos, que sea razonable aplicar
exactamente el mismo copyright, de exactamente la misma manera, a
programas que a libros o canciones.

El elemento que más fácilmente se identifica en el derecho de autor
como inadecuado para el software es el de la duración. El copyright es
un monopolio limitado en tiempo, con la idea de que una vez expirado,
la obra que entra al dominio público sigue siendo útil. En el caso de
la mayoría de las obras musicales y literarias, podemos asumir que
seguirán siendo útiles durante un tiempo muy largoLa exagerada
duración actual del copyright hace que esta suposición aparezca como
exageradamente optimista: es altamente probable que, setenta años
luego de la muerte del autor, ya no haya ejemplares viables de la
obra, ya sea por degradación del medio (papel, vinilo, celuloide) o
porque la obsolescencia del formato hace que no haya dispositivos que
permitan acceder a ellas. ¿Cómo escucharíamos hoy música grabada en un
magazine de ocho pistas?, pero los programas tienen una vida útil muy
limitada. La rápida evolución de los diseños de hardware y el
surgimiento constante de nuevos entornos de aplicación hacen que los
programas pierden su utilidad a escasos cinco años de ser publicado, a
menos que se los actualice. Un programa que entrara en el dominio
público apenas diez años luego de ser publicado sería inútil para
fines prácticos. Si un programa entra en el dominio público setenta
años luego de la muerte del autor, ¿de dónde vamos a sacar hardware
capaz de ejecutarlo?

Hay otro aspecto menos obvio en el cual la transacción social
implícita en el copyright no se cumple para el software. Cuando un
autor publica una obra bajo copyright, (un libro, una pintura, una
composición musical), ésta queda inmediatamente a la vista del
público, quien puede estudiarla, analizarla, desmenuzarla y apreciar
todos los aspectos que hacen a la construcción de la obra. Esto no
ocurre necesariamente cuando la obra es un programa: los programadores
tienen la posibilidad de ejercer el monopolio sobre la obra sin
necesidad de revelarla.

Esto es posible gracias al hecho de que hay varias representaciones de
un mismo programa, algunas de las cuales son prácticamente imposibles
de comprender por el ser humano porque están diseñadas para ser
interpretadas por una máquina. Por supuesto, las personas que
programan no usan esas representaciones directamente, sino que usan
lenguajes de programación, notaciones formales diseñadas para ser
fácilmente comprensibles para quienes las conocen, aunque al ojo no
entrenado aparezcan como una cruza entre Inglés y matemáticas. Un
programa para calcular la raíz cuadrada de un número, por ejemplo,
podría escribirse así en el lenguaje `C`:

```
/* Esta función imprime la raíz cuadrada de su argumento */
static void printsqrt(float x) {
if (x < 0) /* la raíz de un numero negativo es imaginaria */
    printf("El numero es menor que cero!\n);
else       /* el numero es positivo, todo bien */
    printf("%f\n", sqrt(x));
}
```

En este trozo de código puede apreciarse la intención comunicativa del
programa, expresado en una notación “humana” que incluye notas
aclaratorias de la intención del autor y las razones por las que toma
ciertas decisiones, de modo que pueda ser entendido por otra
persona. Esta representación del programa en forma comprensible a los
humanos es lo que suele llamarse “código fuente” del programa.[^2] Lo que la
computadora ejecuta, sin embargo, no es el código fuente, sino el
resultado de traducirlo, mediante un proceso automático, en _lenguaje
de máquina_. Un programa en lenguaje de máquina consiste en una larga
lista de instrucciones codificadas numéricamente, que listan en
detalle las operaciones elementales que el procesador debe
ejecutar. Cuando traducimos el programa de más arriba para que pueda
ser ejecutado en máquinas de tipo “PC,” todos los elementos
comunicativos desaparecen, y queda reducido a la siguiente lista de
números:

```
2212858197      1171855596      3673086216      2665537513
250282615       1680082119      3892839557      4294967036
1171856363      605871368       4294901736      610065919
604292868       134514050       4294893544      1438894591
```

El problema consiste en que el derecho de autor no sólo se aplica a
los programas en su forma legible sino también al software en lenguaje
de máquina, aún cuando sólo se distribuya el segundo y no el
primero. Pero la transacción del copyright se basa en la idea de que
el autor obtiene del público un monopolio sobre la obra, a cambio de
socializarla. Cuando un programa se distribuye sólo en lenguaje de
máquina, esa socialización no se produce, y el público es estafado.

## Los hijos reclaman el divorcio

Mucho ha escrito ya la [Free Software Foundation](http://fsf.org/)
acerca de los daños que los monopolios sobre la distribución de
software causan en la sociedad como un todo, criminalizando actitudes
valiosas como la solidaridad de compartir con nuestros
semejantes. Pero más allá de eso, la manera en que aplicamos el
copyright a los programas, sin prestar atención a aquellas
características que lo diferencian de otros medios de expresión
cultural, atenta contra su florecimiento como tal.

La práctica generalizada de la distribución de software sin código
fuente (más parecido, estrictamente, al ejercicio de un secreto
industrial que al de un derecho de autor) entorpece la capacidad de
quienes ejercen la disciplina de aprender unos de otros, como ocurre
en las demás artes. Dificulta, además, el ejercicio efectivo del
derecho de autor sobre aquellas obras que sí han sido publicadas como
código fuente: resulta muy difícil descubrir y demostrar que cierto
programa ejecutable contiene un plagio de otro cuando no contamos con
el código fuente del primero, sino sólo con una lista de números
dentro de la cual puede estar, o no, escondida una de muchas posibles
traducciones del código fuente a código de máquina.

El resultado de esta distorsión es fácil de reconocer la práctica: un
mercado de grandes corporaciones que privatizan para sí las obras de
sus empleados, manteniendo el monopolio sobre su distribución sin
enriquecer el acervo cultural común ni aportar obras útiles al dominio
público, al tiempo que corren muy poco riesgo de ser descubiertas
cuando incorporan en sus programas obras de terceros.

Queda por preguntarse cómo sería el paisaje de software actual si en
aquellas negociaciones de los '70 hubiera prevalecido la idea de que
el software requiere un régimen similar al copyright pero adaptado a
su naturaleza específica, con duraciones drásticamente menores y
exigiendo la publicación del código fuente.

En todo caso, la gran cantidad de desarrolladores de software libre,
quienes deliberadamente renuncian a imponer condiciones restrictivas a
la distribución, estudio y confección de obras derivadas de sus
programas, no sólo desmiente de plano que el copyright sea necesario
para el desarrollo de la disciplina, sino que demuestra, por
construcción, que un ambiente de cooperación y colaboración es mucho
más fértil para la disciplina que uno de aislamiento y restricción.

[^1]: En este texto hablaré de “copyright” como sinónimo de “derechos
      de autor.” Esto no es estrictamente correcto, pero la diferencia
      entre ambos conceptos no afecta a la argumentación específica de
      este artículo.
[^2]: Una exposición más a fondo de la diferencia entre lenguaje de
      programación y lenguaje de ejecución puede leerse en [¿Qué es el
      código fuente?]({{< ref "2006-05-21-codigofuente.md" >}})
