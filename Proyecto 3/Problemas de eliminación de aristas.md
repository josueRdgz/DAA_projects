Existen, en teoría de grafos, muchos problemas de eliminación de aristas, los cuales pueden ser difíciles de resolver de manera eficiente, o incluso, imposibles de hacerlo de manera de correcta para un número considerable de nodos y aristas.

El problema que se presenta es uno de estos:

# Problema

Luego de leer el problema en [Readme](obsidian://open?vault=Proyecto%203&file=Readme) podemos reducirlo a:

 > Decir si es posible obtener un grafo bipartito a partir de la eliminación de hasta k aristas de un grafo G
 
Debemos tener en cuenta que si un planeta apunta a otro entonces existe una arista entre ellos. En caso de apuntarse mutuamente, entonces tenemos que modificar el grafo inicial tomando uno de esos nodos y duplicándolo, de tal manera que uno de ellos tenga la arista que representa el ataque de salida y el otro nodo tenga la arista del ataque de entrada. En la figura siguiente se muestra la transformación:

![[transformacion.png]]

Si nos damos cuenta, el resultado será el mismo, ya que el objetivo es demostrar que existe o no un grafo bipartito. Como un planeta no se ataca a sí mismo, al duplicar un nodo, estos estarán en la misma parte de la bipartición y la eliminación de aristas sigue siendo inalterable.

Por lo tanto, tenemos, en general, el siguiente problema:

> Entrada: 
> Un grafo $G(N,E)$ y un entero $k$ que será el número máximo de aristas a eliminar.
> 
> Salida: 
> - $True$ si  $\exists$  $p\leq k$  $|$  $G(N,E-p)$ es bipartito. 
> - $False$ en caso contrario   

# Demostrando NP-completitud

Este problema (llamémosle A) es  *NP-completo*, es decir, es un problema de decisión sobre el que podemos probar que existe otro problema *NP-completo* (llamémosle B)  tal que: B $≤p$ A y A $\in$ NP.

Primero demostremos que el problema se encuentra en la clase de problemas NP:

1. Tomemos una instancia de la solución, es decir, una lista de hasta k aristas que se eliminan del grafo G para obtener un grafo bipartito.

2. Comprobemos que la instancia es verdadera. Se debe eliminar las aristas de la lista del grafo G y comprobar si el grafo resultante es bipartito. Esto se puede hacer en tiempo polinómico, ya que la verificación de si un grafo es bipartito se puede hacer en tiempo O(V+E) utilizando el algoritmo BFS.

3. Como se puede verificar en tiempo polinómico si esta instancia es verdadera, el problema se encuentra en la clase de problemas NP.

Ahora, demostremos que es NP- completo aplicando la reducción de uno de los 21 problemas de Karp a este problema.

## Problema de corte máximo

Dado un grafo _G_ y un entero $k$ _,_ determinar si hay un corte de tamaño al menos $k$ en _G._

Se sabe que este problema es NP-completo . Es fácil ver que el problema está en NP: una respuesta _afirmativa_ es fácil de probar presentando un corte lo suficientemente grande. La NP-completitud del problema se puede mostrar, por ejemplo, mediante una reducción de la máxima 2-satisfacibilidad (una restricción del problema de máxima satisfacibilidad. La versión ponderada del problema de decisión fue uno de los [21 problemas NP-completos de Karp](https://en.wikipedia.org/wiki/Karp%27s_21_NP-complete_problems "Los 21 problemas NP-completos de Karp") Él mostró que era NP-completo por una reducción del problema de partición.

## Reducción

(=>) Sea $G=(N,E)$ un grafo de tal manera que al eliminar al menos $k$ aristas este es bipartito.

- Creamos un nuevo grafo G´ que es copia de G y obtengamos el entero $p$ para usarlo en el problema de corte máximo.
- Al eliminar k aristas de G y obtener un grafo bipartito nos quedamos con aristas que van de una bipartición a otra, por lo tanto, si nos quedamos con esas aristas podemos separar con un corte ambas biparticiones. Así que $p =|E|-k$.
- Esto nos permite decir que si existe el grafo bipartito al eliminar al menos $k$ aristas, entonces para G´ y un entero $p$ existe un corte de tamaño al menos $p$. Ahora, ¿cómo sabemos que el tamaño del corte es al menos $p$?
- Como la cantidad de aristas que se eliminan de G, es menor o igual que $k$ entonces el número de aristas que quedan cruzando las biparticiones es mayor o igual que $p$, por lo tanto, el tamaño del corte es mayor o igual que $p$.

(<=) Sea $G´=(N´,E´)$ un grafo  que presenta un corte de tamaño al menos $p$.

Seguimos de la misma manera que la demostración anterior:

- Tomamos un grafo G =G´
- Como $p$ es el tamaño del corte que divide en dos particiones al grafo, tomamos el número de todas las aristas que no cruzan ese corte, es decir, $k=|E´|-p$. Estas aristas son las que se encuentran dentro de las particiones (que necesitamos eliminar para obtener el grafo bipartito).
- Así obtenemos que dado G y $k$ determinamos que eliminando a lo sumo k aristas, G es bipartito.

 >[!Note] Conclusión
 >Como puede reducirse el problema de corte máximo al problema presentado y teniendo en cuenta que es NP-completo, podemos concluir que nuestro problema es NP-completo.
 
# Archivos

### Solución con backtrack

Se presenta una solución ineficiente pero exacta de nuestro problema, eliminando aristas y comprobando si el grafo resultante es bipartito.

# K-aproximación

Un algoritmo de aproximación común para los problemas de eliminación de aristas es el algoritmo de eliminación de aristas aleatorias. Este algoritmo funciona de la siguiente manera:

1. Seleccionamos aleatoriamente k aristas del grafo original y las eliminamos.

2. Verificamos si el grafo resultante es bipartito. Si es así se devuelva el subgrafo bipartito resultante. Si no, volvemos a elegir aleatoriamente k aristas

Este algoritmo es $\frac{k}{2}$ - aproximación del problema, lo que significa que la solución que devuelve siempre tendrá al menos la mitad del tamaño del subgrafo bipartito óptimo. Además, el algoritmo se ejecuta en tiempo polinómico en el tamaño del grafo.

>[!Note] Vamos a demostrar este algoritmo aleatorio de  $\frac{k}{2}$ - aproximación.
>
>Podemos garantizar esta aproximación ya que, en promedio, la mitad de las aristas eliminadas serán necesarias para obtener un subgrafo bipartito. Veamos cómo probamos esto:
>
>Sabemos que la probabilidad de que una arista sea necesaria para obtener un subgrafo bipartito es de 1/2 (es o no necesaria). Por lo que la esperanza del conjunto $K$ de aristas aleatorias tomadas es:
>
>$E[K] = \frac{1}{2} + \frac{1}{2} * (E[K-1] + 1)$
>
>Donde $\frac{1}{2}$ representa la probabilidad de que la primera arista eliminada sea necesaria para obtener un subgrafo bipartito y $\frac{1}{2} * (E[K-1] + 1)$ representa la probabilidad de que la primera arista eliminada no sea necesaria y se tenga que eliminar una arista adicional.
>
>La ecuación anterior es una ecuación de recurrente fácil de resolver:
>$E[K] = \frac{1}{2} + \frac{1}{2} * E[K-1] + \frac{1}{2}$
>$E[K] = 1 + \frac{1}{2} * E[K-1]$
> Vemos que $E[K-1] = 1 + \frac{1}{2} * E[K-2]$
> Al sustituir en la ecuación original:
> $E[K] = 1 + \frac{1}{2} * (1 + \frac{1}{2} * E[X-2]$
> $E[K] = 1+ \frac{1}{2} + \frac{1}{4} * E[K-2]$
> $E[K] = \frac{3}{2} + \frac{1}{4} * E[K-2]$
> Esto se realiza $k$ veces hasta llegar a $E[0]=0$ y como se puede notar obtenemos $E[K] =\frac{k}{2}$. Esto significa que, en promedio, el algortimo se aproxima en $\frac{k}{2}$ aristas a la solución correcta.
> 
> La complejidad temporal en el peor de los casos es $O(E)$ ya que se puede probar eliminar todas las aristas del grafo en el conjunto $K$.


### Solución con metaheurísitca

Además de la solución aleatoria demostrada anteriormente desarrollamos una metaheurística basada en colonia de hormigas.

# Bibliografía