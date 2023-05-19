# Manager Mauro

Mauro tiene un espíritu deportivo tan grande, que paralelamente con sus estudios ha decidido también manejar el equipo de fútbol de su facultad MATCOM. Dedicar su tiempo a esto no es impedimento (cree él) para seguir obteniendo buenos resultados académicos. La verdad sea dicha, Mauro no tiene ni idea de fútbol. De hecho, varias veces se ha preguntado a sí mismo cómo llegó a esa importante posición. Lo bueno es que sí sabe de matemática y porgramación, así que decide formar un equipo (teóricamente) poderoso. Mejor aún, el equipo más (teóricamente) poderoso posible.

Se debe formar un equipo de $p$ jugadores en distintas posiciones y $k$ espectadores VIP (comisión de embullo). La facultad tiene $n$ personas. Para cada persona $i$ se conoce su valor $a_{i}$ como espectador VIP y su valor $p_{ij}$ como jugador en la posición $j$.

Ayude a Mauro haciendo un algoritmo que calcule el poder (valor) del mejor equipo posible. Un equipo es mejor que otro si tiene más valor.

> Se proveen 4 archivos de python y la documentación que explica los algoritmos utilizados. Para su uso:

- Abrir main.py
- Debe proveer una matriz de valores que representa el valor de los jugadores (filas) en las posiciones (columnas)
- Debe proveer además un array de tamaño n (cantidad de jugadores) con su valor como espectador VIP
- Llamar al método hungarian para obtener asignación y valor total.

     > hungarian(matrix)

- Se presenta un generador de casos de prueba y ambos métodos (combinatorio y húngaro) para comprobar sus resultados y tiempos.
