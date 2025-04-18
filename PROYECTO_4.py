# importar librerías

import pandas as pd
import matplotlib.pyplot as plt

# leer conjuntos de datos en los DataFrames

orders        = pd.read_csv('instacart_orders.csv',sep=";")
products      = pd.read_csv('products.csv',sep=";")
aisles        =pd.read_csv('aisles.csv',sep=";" )
departments   =pd.read_csv('departments.csv',sep=";")
order_products=pd.read_csv('order_products.csv',sep=";")

# mostrar información del DataFrame
print(orders.info())
# mostrar información del DataFrame
products.info()
# mostrar información del DataFrame
aisles.info()
# mostrar información del DataFrame
departments.info()
# mostrar información del DataFrame
order_products.info(show_counts=True)

# Tras leer los archivos y revisar la información de los DataFrames, 
# hemos identificado la estructura y los tipos de datos de cada columna. 
# Esto nos permitirá detectar posibles valores ausentes o inconsistencia 

#   Paso 2. Preprocesamiento de los datos
# - Verifica y corrige los tipos de datos 
# - Identifica y completa los valores ausentes.
# - Identifica y elimina los valores duplicados.

# Revisa si hay pedidos duplicados
orders[orders.duplicated()]

#duplicated_orders = orders[orders.duplicated()]
orders.duplicated().sum()

#Según el analisis efectuado los pedidos duplicados fueron efectuados en las misma hora 
# y el mismo día.

# Verifica todos los pedidos que se hicieron el miércoles a las 2:00 a.m.

orders[(orders['order_dow'] == 3) & (orders['order_hour_of_day'] == 2)]

# Sugiere que ciertos usuarios tienen el hábito de realizar pedidos a esa hora.
# Este análisis puede ofrecer una visión sobre el comportamiento del usuario
# y ayudar a la plataforma a ajustar sus estrategias de marketing, promociones 
# y logística para maximizar la eficiencia y la satisfacción del cliente.

# Elimina los pedidos duplicados
orders.drop_duplicates(inplace=True)

# Vuelve a verificar si hay filas duplicadas
orders[orders.duplicated()]

# Vuelve a verificar únicamente si hay IDs duplicados de pedidos
orders[orders.duplicated(subset="order_id")]
# Se encontró valores duplicados en el data frame "orders", que fueron eliminados.

# Verifica si hay filas totalmente duplicadas
products[products.duplicated()]

# Revisa únicamente si hay ID de departamentos duplicados
departments[departments.duplicated(subset="department_id")]

# Revisa únicamente si hay nombres duplicados de productos (convierte los nombres a letras mayúsculas para compararlos mejor)
products["product_name"].str.upper().duplicated().sum()

# Revisa si hay nombres duplicados de productos no faltantes
products[(~products["product_name"].isna()) & (products["product_name"].str.upper().duplicated())]

# Despues de analizar el data frame "products", 
# se halló que existían duplicados en la columna "product_name", 
# de los cuales se convirtió a los nombres a mayusculas para un mejor analisis 
# y se determinó que existían 104 duplicados con valores no ausentes en dicha columna.

# Muy buen trabajo!! Desarrollaste de manera excelente el análisis de duplicados. Para complementar el análisis, qué podríamos decir de estos 104 productos duplicados? 
#     
# </div>

# ### `departments` data frame

# In[18]:


# Revisa si hay filas totalmente duplicadas
departments[departments.duplicated()]


# In[19]:


# Revisa únicamente si hay IDs duplicadas de productos
products[products.duplicated(subset="product_id")]


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# Se determinó que en el dataframe "departments" no existen valores duplicados.

# ### `aisles` data frame

# In[20]:


# Revisa si hay filas totalmente duplicadas
departments[departments.duplicated()]


# In[21]:


# Revisa únicamente si hay IDs duplicadas de productos
departments[departments.duplicated(subset='department_id')]


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# Se determino que el data frame "departments" no existen valores duplicados.

# ### `order_products` data frame

# In[22]:


# Revisa si hay filas totalmente duplicadas
order_products.duplicated().sum()


# In[23]:


# Vuelve a verificar si hay cualquier otro duplicado engañoso
order_products.duplicated(subset=["order_id","product_id"]).sum()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# Se determino que el data frame "order_products" no existen valores duplicados.

# ## Encuentra y elimina los valores ausentes
# 
# Al trabajar con valores duplicados, pudimos observar que también nos falta investigar valores ausentes:
# 
# * La columna `'product_name'` de la tabla products.
# * La columna `'days_since_prior_order'` de la tabla orders.
# * La columna `'add_to_cart_order'` de la tabla order_productos.

