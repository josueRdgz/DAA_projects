# DAA_projects
El problema en cuestión es el siguiente: Se tienen n personas y k posiciones de un equipo con un costo de cada persona por cada posicion que puede jugar y una posicion extra que es observador (esta la tomaremos como una posición más). Debemos formar el mejor equipo.

Este es un problema de combinatoria, atacar este problema viendo todas las combinaciones tiene una complejidad N!, muy ineficiente. En la comunidad científica hay un algoritmo muy utilizado en orden polinomial para atacar este tipo de problemas de asignación: El algoritmo húngaro.

El algoritmo Húngaro es un algoritmo de optimización el cual resuelve problemas de asignación en tiempo O(n^{4}) con una mejora en O(n^{3})

El algoritmo modela un problema de asignación como una matriz de costes n×m, donde cada elemento representa el coste de asignar el enésimo trabajador al emésimo trabajo. Por defecto, el algoritmo realiza la minimización de los elementos de la matriz; de ahí que en caso de ser un problema de minimización de costes, es suficiente con comenzar la eliminación de Gauss-Jordan para hacer ceros (al menos un cero por línea y por columna). Sin embargo, en caso de un problema de maximización del beneficio, el coste de la matriz necesita ser modificado para que la minimización de sus elementos lleve a una maximización de los valores de coste originales. En un problema de costes infinito, el coste inicial de la matriz puede ser remodelado restando a cada elemento de cada línea el valor máximo del elemento de esa línea (o análogamente columna ). En un problema de coste infinito, todos los elementos son restados por el valor máximo de la matriz entera. En la matriz se tiene que realizar un conjunto de operaciones que nos permitirán conocer con mejor eficacia el resultado final de la problemática planteada.

a) Dada la matriz de costes C se construye C′ encontrando el valor mínimo de cada fila y restando ese valor a cada elemento de la fila. 

b) Se encuentra el valor mínimo de cada columna y se resta a cada elemento de la columna. 

c) Luego verificamos si para todas las filas existe una columna con costo 0 que no ha sido asignada a otra fila.

Determinar sobre G, un matching M de cardinalidad máxima.

si |M|=|N1|=|N2|⇒STOP

Si todas las filas tienen a lo menos una intersección con costo cero que no ha sido ocupada por otra fila, estamos en el óptimo. Termina el algoritmo.

1- Considero C′ y se etiquetan las filas que no han sido acopladas o asignadas por el algoritmo de matching máximo.

2- Se etiquetan en C′ las columnas que tienen los ceros en correspondencia o asignadas a las filas etiquetadas (con *).

3- Etiquetar las filas que no han sido ya etiquetadas y acopladas o asignadas por el algoritmo de matching máximo con las columnas ya etiquetadas (con *).

4- Repetir los pasos 2 y 3 hasta que no haya más filas o columnas que etiquetar.

5- Borrar las filas NO etiquetadas y las columnas etiquetadas. Para esto puede trazar una línea recta en las columnas y filas borradas.

6- Sea δ el elemento de C′ de valor mínimo entre aquellos costos no borrados (o tarjados) en el paso anterior.

7- Restar δ a cada elemento no borrado y sumarlo a los elementos doblemente borrados (o donde haya intersección o cruces entre las líneas marcadas en el paso 5

8-  Volver al paso c)


Uso: hungarian=Hungarian(profitMatrix,isProfitMatrix=True)
     hungarian.calculate
     hungarian.getResults()
     hungarian.getTotalPotential()
