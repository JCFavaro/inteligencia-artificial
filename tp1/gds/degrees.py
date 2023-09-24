import csv
import heapq
import sys

from util import Node, PriorityQueueFrontier, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    function = input("Which algorithm do you want to use? 1.BFS 2.A* ")
    print("\n")

    source = person_id_for_name(input("Name: "))
    print("\n")
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    print("\n")
    if target is None:
        sys.exit("Person not found.")

    path = 0
    if function == "1":
        path = shortest_path_BFS(source, target)
    elif function == "2": 
        path = shortest_path_AStar(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")

# BFS
def shortest_path_BFS(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.

    Implementaremos el algoritmo busqueda en amplitud (BFS)
    
    La estructura de datos frontier es una cola FIFO, en cada iteracion
    sacamos un nodo (frontier.remove) y lo exloramos y luego agregamos sus vecinos
    a la frontera.

    La búsqueda en amplitud es una estrategia sistemática que examina todos los nodos 
    en el mismo nivel antes de pasar al siguiente nivel.

    Esto significa que estamos examinando todas las personas 
    que estan a una distancia de un grado de separacion antes de pasar a las personas que 
    estan a una distancia de dos grados de separacion, y asi sucesivamente.
    """

    # Inicializamos la frontera con el nodo fuente
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier()
    frontier.add(start)

    visitedNodes = set()


    while not frontier.empty():
        node = frontier.remove()

        if node.state == target:
            path = []
            while node.parent is not None:
                path.append((node.action, node.state))
                node = node.parent
            path.reverse()
            return path
    
        visitedNodes.add(node.state)

        neighbors = neighbors_for_person(node.state)

        for action,state in neighbors:
            if state not in visitedNodes:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)


    return None

#A*
def shortest_path_AStar(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target using A* algorithm.

    If no possible path, returns None.
    """

    start = Node(state=source, parent=None, action=None)
    frontier = PriorityQueueFrontier()  
    frontier.add(start, 0)  # 0 es la prioridad inicial

    visitedNodes = set()

    while not frontier.empty():
        node = frontier.remove()

        if node.state == target:
            path = []
            while node.parent is not None:
                path.append((node.action, node.state))
                node = node.parent
            path.reverse()
            return path

        visitedNodes.add(node.state)

        neighbors = neighbors_for_person(node.state)

        for action, state in neighbors:
            if state not in visitedNodes:
                child = Node(state=state, parent=node, action=action)
                priority = heuristic(state, target) 
                frontier.add(child, priority)

    return None

def heuristic(state, target):
    """
    Función de heurística que estima la distancia
    entre la persona actual (state) y la persona objetivo (target).
    """
    # Cuanto más películas en común, más cercanos están en la red de actores.
    return -len(people[state]["movies"].intersection(people[target]["movies"]))


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