# ### `products` data frame

# In[24]:


# Encuentra los valores ausentes en la columna 'product_name'
products[products["product_name"].isna()]


# Describe brevemente cuáles son tus hallazgos.
# 
# Esto identifica todas las filas donde falta el nombre del producto.

# In[25]:


#  ¿Todos los nombres de productos ausentes están relacionados con el pasillo con ID 100?
products[(products["product_name"].isna()) & (products["aisle_id"]!=100)]


# Describe brevemente cuáles son tus hallazgos.
# 
# Comprobamos si todos los productos con nombres ausentes están relacionados con el pasillo 100, donde podríamos inferir un problema específico con la entrada de datos para este pasillo.

# In[26]:


# ¿Todos los nombres de productos ausentes están relacionados con el departamento con ID 21?
products[(products["product_name"].isna()) & (products["department_id"]!=21)]


# Describe brevemente cuáles son tus hallazgos.
# 
# Comprobamos si todos los productos con nombres ausentes están relacionados con el departamento 21, podríamos sospechar un problema específico con la entrada de datos para este departamento.

# In[27]:


# Usa las tablas department y aisle para revisar los datos del pasillo con ID 100 y el departamento con ID 21.

print(products[(products["aisle_id"] == 100) & (products["department_id"]==21)])


# Describe brevemente cuáles son tus hallazgos.
# 
# Comprobamos si todos los productos con nombres ausentes están relacionados con el departamento 21, podríamos sospechar un problema específico con la entrada de datos para este departamento.

# In[28]:


# Completa los nombres de productos ausentes con 'Unknown'
products.fillna('Unknown', inplace=True)
products.isna().sum()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Se reemplazo los valores ausentes, para poder procesarlos.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy buen trabajo!! Desarrollaste de manera excelente el análisis de valores faltantes y los llenaste con "unknown".
#     
# </div>

# ### `orders` data frame

# In[29]:


# Encuentra los valores ausentes
orders.isna().sum()


# In[30]:


# ¿Hay algún valor ausente que no sea el primer pedido del cliente?

orders[(orders["days_since_prior_order"].isna())&(orders["order_number"]!=1)]




# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Se hallaron valores ausentes en la columna days_since_prior_order del data frame orders, debido a que al ser las primeras compras no tienen días transcurridos desde el pedido anterior por lo que es razonable que tengan valores ausentes.

# ### `order_products` data frame

# In[31]:


# Encuentra los valores ausentes
order_products.isna().sum()


# In[32]:


# ¿Cuáles son los valores mínimos y máximos en esta columna?
order_products["add_to_cart_order"].min()


# In[33]:


order_products["add_to_cart_order"].max()


# Describe brevemente cuáles son tus hallazgos
# Se encontraron valores ausentes en la columna "add_to_cart_order" del data frame "order_products" cuyo valor minimo es 1 y valor maximo es 64

# In[34]:


# Guarda todas las IDs de pedidos que tengan un valor ausente en 'add_to_cart_order'
orders_id_ausentes= list(order_products[order_products["add_to_cart_order"].isna()]["order_id"].unique())
orders_id_ausentes= sorted(orders_id_ausentes)


# In[35]:


order_products.groupby("order_id")["product_id"].count().sort_values(ascending=False)


# In[36]:


# ¿Todos los pedidos con valores ausentes tienen más de 64 productos?
order_products[order_products['order_id'].isin(orders_id_ausentes)]['order_id'].value_counts()


# In[37]:


# Agrupa todos los pedidos con datos ausentes por su ID de pedido.
order_products.groupby("order_id")["product_id"].count()
order_products[order_products['order_id'].isin(orders_id_ausentes)].groupby('order_id').count()


# In[38]:


# Cuenta el número de 'product_id' en cada pedido y revisa el valor mínimo del conteo.
order_products[order_products['add_to_cart_order'].isnull()].groupby('order_id')['product_id'].count()


# Describe brevemente cuáles son tus hallazgos.
# 
# Se ha determinado de el analisis que existen ordenes que tienen un mayor valor de 64

# In[39]:


# Remplaza los valores ausentes en la columna 'add_to_cart? con 999 y convierte la columna al tipo entero.
order_products ['add_to_cart_order'] = order_products['add_to_cart_order'].fillna(999).astype(int)
order_products.isna().sum()


