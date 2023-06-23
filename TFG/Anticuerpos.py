#------------------------------------------------Análisis de anticuerpos------------------------------------------------------------------------------------------------------
import pandas as pd

# Inicializar una lista para almacenar las medias de anticuerpos por etapa
medias_etapas_transplante = []

# Calcular la media de anticuerpos de pacientes con trasplante en cada etapa
for etapa in range(187, 193):
    media_etapa = df.loc[df.iloc[:, 10] == 1, df.columns[etapa]].mean()
    medias_etapas_transplante.append(media_etapa)

# Imprimir los resultados
print("Medias de anticuerpos de los pacientes con trasplante por etapa:")
for i, media_etapa in enumerate(medias_etapas_transplante, start=1):
    print("Etapa", i, ":", media_etapa)

import pandas as pd

# Inicializar una lista para almacenar las medias de anticuerpos por etapa para pacientes con hemodiálisis
medias_etapas_hemodialisis = []

# Inicializar una lista para almacenar las medias de anticuerpos por etapa para pacientes con diálisis peritoneal
medias_etapas_peritoneal = []

# Calcular la media de anticuerpos de pacientes con hemodiálisis y diálisis peritoneal en cada etapa
for etapa in range(187, 193):
    media_hemodialisis = df.loc[df.iloc[:, 10] == 3, df.columns[etapa]].mean()
    medias_etapas_hemodialisis.append(media_hemodialisis)

    media_peritoneal = df.loc[df.iloc[:, 10] == 2, df.columns[etapa]].mean()
    medias_etapas_peritoneal.append(media_peritoneal)

# Imprimir los resultados
print("Medias de anticuerpos de los pacientes con hemodiálisis por etapa:")
for i, media_etapa in enumerate(medias_etapas_hemodialisis, start=1):
    print("Etapa", i, ":", media_etapa)

print("\nMedias de anticuerpos de los pacientes con diálisis peritoneal por etapa:")
for i, media_etapa in enumerate(medias_etapas_peritoneal, start=1):
    print("Etapa", i, ":", media_etapa)

