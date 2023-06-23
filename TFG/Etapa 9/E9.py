import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#-------------------------------------------------------------ETAPA 9------------------------------------------------------------------------------------------------------------
#importamos los datos
#---------------------------------cargamos los datos--------------------------------------
df = pd.read_csv('SENCOVAC_versionReducida_Blancos(CSV).csv', skiprows= 1, sep='[;,:\s+]', names=range(225))
df.fillna(value=0, inplace=True)
# Aplicar la conversión a timestamp a la columna 'fecha'
# df[225] = df[2].apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y').timestamp())
# d_col1 = df.pop(225)
# df.insert(1, 225, d_col1)
# df.drop(columns=[2], inplace=True)
import datetime
# Convertir la columna de fecha de nacimiento al formato de fecha
df.iloc[:, 2] = pd.to_datetime(df.iloc[:, 2], format='%d/%m/%Y')
# Calcular la edad restando el año de nacimiento al año actual
df['Edad'] = pd.to_datetime('today').year - df.iloc[:, 2].dt.year
#voy a eliminar las columnas 0 y 10 xq ambas contienen variables del tipo objeto que no me permitirian trabajar con
#clusteres y como la columna 0 es el id y la columna 10 es el peso del paciente, no son variables importantes para nuestro estudio
df = df.drop(0, axis=1)
df = df.drop(10, axis=1)
#------------------------------------------------------Analisis de infeccion y enfermedad-------------------------------------------------------------------------------

# Obtener los datos de las columnas 43 (pacientes infectados) y 44 (pacientes enfermos)
pacientes_infectados = df[df.iloc[:, 145] == 1]  # Filtrar pacientes infectados con valor 1 en columna 43, PACIENTES INFECTADOS
pacientes_enfermos = df[df.iloc[:, 146] == 1]  # Filtrar pacientes enfermos con valor 1 en columna 44, PACIENTES ENFERMOS

# Contar pacientes infectados por tipo de paciente (columna 12)
pacientes_infectados_tipo = pacientes_infectados.iloc[:, 10].value_counts().sort_index()

# Contar pacientes enfermos por tipo de paciente (columna 12)
pacientes_enfermos_tipo = pacientes_enfermos.iloc[:, 10].value_counts().sort_index()

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots(figsize=(8, 6))

# Configurar las posiciones de las barras en el eje x
x = [0, 1]  # Dos posiciones: 0 para pacientes infectados, 1 para pacientes enfermos

# Graficar la barra de pacientes infectados dividida por tipo de paciente
colores = ['red', 'green', 'blue']

# Graficar la barra de pacientes infectados dividida por tipo de paciente
ax.bar(x[0], pacientes_infectados_tipo.values[1], color=colores[0], label='Paciente con transplante')
ax.bar(x[0], pacientes_infectados_tipo.values[2], bottom=pacientes_infectados_tipo.values[1], color=colores[1], label='Paciente con Diálisis Peritoneal')
ax.bar(x[0], pacientes_infectados_tipo.values[3], bottom=pacientes_infectados_tipo.values[1] + pacientes_infectados_tipo.values[2], color=colores[2], label='Paciente con hemodiálisis')

# Graficar la barra de pacientes enfermos dividida por tipo de paciente
ax.bar(x[1], pacientes_enfermos_tipo.values[1], color=colores[0])
ax.bar(x[1], pacientes_enfermos_tipo.values[2], bottom=pacientes_enfermos_tipo.values[1], color=colores[1])
ax.bar(x[1], pacientes_enfermos_tipo.values[3], bottom=pacientes_enfermos_tipo.values[1] + pacientes_enfermos_tipo.values[2], color=colores[2])



# Configurar las etiquetas y los títulos de los ejes
ax.set_xticks(x)
ax.set_xticklabels(['Pacientes Infectados', 'Pacientes Enfermos'])
ax.set_ylabel('Cantidad de Pacientes')
ax.set_title('Comparación de Pacientes Infectados y Enfermos por Tipo de Paciente')

# Agregar una leyenda
ax.legend(fontsize=8)


# Mostrar el gráfico
plt.tight_layout()
plt.show()