# Describe brevemente tus hallazgos y lo que hiciste con ellos.
# 
# Al descubrir valores ausentes en las ordenes de pedidos , se opto por reemplazarlos por 999 para poder procesar de los datos.
## Conclusiones

# En el preprocesamiento de datos hallamos valores ausentes en las columnas que probablemente se deban a un error en el ingreso de datos , por lo que se opto por reemplazarlos para poder procesarlos posteriormente.

# <div class="alert alert-block alert-warning">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# 
# Muy buena conclusión de esta base. Pero qué podríamos decir de los pedidos que tienen más de 64 productos?
# </div>

# <div class="alert alert-block alert-info">
# <b>Al contar las ordenes nos damos cuenta que el número máximo es 64, sin embargo al realizar un analisis más profundo cuando agrupamos por ordenes y contamos los productos registrados nos damo cuenta que hay más de 64 productos , lo que se puede inferir que los datos ausentes nulos , pudo hacer una falla en el registro de los demás productos.</b> <a class="tocSkip"></a>
# </div>

# # Paso 3. Análisis de los datos
# 
# Una vez los datos estén procesados y listos, haz el siguiente análisis:

# # [A] Fácil (deben completarse todos para aprobar)
# 
# 1. Verifica que los valores en las columnas `'order_hour_of_day'` y `'order_dow'` en la tabla orders sean razonables (es decir, `'order_hour_of_day'` oscile entre 0 y 23 y `'order_dow'` oscile entre 0 y 6).
# 2. Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
# 3. Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
# 4. Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, y comenta sobre los valores mínimos y máximos.

# <div class="alert alert-block alert-danger">
# <b>Comentario Revisor</b> <a class="tocSkip"></a>
# 
# En este primer punto nos piden mostrar que los valores sean sensibles. Para hacerlo puedes explorar el uso de la función .unique() o .value_counts(). 
# </div>
# 
# 

# <div class="alert alert-block alert-info">
# <b>Se realizó modificación y se aplicó método value_counts().</b> <a class="tocSkip"></a>
# </div>

# ### [A1] Verifica que los valores sean sensibles

# In[40]:


# Verifica que los valores en las columnas 'order_hour_of_day' y 'order_dow' 
# en la tabla orders sean razonables (es decir, 'order_hour_of_day' oscile entre 0 y 23 y 'order_dow' oscile entre 0 y 6)


orders[(orders['order_hour_of_day']>0)&(orders['order_hour_of_day']<23)].value_counts()
orders[(orders['order_dow']>0)&(orders['order_dow']<6)].value_counts()


# ### [A2] Para cada hora del día, ¿cuántas personas hacen órdenes?

# In[41]:


#Crea un gráfico que muestre el número de personas que hacen pedidos dependiendo de la hora del día.
compras_horas_del_dia=orders['order_hour_of_day'].value_counts().sort_index()
compras_horas_del_dia.plot(
    kind='bar',
    title="Ordenes por hora del día",
    xlabel="Hora del día",
    ylabel="Numero de ordenes")
    


# Escribe aquí tus conclusiones
# De acuerdo al gráfico se puede observar que hay mayor frecuencia de ordenes entre las 10  y 15 horas

# ### [A3] ¿Qué día de la semana compran víveres las personas?

# In[42]:


#Crea un gráfico que muestre qué día de la semana la gente hace sus compras.
compras_dia_de_la_semana=orders['order_dow'].value_counts().sort_index()

compras_dia_de_la_semana.plot(
    kind='bar',
    title="Compras por día",
    xlabel="Días",
    ylabel="Compras")


# Escribe aquí tus conclusiones
# 
# De acuerdo al gráfico se puede observar que hay mayor frecuencia de ordenes los días domingo y lunes.

# ### [A4] ¿Cuánto tiempo esperan las personas hasta hacer otro pedido? Comenta sobre los valores mínimos y máximos.

# In[43]:


#Crea un gráfico que muestre el tiempo que la gente espera hasta hacer su siguiente pedido, 
#y comenta sobre los valores mínimos y máximos.
tiempo_de_las_ordenes=orders['days_since_prior_order']
tiempo_de_las_ordenes.plot(
    kind='hist',
    bins=30,
    title="Tiempo de espera para el siguiente pedido",
    )


# In[44]:


orders['days_since_prior_order'].min()


# In[45]:


orders['days_since_prior_order'].max()


# Escribe aquí tus conclusiones
# 
# Al determinar el valor máximo podemos observar que el tiempo máximo despues de la orden anterior es de 30 días.

