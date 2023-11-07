import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

TEST_SIZE = 0.4


def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shopping.py data alghoritm")


    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    model = ""
    # Train model and make predictions
    if int(sys.argv[2]) == 1:
        model = train_model_KNN(X_train, y_train)
    else:
        model = train_model_Random_Forest(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


"""
    Esta función carga los datos de compras desde un archivo CSV y 
    los convierte en dos listas: una con la evidencia (características) 
    y otra con las etiquetas (si se realizó una compra o no).
"""


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # raise NotImplementedError
    evidence = []
    labels = []

    with open(filename, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Salta la primera fila que contiene los encabezados

        for row in reader:
            evidence_row = [
                int(row[0]),
                float(row[1]),
                int(row[2]),
                float(row[3]),
                int(row[4]),
                float(row[5]),
                float(row[6]),
                float(row[7]),
                float(row[8]),
                float(row[9]),
                [
                    "Jan",
                    "Feb",
                    "Mar",
                    "Apr",
                    "May",
                    "June",
                    "Jul",
                    "Aug",
                    "Sep",
                    "Oct",
                    "Nov",
                    "Dec",
                ].index(row[10]),
                int(row[11]),
                int(row[12]),
                int(row[13]),
                int(row[14]),
                1 if row[15] == "Returning_Visitor" else 0,
                1 if row[16] == "TRUE" else 0,
            ]

            label = 1 if row[17] == "TRUE" else 0  # Convertir a entero (Revenue)

            # caracteristicas
            evidence.append(evidence_row)
            # revenues
            labels.append(label)

    return evidence, labels


"""
    Entrena un modelo de clasificación basado en el algoritmo de vecinos más cercanos. 
    En este caso, se usa k=1, lo que significa que el modelo considerará el vecino más cercano al realizar predicciones.
"""


def train_model_KNN(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    # raise NotImplementedError
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(evidence, labels)
    return knn


"""
    Dado una lista de listas de evidencia y una lista de etiquetas,
    devuelve un modelo de Bosques Aleatorios entrenado en los datos.
"""


def train_model_Random_Forest(evidence, labels):

    #n_estimators (Numero de estimadores) 
    # Este parámetro determina cuántos árboles se construirán en el bosque. 
    # Más árboles generalmente conducen a un mejor rendimiento, pero también 
    # aumentan el costo computacional. Sin embargo, después de un cierto punto, 
    # el beneficio en términos de precisión comienza a disminuir y puede haber un 
    # punto óptimo para el número de estimadores. Elegir un valor alto como 100 suele ser una 
    # buena elección para obtener una precisión razonable sin incurrir en un exceso de costo computacional.

    #random_state (Semilla Aleatoria):
    #La construcción de árboles de decisión implica un componente aleatorio, 
    # como la selección de características en cada división. La semilla aleatoria 
    # controla este comportamiento aleatorio. Si fijas la semilla aleatoria (random_state) 
    # a un valor específico, obtendrás los mismos resultados cada vez que ejecutes el modelo. 
    # Esto es crucial para la reproducibilidad y la comparación de resultados entre diferentes ejecuciones del modelo.

    forest = RandomForestClassifier(n_estimators=100, random_state=0)
    forest.fit(evidence, labels)
    return forest


"""
    Evalúa el rendimiento del modelo. 
    Calcula la sensibilidad (tasa positiva real) y la especificidad (tasa de negativa real) del modelo.
"""


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    # raise NotImplementedError
    true_positive = sum(
        1
        for true, predicted in zip(labels, predictions)
        if true == 1 and predicted == 1
    )
    true_negative = sum(
        1
        for true, predicted in zip(labels, predictions)
        if true == 0 and predicted == 0
    )

    sensitivity = true_positive / labels.count(1)
    specificity = true_negative / labels.count(0)

    return sensitivity, specificity


if __name__ == "__main__":
    main()
