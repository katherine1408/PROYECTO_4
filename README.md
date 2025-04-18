# 🛒 Sprint 4 – Manipulación de Datos con Instacart

## 📌 Descripción del Proyecto

Este proyecto forma parte del Sprint 4 del bootcamp de Ciencia de Datos y tiene como objetivo aplicar técnicas de manipulación de datos (Data Wrangling) utilizando datos reales de la plataforma **Instacart**, una app de pedidos de comestibles online. El dataset ha sido adaptado para incluir valores faltantes y duplicados, lo cual permite practicar el preprocesamiento completo de datos reales.

## 🎯 Propósito

- Limpiar, transformar y preparar múltiples tablas con pandas.
- Detectar y manejar valores ausentes y duplicados.
- Integrar fuentes de datos (joins) para análisis más completos.
- Identificar patrones de consumo de clientes.
- Visualizar resultados de forma clara con gráficos interpretables.

## 🧰 Funcionalidad

El proyecto consta de tres grandes bloques:

### Etapa 1: Exploración y carga de datos
- Revisión general de los 5 archivos CSV.
- Configuración correcta de `pd.read_csv()` para formatos no estándar.

### Etapa 2: Preprocesamiento
- Conversión de tipos de datos.
- Identificación y tratamiento de valores ausentes y duplicados.
- Justificación de cada acción tomada.

### Etapa 3: Análisis exploratorio
#### A. Análisis del comportamiento de pedidos
- Verificación de valores válidos (`order_hour_of_day`, `order_dow`).
- Gráficos de frecuencia de pedidos por hora y día.
- Análisis del tiempo entre pedidos.

#### B. Preferencias de los clientes
- Comparación de hábitos entre miércoles y sábado.
- Frecuencia de pedidos por cliente.
- Top 20 productos más pedidos.

#### C. Análisis de reincidencia y comportamiento
- Promedio de artículos por pedido.
- Top 20 productos más “reordenados”.
- Proporción de reordenamiento por producto y por cliente.
- Productos más frecuentes como primer artículo en el carrito.

## 🗂️ Archivos utilizados

- `instacart_orders.csv`
- `products.csv`
- `order_products.csv`
- `aisles.csv`
- `departments.csv`

## 📊 Herramientas y Librerías

- Python  
- pandas  
- matplotlib  
- seaborn  

---

📌 Proyecto desarrollado en el Sprint 4 del programa de Data Science en **TripleTen**.