# # [B] Intermedio (deben completarse todos para aprobar)
# 
# 1. ¿Existe alguna diferencia entre las distribuciones `'order_hour_of_day'` de los miércoles y los sábados? Traza gráficos de barra de `'order_hour_of_day'` para ambos días en la misma figura y describe las diferencias que observes.
# 2. Grafica la distribución para el número de órdenes que hacen los clientes (es decir, cuántos clientes hicieron solo 1 pedido, cuántos hicieron 2, cuántos 3, y así sucesivamente...).
# 3. ¿Cuáles son los 20 principales productos que se piden con más frecuencia (muestra su identificación y nombre)?

# ### [B1] Diferencia entre miércoles y sábados para  `'order_hour_of_day'`. Traza gráficos de barra para los dos días y describe las diferencias que veas.

# In[65]:


ordenes_miercoles = orders[orders['order_dow'] == 3]['order_hour_of_day'].value_counts().sort_index()


# In[47]:


ordenes_sabado = orders[orders['order_dow'] == 6]['order_hour_of_day'].value_counts().sort_index()


# In[48]:


miercoles_y_sabado=pd.concat([ordenes_miercoles,ordenes_sabado], axis=1)
miercoles_y_sabado.columns=["Miercoles","sabado"]
miercoles_y_sabado.plot(
    kind='bar',
    title="Comparación de ordenes Miercoles y Sabado",
    xlabel="Hora del día",
    ylabel="Numero de ordenes")
#orders_wed.value_counts().sort_index().plot(kind='bar', alpha=0.5, label='Miércoles')


# Escribe aquí tus conclusiones
# 
# 
# Del gráfico de barras observamos que en comparación del día sábado y miércoles existe una diferencia en la cantidad de numero de ordenes en relacion de las horas pico, el día sabado se tiene mayor numero de ordenes.
# 

# ### [B2] ¿Cuál es la distribución para el número de pedidos por cliente?

# In[49]:


#orders['user_id'].value_counts().plot(kind='hist', bins=100,title="Distribución total de ordenes")

order_count_per_user = orders.groupby('user_id')['order_id'].count().sort_values()
order_count_per_user
order_count_per_user.plot(kind='hist',
                          bins=28,
                          title='Distribution of total orders')                        



# Del gráfico podemos determinar que hay mayor frecuencia de cantidad de ordenes en las primeras compras 

# Escribe aquí tus conclusiones

# ### [B3] ¿Cuáles son los 20 productos más populares (muestra su ID y nombre)?

# In[50]:


product_counts = order_products['product_id'].value_counts().reset_index()
product_counts.columns = ['product_id', 'count']
popular_products = pd.merge(product_counts, products, on='product_id', how='left')


# In[51]:


print(product_counts.head(20))


# In[52]:


print(popular_products.head(20))


# Escribe aquí tus conclusiones
# 
# Del analisis realizado observamos que los 20 productos más populares son de consumo masivo.

# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy buen desarrollo de la sección. Desarrollaste de buena manera todos los análisis y lo complementaste con una gráfica. 
# </div>

# # [C] Difícil (deben completarse todos para aprobar)
# 
# 1. ¿Cuántos artículos suelen comprar las personas en un pedido? ¿Cómo es la distribución?
# 2. ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?
# 3. Para cada producto, ¿cuál es la tasa de repetición del pedido (número de repeticiones de pedido/total de pedidos?
# 4. Para cada cliente, ¿qué proporción de los productos que pidió ya los había pedido? Calcula la tasa de repetición de pedido para cada usuario en lugar de para cada producto.
# 5. ¿Cuáles son los 20 principales artículos que la gente pone primero en sus carritos (muestra las IDs de los productos, sus nombres, y el número de veces en que fueron el primer artículo en añadirse al carrito)?

# ### [C1] ¿Cuántos artículos compran normalmente las personas en un pedido? ¿Cómo es la distribución?

# In[53]:


order_products.groupby('order_id').size().plot(kind='hist', bins=5)


# Escribe aquí tus conclusiones
# En promedio se compran 20 articulos en un pedido

# ### [C2] ¿Cuáles son los 20 principales artículos que vuelven a pedirse con mayor frecuencia (muestra sus nombres e IDs de los productos)?

# In[54]:


#top_20_reordered = print(order_products[order_products['reordered'] == 1]['product_id'].value_counts().head(20))
reordered_products = order_products[order_products['reordered'] == 1]
reordered_counts = reordered_products['product_id'].value_counts().reset_index()
reordered_counts.columns = ['product_id', 'reorder_count']
popular_reordered_products = pd.merge(reordered_counts, products, on='product_id', how='left')


