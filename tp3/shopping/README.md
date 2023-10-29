# Informe sobre el Trabajo de Inteligencia Artificial en Predicción de Compras en Línea

## Objetivo

El objetivo de este trabajo es desarrollar un sistema de Inteligencia Artificial (IA) capaz de predecir si los clientes completarán una compra durante una sesión de compra en línea.
Descripción del Problema

El conjunto de datos proporcionado contiene alrededor de 12,000 sesiones de usuario representadas como filas en una hoja de cálculo. Cada fila contiene información sobre el comportamiento del usuario durante su sesión, como el tipo de páginas visitadas, la duración de la visita, métricas de Google Analytics y más. La columna Revenue indica si el usuario finalmente realizó una compra (TRUE) o no (FALSE). Esta será nuestra variable objetivo.

## Algoritmos Utilizados

* 1. K-Nearest Neighbors (KNN)

El algoritmo K-Nearest Neighbors (Vecinos más Cercanos) se utiliza para clasificación y regresión. En este trabajo, se emplea como un clasificador para predecir si un cliente completará una compra.

* 2. Preprocesamiento de Datos

Antes de aplicar el algoritmo KNN, se realiza un preprocesamiento de los datos. Esto incluye la transformación de ciertos tipos de datos y normalización de valores para asegurar que todos los datos sean numéricos y estén en el rango adecuado.

## Funciones Implementadas

* 1. load_data(filename)

Esta función carga los datos desde un archivo CSV y los convierte en dos listas: evidence y labels. Evidence contiene información sobre el comportamiento del usuario, mientras que labels indica si el usuario completó una compra o no.

* 2. train_model(evidence, labels)

Entrena un clasificador K-Nearest Neighbors con k=1 utilizando el conjunto de datos de entrenamiento. Este modelo será utilizado para hacer predicciones.

* 3. evaluate(labels, predictions)

Evalúa el rendimiento del modelo mediante la comparación de las etiquetas reales (labels) y las etiquetas predichas (predictions). Calcula la sensibilidad (tasa positiva real) y especificidad (tasa negativa real) del modelo.

## Ejecución del Programa

El programa comienza verificando los argumentos de línea de comandos y luego carga los datos del archivo CSV. Los datos se dividen en conjuntos de entrenamiento y prueba para evaluar el modelo.

A continuación, se entrena un modelo KNN y se realizan predicciones en el conjunto de prueba. Finalmente, se evalúa el rendimiento del modelo y se imprimen los resultados.

## Estrategias Aplicadas

Se implementaron las siguientes estrategias para mejorar el rendimiento del modelo:

    * Transformación de Datos: Se aseguró de que los datos estén en el formato correcto y se realizaron conversiones necesarias para asegurar que todos los datos fueran numéricos.

    * Normalización de Valores: Se normalizaron ciertos valores para asegurarse de que estén en el rango adecuado y no dominen sobre otras características.

## Aplicaciones Similares de este Algoritmo

El algoritmo K-Nearest Neighbors (KNN) tiene una amplia gama de aplicaciones en diversos campos:

    * Sistemas de Recomendación: KNN se utiliza en sistemas de recomendación para encontrar productos o contenido similares a los gustos de un usuario.

    * Diagnóstico Médico: Se aplica en medicina para clasificar pacientes en grupos con base en características similares.

    * Procesamiento de Lenguaje Natural: En tareas como la clasificación de texto o la traducción automática, KNN puede ser utilizado para encontrar similitudes entre textos.

    * Análisis de Imágenes: Se utiliza para clasificar imágenes basado en características como píxeles o características extraídas.

    * Detección de Anomalías: KNN puede detectar anomalías en datos, como transacciones fraudulentas en tarjetas de crédito.

## Conclusiones

Este trabajo demuestra cómo utilizar el algoritmo K-Nearest Neighbors para predecir el comportamiento de compra en línea de los usuarios. El preprocesamiento de datos y la evaluación del modelo son etapas cruciales en el desarrollo de un sistema de IA efectivo.

El modelo puede ser afinado y mejorado mediante la exploración de otros algoritmos y técnicas de preprocesamiento de datos más avanzadas.