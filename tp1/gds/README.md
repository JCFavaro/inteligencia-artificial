# Resolución del Problema y Estrategias Aplicadas

## Descripción del Problema

- El problema consiste en encontrar el camino más corto de conexión entre dos actores en la industria cinematográfica utilizando el concepto de "Grados de separación de Kevin Bacon". En este contexto, se asume que cualquier persona en la industria cinematográfica de Hollywood puede conectarse con Kevin Bacon en seis pasos, donde cada paso consiste en encontrar una película protagonizada por dos actores.

## Estrategia de Resolución

- Para abordar este problema, se ha implementado una solución basada en el algoritmo de búsqueda en amplitud (BFS). La búsqueda en amplitud permite explorar el espacio de búsqueda de manera sistemática y encuentra la solución óptima en términos de la menor cantidad de pasos (o grados de separación) necesarios para conectar dos actores.

- La implementación del algoritmo se realiza en la función shortest_path del archivo degrees.py. Esta función utiliza una estructura de datos de frontera (ya sea una cola o una pila) para explorar los nodos de manera ordenada, manteniendo un registro de los nodos visitados y el camino actual.

## Aplicaciones Similares

### Redes Sociales y Teoría de Grafos

- La búsqueda de caminos más cortos entre nodos en un grafo es un problema fundamental en la teoría de grafos y tiene aplicaciones en redes sociales, sistemas de recomendación y análisis de redes. Por ejemplo, en redes sociales como Facebook o LinkedIn, se puede utilizar un algoritmo similar para encontrar la ruta de amistad más corta entre dos usuarios.

### Navegación y GPS

- En sistemas de navegación y GPS, la búsqueda de rutas óptimas entre ubicaciones es esencial. Al aplicar algoritmos de búsqueda de caminos más cortos, se pueden encontrar las rutas más eficientes para llegar de un punto A a un punto B, teniendo en cuenta factores como el tráfico y las restricciones de carreteras.

### Análisis de Trayectorias en Ciencias de Datos

- En el campo de la ciencia de datos, la búsqueda de caminos más cortos es utilizada para analizar trayectorias en diversos dominios. Por ejemplo, en biología, se puede utilizar para estudiar interacciones entre proteínas o rutas metabólicas.

## Posibles mejoras a este problema

### Algormito A* 

-En lugar de utilizar una búsqueda en amplitud (BFS), se podría considerar implementar el algoritmo A*. 
A* es una variante de la búsqueda en grafos que utiliza una heurística para priorizar los nodos que probablemente conduzcan más rápido a la solución.

### Caché de búsquedas anteriores

- Si es probable que se realicen búsquedas frecuentes entre ciertos pares de actores, se puede implementar una caché que almacene los resultados de búsquedas anteriores para evitar volver a calcularlos.

### Paralelización

- Si el conjunto de datos es lo suficientemente grande, podríamos explorar la posibilidad de paralelizar la búsqueda en múltiples procesos o hilos para acelerar el proceso.