# In[55]:


print(popular_reordered_products[['product_id', 'product_name']].head(20))


# Escribe aquí tus conclusiones
# Del analisis realizado observamos que los 20 productos más populares y que vuelven a pedirse con mayor frecuencia son de consumo masivo.
# 

# ### [C3] Para cada producto, ¿cuál es la proporción de las veces que se pide y que se vuelve a pedir?

# In[56]:


total_orders = order_products['product_id'].value_counts().reset_index()
total_orders.columns = ['product_id', 'total_orders']
reordered_counts = order_products[order_products['reordered'] == 1]['product_id'].value_counts().reset_index()
reordered_counts.columns = ['product_id', 'reorder_count']


# In[57]:


product_reorder_info = pd.merge(total_orders, reordered_counts, on='product_id', how='left')
product_reorder_info['reorder_count'].fillna(0, inplace=True)
product_reorder_info['reorder_ratio'] = product_reorder_info['reorder_count'] / product_reorder_info['total_orders']
product_reorder_info = pd.merge(product_reorder_info, products, on='product_id', how='left')


# In[58]:


print(product_reorder_info[['product_id', 'product_name', 'reorder_ratio']])


# Escribe aquí tus conclusiones
# Del analisis obtenemos que la mayor proporcion de tasa de reordenes son los productos organicos y, por lo tanto, son más populares para ser pedidos nuevamente.

# ### [C4] Para cada cliente, ¿qué proporción de sus productos ya los había pedido?

# In[59]:


orders_products_merged = pd.merge(order_products, orders, on='order_id')


# In[60]:


reorder_rate = orders_products_merged.groupby('user_id')['reordered'].mean()
reorder_rate


# Escribe aquí tus conclusiones:
# 
# Esta información  permite ver qué proporción de los productos pedidos por cada cliente son reordenes, proporcionando información sobre la lealtad del cliente y los hábitos de compra.

# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy buena utilización  de la agrupación de los valores. Pero en este caso nos piden sacar el dato para cada cliente, en este sentido dentro del groupby te sugiero utilizar la variable 'user_id' y en este caso el ejercicio hace referencia a cuál es la proporción de veces que se vuleve a pedir cada producto. Es por ello que la variable que nos interesa hacer el mean es ['reordered'] 
#     
# </div>

# <div class="alert alert-block alert-info">
# <b>Se realizó modificación </b> <a class="tocSkip"></a>
# </div>

# ### [C5] ¿Cuáles son los 20 principales artículos que las personas ponen primero en sus carritos?

# In[61]:


df_merge = order_products.merge(products)
first_in_cart = df_merge[df_merge['add_to_cart_order'] == 1]
first_in_cart


# In[62]:


first_count = first_in_cart.groupby(['product_id', 'product_name'])['product_id'].count().sort_values(ascending=False)
first_count


# In[63]:


first_count_as_df = first_count.reset_index(name='count')
first_count_as_df.head(20)


# Escribe aquí tus conclusiones:
# EL código produce una tabla con los IDs de los productos y los nombres de los 20 productos que más frecuentemente son agregados primero al carrito, lo que nos  permitire identificar los productos que los usuarios tienden a considerar primero en sus compras.

# ### Conclusion general del proyecto:

# En este proyecto, hemos realizado un análisis  de los datos de pedidos de Instacart para extraer 
# información valiosa sobre el comportamiento de compra de los usuarios:
# Identificamos los 20 productos más populares y los productos que más se reordenan,o que ayuda a entender 
# los hábitos de compra de los clientes hacia productos específicos, al determinar los 20 principales artículos
# que los usuarios agregan primero a sus carritos.

# <div class="alert alert-block alert-warning">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# En general creo que hiciste un muy buen trabajo con el proyecto, pudiste limpiar y trabajar las bases de datos de beuna manera, análisis de duplicados, y de valores faltantes. Además dearrollaste de buena manera los diferentes anális que se solicitaban y cuando podías los complementabas con greaficas. No obstante, recuerda que siempre podemos mejorar y te menciono algunos puntos que debes considerar:
# 
# * Revisar que los filtros sean correctos en algunos apartados con base en la indicación
#     
#     
# *  Realizar análisis complementarios eliminando los valores que parecen ser atípicos. 
#     
# *  Realizar gráficas de barras en algunos análisis para complementarlos.
#     
# *  Ordenar los datos para que sean más claros los resultados.
#     
# *  Profundizar en los resultados intermedios y en la conclusión final.
# 
# </div>
