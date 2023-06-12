
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import datetime


#---------------------------------cargamos los datos-------------------------------------------------------------------------------------
df = pd.read_csv('SENCOVAC_versionReducida_Blancos(CSV).csv', skiprows= 1, sep='[;,:\s+]', names=range(225))
df.fillna(value=0, inplace=True)
# Convertir la columna de fecha de nacimiento al formato de fecha
df.iloc[:, 2] = pd.to_datetime(df.iloc[:, 2], format='%d/%m/%Y')

# Calcular la edad restando el año de nacimiento al año actual
df['Edad'] = pd.to_datetime('today').year - df.iloc[:, 2].dt.year
#voy a eliminar las columnas 0 y 10 xq ambas contienen variables del tipo objeto que no me permitirian trabajar con 
#clusteres y como la columna 0 es el id y la columna 10 es el peso del paciente, no son variables importantes para nuestro estudio
df = df.drop(0, axis=1)
df = df.drop(10, axis=1)

#------------------------------grafico para visualizar las edades de los pacientes con los que trabajamos------------------------------------------------------------------------------

# Obtén los datos de edad de tu dataframe
edades = df['Edad']

# Define los rangos de edad y los colores correspondientes
rangos_edad = ['20-40', '40-60', '60-80', '80+']
colores = ['blue', 'green', 'orange', 'red']

# Calcula la cantidad de pacientes en cada grupo de edad
cantidades = [
    len(edades[(edades >= 20) & (edades <= 40)]),
    len(edades[(edades > 40) & (edades <= 60)]),
    len(edades[(edades > 60) & (edades <= 80)]),
    len(edades[edades > 80])
]

# Calcula los porcentajes de pacientes en cada grupo de edad
total_pacientes = len(edades)
porcentajes = [cantidad / total_pacientes * 100 for cantidad in cantidades]

# Crea el gráfico circular
plt.pie(cantidades, labels=rangos_edad, colors=colores)

# Crea la leyenda recuadrada
legend_labels = [f'{porcentaje:.1f}% - {cantidades[i]} pacientes' for i, porcentaje in enumerate(porcentajes)]
plt.legend(legend_labels, loc='upper left', bbox_to_anchor=(0.5, -0.1), frameon=True)

# Configura el aspecto del gráfico
plt.title('Distribución de Edades de los Pacientes')
plt.axis('equal')

# Muestra el gráfico
plt.show()
#---------------------------------------------------grafico de dispersion de edades y anticuerpos-------------------------------------------------------------------------------------

# Obtener los valores de la edad (columna 'Edad')
edades = df['Edad']

# Obtener los valores de los anticuerpos (columna 31)
anticuerpos = df.iloc[:, 31]

# Crear la figura y los ejes del gráfico
fig, ax = plt.subplots()

# Graficar los puntos y asignar colores según los rangos de edad
for edad, anticuerpo in zip(edades, anticuerpos):
    if 20 <= edad <= 40:
        color = 'blue'
        ax.scatter(anticuerpo, edad, color=color)
    elif 40 <= edad <= 60:
        color = 'green'
        ax.scatter(anticuerpo, edad, color=color)
    elif 60 <= edad <= 80:
        color = 'orange'
        ax.scatter(anticuerpo, edad, color=color)
    elif edad >= 80:
        color = 'red'
        ax.scatter(anticuerpo, edad, color=color)
    else:
        continue

# Calcular la media de anticuerpos para cada grupo de edad
media_anticuerpos_2040 = df.loc[(edades >= 20) & (edades <= 40)].iloc[:, 31].mean()
media_anticuerpos_4060 = df.loc[(edades > 40) & (edades <= 60)].iloc[:, 31].mean()
media_anticuerpos_6080 = df.loc[(edades > 60) & (edades <= 80)].iloc[:, 31].mean()
media_anticuerpos_80plus = df.loc[edades > 80].iloc[:, 31].mean()

# Graficar los puntos negros para las medias de anticuerpos de los grupos de edad
ax.scatter(media_anticuerpos_2040, 30, color='black')
ax.scatter(media_anticuerpos_4060, 50, color='black')
ax.scatter(media_anticuerpos_6080, 70, color='black')
ax.scatter(media_anticuerpos_80plus, 90, color='black')

# Configurar los ejes y las etiquetas
ax.set_xlabel('Número de Anticuerpos')
ax.set_ylabel('Edad del Paciente')
ax.set_title('Edad del Paciente en función de la Cantidad de Anticuerpos')

# Agregar leyenda para las medias de anticuerpos
leyenda = f'Media de anticuerpos del grupo 20-40: {media_anticuerpos_2040:.2f}\n' \
          f'Media de anticuerpos del grupo 40-60: {media_anticuerpos_4060:.2f}\n' \
          f'Media de anticuerpos del grupo 60-80: {media_anticuerpos_6080:.2f}\n' \
          f'Media de anticuerpos del grupo 80+: {media_anticuerpos_80plus:.2f}'