conteo_1 = (df.iloc[:, 145] == 1).sum()
print("Número total de pacientes infectados:", conteo_1)
conteo_2 = ((df.iloc[:,145] == 1) & (df.iloc[:, 10] == 1)).sum()
print("Número de pacientes con transplante infectados:", conteo_2)
conteo_3 = ((df.iloc[:, 145] == 1) & (df.iloc[:, 10] == 2)).sum()
print("Número de pacientes con diálisis peritoneal infectados:", conteo_3)
conteo_4 = ((df.iloc[:, 145] == 1) & (df.iloc[:, 10] == 3)).sum()
print("Número de pacientes con hemodiálisis infectados:", conteo_4)

conteo_5 = (df.iloc[:, 146] == 1).sum()
print("Número total de pacientes enfermos:", conteo_5)
conteo_6 = ((df.iloc[:, 146] == 1) & (df.iloc[:, 10] == 1)).sum()
print("Número de pacientes con transplante enfermos:", conteo_6)
conteo_7 = ((df.iloc[:, 146] == 1) & (df.iloc[:, 10] == 2)).sum()
print("Número de pacientes con diálisis peritoneal enfermos:", conteo_7)
conteo_8 = ((df.iloc[:,146] == 1) & (df.iloc[:, 10] == 3)).sum()
print("Número de pacientes con hemodiálisis enfermos:", conteo_8)
#-------------------------------------------------------------------------Analisis por edad-----------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# Filtrar los pacientes con trasplante e infectados
pacientes_transplante_infectados = df[(df.iloc[:, 10] == 3) & (df.iloc[:, 146] == 1)]

# Obtén los datos de edad de los pacientes filtrados
edades = pacientes_transplante_infectados['Edad']

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

# Crea el gráfico circular
plt.pie(cantidades, labels=rangos_edad, colors=colores)
# Filtra los colores y las etiquetas que no están presentes en el gráfico
colores_presentes = [colores[i] for i, cantidad in enumerate(cantidades) if cantidad > 0]
etiquetas_presentes = [f'{etiqueta} {cantidad} pacientes' for etiqueta, cantidad in zip(rangos_edad, cantidades) if cantidad > 0]

# Crea la leyenda con los colores y etiquetas presentes
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colores_presentes]
plt.legend(handles, etiquetas_presentes, loc='lower right')
# Configura el aspecto del gráfico
plt.title('Distribución de Edades de los Pacientes con hemodiálisis y enfermos')

# Muestra el gráfico
plt.show()
#---------------------------------------------------grafico de dispersion de edades y anticuerpos-------------------------------------------------------------------------------------

# Obtener los valores de la edad (columna 'Edad')
edades = df['Edad']

# Obtener los valores de los anticuerpos (columna 31)
anticuerpos = df.iloc[:, 192]

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
media_anticuerpos_2040 = df.loc[(edades >= 20) & (edades <= 40)].iloc[:,192].mean()
media_anticuerpos_4060 = df.loc[(edades > 40) & (edades <= 60)].iloc[:, 192].mean()
media_anticuerpos_6080 = df.loc[(edades > 60) & (edades <= 80)].iloc[:, 192].mean()
media_anticuerpos_80plus = df.loc[edades > 80].iloc[:, 192].mean()

# Graficar los puntos negros para las medias de anticuerpos de los grupos de edad
ax.scatter(media_anticuerpos_2040, 30, color='black')
ax.scatter(media_anticuerpos_4060, 50, color='black')
ax.scatter(media_anticuerpos_6080, 70, color='black')
ax.scatter(media_anticuerpos_80plus, 90, color='black')

# Configurar los ejes y las etiquetas
ax.set_xlabel('Número de Anticuerpos')
ax.set_ylabel('Edad del Paciente')
ax.set_title('Cantidad de Anticuerpos en función de la Edad del Paciente')

# Agregar leyenda para las medias de anticuerpos
leyenda = f'Media de anticuerpos del grupo 20-40: {media_anticuerpos_2040:.2f}\n' \
          f'Media de anticuerpos del grupo 40-60: {media_anticuerpos_4060:.2f}\n' \
          f'Media de anticuerpos del grupo 60-80: {media_anticuerpos_6080:.2f}\n' \
          f'Media de anticuerpos del grupo 80+: {media_anticuerpos_80plus:.2f}'

ax.text(0.1, -0.3, leyenda,
        transform=ax.transAxes, fontsize=10, bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round'))

# Mostrar el gráfico
plt.show()