ax.text(0.1, -0.3, leyenda,
        transform=ax.transAxes, fontsize=10, bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round'))

# Mostrar el gráfico
plt.show()

#--------------------------------------------------------------Grafico para analisis de anticuerpos E1 por tipo de paciente TRS------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

# Obtener los valores de los anticuerpos (columna 33)
anticuerpos = df.iloc[:, 31]

# Obtener los valores de los tipos de pacientes (columna 12)
tipos_pacientes = df.iloc[:, 10]

# Filtrar los valores de anticuerpos y tipos de pacientes correspondientes a cada categoría
anticuerpos_transplante = anticuerpos[tipos_pacientes == 1]
anticuerpos_peritoneal = anticuerpos[tipos_pacientes == 2]
anticuerpos_hemodialisis = anticuerpos[tipos_pacientes == 3]

# Definir los colores para cada tipo de paciente
colores = ['red', 'green', 'blue']

# Crear la figura y los ejes del gráfico
fig, ax = plt.subplots()

# Crear los valores del eje x
x = np.arange(3)

# Graficar las barras de cada tipo de paciente
ax.bar(x[0], anticuerpos_transplante.mean(), color=colores[0], label='Trasplante')
ax.bar(x[1], anticuerpos_peritoneal.mean(), color=colores[1], label='Diálisis Peritoneal')
ax.bar(x[2], anticuerpos_hemodialisis.mean(), color=colores[2], label='Hemodiálisis')

# Configurar los ejes y las etiquetas
ax.set_xticks(x)
ax.set_xticklabels(['Trasplante', 'Diálisis Peritoneal', 'Hemodiálisis'])
ax.set_ylabel('Número de Anticuerpos')
ax.set_title('Número de Anticuerpos por Tipo de Paciente')

# Mostrar la leyenda
ax.legend()

#Mostrar el gráfico
plt.show()

#--------------------------------------------------Anticuerpos Etapa 1 Pacientes con transplante--------------------------------------------------------------------------------------
# Filtrar los valores de los niveles de anticuerpos en la etapa 1 para los pacientes que han sufrido un trasplante
etapa1_antibodies_transplante = df.loc[df.iloc[:, 10] == 1, 31]  

# Calcular el promedio de los niveles de anticuerpos en la etapa 1 para los pacientes que han sufrido un trasplante
promedio_etapa1_transplante = etapa1_antibodies_transplante.mean()

# Crear el gráfico
fig, ax = plt.subplots()
ax.plot(etapa1_antibodies_transplante, color='orange', label='Niveles de anticuerpos')
ax.axhline(promedio_etapa1_transplante, color='blue', linestyle='--', label='Promedio')

# Agregar el valor de la media en el eje y
ax.text(0, promedio_etapa1_transplante, f'Promedio: {promedio_etapa1_transplante:.2f}', color='blue', ha='left', va='bottom')

# Personalizar el gráfico
ax.set_xlabel('Pacientes con trasplante')
ax.set_ylabel('Niveles de anticuerpos')
ax.set_title('Promedio de niveles de anticuerpos en la etapa 1')

# Mostrar el gráfico
plt.legend()
plt.show()

#----------------------------------------------Anticuerpos Etapa 1 Pacientes con dialisis peritoneal---------------------------------------------------------------------

# Filtrar los valores de los niveles de anticuerpos en la etapa 1 para los pacientes que han sufrido dialisis peritoneal
etapa1_antibodies_transplante = df.loc[df.iloc[:, 10] == 2, 31]  

# Calcular el promedio de los niveles de anticuerpos en la etapa 1 para los pacientes que han sufrido dialisis peritoneal
promedio_etapa1_transplante = etapa1_antibodies_transplante.mean()

# Crear el gráfico
fig, ax = plt.subplots()
ax.plot(etapa1_antibodies_transplante, color='orange', label='Niveles de anticuerpos')
ax.axhline(promedio_etapa1_transplante, color='blue', linestyle='--', label='Promedio')

# Agregar el valor de la media en el eje y
ax.text(0, promedio_etapa1_transplante, f'Promedio: {promedio_etapa1_transplante:.2f}', color='blue', ha='left', va='bottom')

# Personalizar el gráfico
ax.set_xlabel('Pacientes con diálisis peritoneal')
ax.set_ylabel('Niveles de anticuerpos')
ax.set_title('Promedio de niveles de anticuerpos en la etapa 1')

# Mostrar el gráfico
plt.legend()
plt.show()

#-------------------------------------------Anticuerpos Etapa 1 Pacientes con hemodialisis-------------------------------------------------------------------------

# Filtrar los valores de los niveles de anticuerpos en la etapa 1 para los pacientes que han sufrido hemodialisis
etapa1_antibodies_transplante = df.loc[df.iloc[:, 10] == 3, 31]  

# Calcular el promedio de los niveles de anticuerpos en la etapa 1 para los pacientes que han sufrido hemodialisis
promedio_etapa1_transplante = etapa1_antibodies_transplante.mean()

# Crear el gráfico
fig, ax = plt.subplots()
ax.plot(etapa1_antibodies_transplante, color='orange', label='Niveles de anticuerpos')
ax.axhline(promedio_etapa1_transplante, color='blue', linestyle='--', label='Promedio')

# Agregar el valor de la media en el eje y
ax.text(0, promedio_etapa1_transplante, f'Promedio: {promedio_etapa1_transplante:.2f}', color='blue', ha='left', va='bottom')

# Personalizar el gráfico
ax.set_xlabel('Pacientes con hemodiálisis')
ax.set_ylabel('Niveles de anticuerpos')
ax.set_title('Promedio de niveles de anticuerpos en la etapa 1')

# Mostrar el gráfico
plt.legend()
plt.show()

