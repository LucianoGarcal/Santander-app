# -*- coding: utf-8 -*-
"""Aplicacion Proyecto Santander.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H-lAxgLEXgway9AKr_if6tWQL-mlr9PA
"""

import sys
import numpy as np
import os.path
import pandas as pd

# Subimos el archivo
from google.colab import files
uploaded = files.upload()

df_2020 = pd.read_excel ("Proyect_SPA_2020.xlsx")
df_2020.head(5)

df_2020.describe()

df_2020.info()

df_2021 = pd.read_excel ("Proyect_SPA_2021.xlsx")
df_2021.head(5)

df_2021.describe()

df_2021.info()

df_2022 = pd.read_excel ("Proyect_SPA_2022.xlsx")
df_2022.head(5)

df_2022.describe()

df_2022.info()

df_intermed = pd.concat([df_2020, df_2021])

df_intermed.head()

df_intermed.info ()

df_20_21=df_intermed.rename( columns={'Support people - Global':'Think Customer – Pienso en el cliente - Global', 'Support people - Autovaloracion': 'Think Customer – Pienso en el cliente - Autovaloracion', 'Support people - Manager': 'Think Customer – Pienso en el cliente - Manager', 'Support people - Colaboradores': 'Think Customer – Pienso en el cliente - Colaboradores',
                                      'Embrace change - Global': 'Embrace Change – Impulso el cambio - Global', 'Embrace change - Autovaloracion': 'Embrace Change – Impulso el cambio - Autovaloracion', 'Embrace change - Manager': 'Embrace Change – Impulso el cambio - Manager', 'Embrace change - Colaboradores': 'Embrace Change – Impulso el cambio - Colaboradores'})

df_20_21.info()

df_20_21

df_20_21['Act Now – Actúo con rapidez - Global']= df_20_21[["Keep promises - Global", "Bring passion - Global"]].mean(axis=1)
df_20_21['Move Together – Trabajo en equipo - Global']= df_20_21[["Actively collaborate - Global", "Show respect - Global"]].mean(axis=1)
df_20_21['Speak Up – Hablo abiertamente - Global']= df_20_21[["Truly listen - Global", "Talk straight - Global"]].mean(axis=1)
df_20_21['Act Now – Actúo con rapidez - Autovaloracion']= df_20_21[["Keep promises - Autovaloracion", "Bring passion - Autovaloracion"]].mean(axis=1)
df_20_21['Move Together – Trabajo en equipo - Autovaloracion']= df_20_21[["Actively collaborate - Autovaloracion", "Show respect - Autovaloracion"]].mean(axis=1)
df_20_21['Speak Up – Hablo abiertamente - Autovaloracion']= df_20_21[["Truly listen - Autovaloracion", "Talk straight - Autovaloracion"]].mean(axis=1)
df_20_21['Act Now – Actúo con rapidez - Manager']= df_20_21[["Keep promises - Manager", "Bring passion - Manager"]].mean(axis=1)
df_20_21['Move Together – Trabajo en equipo - Manager']= df_20_21[["Actively collaborate - Manager", "Show respect - Manager"]].mean(axis=1)
df_20_21['Speak Up – Hablo abiertamente - Manager']= df_20_21[["Truly listen - Manager", "Talk straight - Manager"]].mean(axis=1)
df_20_21['Act Now – Actúo con rapidez - Colaboradores']= df_20_21[["Keep promises - Colaboradores", "Bring passion - Colaboradores"]].mean(axis=1)
df_20_21['Move Together – Trabajo en equipo - Colaboradores']= df_20_21[["Actively collaborate - Colaboradores", "Show respect - Colaboradores"]].mean(axis=1)
df_20_21['Speak Up – Hablo abiertamente - Colaboradores']= df_20_21[["Truly listen - Colaboradores", "Talk straight - Colaboradores"]].mean(axis=1)

df_20_21

df_20_21.columns

df_20_21=df_20_21.drop(columns=['Show respect - Global',
       'Truly listen - Global', 'Talk straight - Global',
       'Keep promises - Global', 'Actively collaborate - Global',
       'Bring passion - Global',
       'Show respect - Autovaloracion',
       'Truly listen - Autovaloracion', 'Talk straight - Autovaloracion',
       'Keep promises - Autovaloracion',
       'Actively collaborate - Autovaloracion',
       'Bring passion - Autovaloracion',
        'Show respect - Manager',
       'Truly listen - Manager', 'Talk straight - Manager',
       'Keep promises - Manager', 'Actively collaborate - Manager',
       'Bring passion - Manager',
        'Show respect - Colaboradores',
       'Truly listen - Colaboradores', 'Talk straight - Colaboradores',
       'Keep promises - Colaboradores', 'Actively collaborate - Colaboradores',
       'Bring passion - Colaboradores'
       ])

df_20_21.info()

df_2022.columns

df_2022.describe

orden_columnas=['ID', 'Gender', 'Country of Origin', 'Age', 'Tenure', 'Job Family',
       'Position Level 1', 'Position Level 2', 'Position Level 3',
       'Position Level 4', 'Position Level 5', 'Position Level 6',
       'Position Level 7', 'Position Level 8', 'Management Level',
       'Corporate Segment', 'Negocio/ No Negocio', 'mar_status', 'n_children',
       'field_study', 'spain_of_control', 'pct_women', 'pct_below40',
       'pct_above60', 'avg_age_sub', 'avg_ten_sub', 'pct_corp_seg', 'pct_STEM',
       'pct_mngt_lvl', 'what_performance_rating_h', 'what_performance_label_h',
       'what_performance_rating_f', 'what_performance_label_f',
       'how_performance_rating', 'how_performance_label',
       'risk_performance_rating', 'risk_performance_label',
       'overall_manager_rating', 'overall_manager_label',
       'emp_what_perf_rating', 'emp_what_perf_label', 'emp_how_perf_rating',
       'emp_how_perf_label', 'emp_rsk_perf_rating', 'emp_rsk_perf_label',
       'overall_employee_rating', 'overall_employee_label', 'year_performance',
       'Valoracion 360 Global',
       'Think Customer – Pienso en el cliente - Global',
       'Embrace Change – Impulso el cambio - Global',
       'Act Now – Actúo con rapidez - Global',
       'Move Together – Trabajo en equipo - Global',
       'Speak Up – Hablo abiertamente - Global',
       'Valoracion 360 Autovaloracion',
       'Think Customer – Pienso en el cliente - Autovaloracion',
       'Embrace Change – Impulso el cambio - Autovaloracion',
       'Act Now – Actúo con rapidez - Autovaloracion',
       'Move Together – Trabajo en equipo - Autovaloracion',
       'Speak Up – Hablo abiertamente - Autovaloracion',
       'Valoracion 360 Manager',
       'Think Customer – Pienso en el cliente - Manager',
       'Embrace Change – Impulso el cambio - Manager',
       'Act Now – Actúo con rapidez - Manager',
       'Move Together – Trabajo en equipo - Manager',
       'Speak Up – Hablo abiertamente - Manager',
       'Valoracion 360 Colaboradores',
       'Think Customer – Pienso en el cliente - Colaboradores',
       'Embrace Change – Impulso el cambio - Colaboradores',
       'Act Now – Actúo con rapidez - Colaboradores',
       'Move Together – Trabajo en equipo - Colaboradores',
       'Speak Up – Hablo abiertamente - Colaboradores']

df_20_21=df_20_21[orden_columnas]

df_20_21.head(150)

df_completo = pd.concat([df_20_21, df_2022])

# Reiniciar el índice con una nueva secuencia numérica
df_completo.reset_index(drop=True, inplace=True)

df_completo.info()

df_completo.shape

df_completo.describe()

#saco % de la columna Job Family (Javier)
job_family_counts = df_completo['Job Family'].value_counts()
job_family_percentages = (job_family_counts / len(df_completo)) * 100
print(job_family_percentages)

# Obtener los valores únicos de la columna 'year_performance' (Javier)
year_performance_values = df_completo['year_performance'].unique()
print(year_performance_values)

# Contar el número de filas por cada valor de 'year_performance' (Javier)
count_by_year_performance = df_completo['year_performance'].value_counts()

print(count_by_year_performance)

# Contar los valores nulos en 'Valoracion 360 Global' y agrupar por 'year_performance' (Javier)
null_counts_by_year = df_completo['Valoracion 360 Global'].isnull().groupby(df_completo['year_performance']).sum()

print(null_counts_by_year)

# Contar los valores nulos en 'Valoracion 360 Manager' y agrupar por 'year_performance' (Javier)
null_counts_by_year = df_completo['Valoracion 360 Manager'].isnull().groupby(df_completo['year_performance']).sum()

print(null_counts_by_year)

# Contar los valores nulos en 'Negocio / No Negocio' y agrupar por 'year_performance' (Javier) LOS PENDIENTES LOS COMPLETAMOS NOSOTROS
null_counts_by_year = df_completo['Negocio/ No Negocio'].isnull().groupby(df_completo['year_performance']).sum()

print(null_counts_by_year)

# Calcular el conteo y porcentaje de valores en 'Negocio/ No Negocio' agrupados por 'year_performance'
grouped_counts = df_completo.groupby('year_performance')['Negocio/ No Negocio'].value_counts()
grouped_percentages = grouped_counts.groupby(level=0).apply(lambda x: (x / x.sum()) * 100)

print(grouped_counts)
print(grouped_percentages)

# Contar los valores nulos en 'field_study' y agrupar por 'year_performance' (Javier)
null_counts_by_year = df_completo['field_study'].isnull().groupby(df_completo['year_performance']).sum()

print(null_counts_by_year)

# Contar filas con todos los campos completos (Javier)
complete_rows_count = df_completo.dropna().shape[0]

print("Número de filas con todos los campos completos:", complete_rows_count)

# Contar el número de campos incompletos por fila (Javier)
incomplete_fields_count = df_completo.isnull().sum(axis=1)

# Agrupar las filas por el número de campos incompletos y contar cuántas filas en cada grupo
grouped_counts = incomplete_fields_count.groupby(pd.cut(incomplete_fields_count, bins=[0, 5, 10, 15, 20, float('inf')], right=False)).count()

print(grouped_counts)

# Contar el número de campos incompletos por fila (Javier)
incomplete_fields_count = df_completo.isnull().sum(axis=1)

# Crear una nueva columna 'Incomplete Fields Count'
df_completo['Incomplete Fields Count'] = incomplete_fields_count

# Agrupar por 'year_performance' y 'Incomplete Fields Count', y contar cuántas filas en cada grupo
grouped_counts = df_completo.groupby(['year_performance', pd.cut(df_completo['Incomplete Fields Count'], bins=[0, 5, 10, 15, 20, float('inf')], right=False)])['Incomplete Fields Count'].count()

# Imprimir los resultados
print(grouped_counts)

df_completo.shape

# Filtrar el dataframe y contar campos vacíos por columna por el valor "2022" en la columna "year_performance" (Javier)
filtered_df = df_completo[df_completo['year_performance'] == 2022]

empty_fields_count = filtered_df.isnull().sum()

for column, count in empty_fields_count.items():
    print(f"Columna: {column}, Campos vacíos: {count}")

# Añadir una columna al df que sume cuantas "Position Level" tiene cada ID, la llamamos num_position_levels (Javier)
position_level_columns = ['Position Level 1', 'Position Level 2', 'Position Level 3',
                          'Position Level 4', 'Position Level 5', 'Position Level 6',
                          'Position Level 7', 'Position Level 8']


df_completo['num_position_levels'] = df_completo[position_level_columns].notnull().sum(axis=1)

print(df_completo['num_position_levels'])

df_completo.shape

df_completo

df_completo_01 = df_completo.copy()
df_completo_01['n_children'] = df_completo_01['n_children'].fillna(0)

df_completo_01

df_completo_01['Job Family'] = df_completo_01['Job Family'].str.replace('(NEW)', '')
unique_job_families = df_completo_01['Job Family'].unique()
print("Campos únicos en la columna 'Job Family':")
print(unique_job_families)

df_completo_01['Job Family'] = df_completo_01['Job Family'].str.replace(r'\(\)', '')
unique_job_family_after_remove = df_completo_01['Job Family'].nunique()
print("Cantidad de campos únicos en 'Job Family' después de eliminar '()':", unique_job_family_after_remove)

num_job_family_with_empty = df_completo_01['Job Family'].str.contains(r'\(\)').sum()
print("Cantidad de campos en 'Job Family' que incluyen '()':", num_job_family_with_empty)

num_empty_overall_manager_rating = df_completo_01['overall_manager_rating'].isna().sum()
num_empty_overall_manager_label = df_completo_01['overall_manager_label'].isna().sum()
print("Cantidad de campos vacíos en 'overall_manager_rating':", num_empty_overall_manager_rating)
print("Cantidad de campos vacíos en 'overall_manager_label':", num_empty_overall_manager_label)

filtered_df = df_completo_01[df_completo_01['overall_manager_label'].notnull() & df_completo_01['overall_manager_rating'].isnull()]
values_only_overall_manager_label = filtered_df['overall_manager_label']
print("Valores en 'overall_manager_label' que no tienen valor en 'overall_manager_rating':")
print(values_only_overall_manager_label)

#Filtrar las entradas con "ID" igual a "AA001" para comprobar que el Job Family es igual en los tres años
filtro = df_completo_01["ID"] == "AA001"
entradas_con_id_concreto = df_completo_01[filtro]
print(entradas_con_id_concreto)

#Definir la función para obtener el grupo de "Job Family"
def get_job_family_group(job_family):
    if job_family in ['Distribution Management', 'Customer S&S: F2F', 'Customer S&S: Remote', 'Customer S&S: Specialized products', 'Commercial & Business Banker', 'Banker', 'Sales', 'Transaction Banking', 'Debt Finance', 'M&A', 'Investment & Asset Management']:
        return "Customer Facing"
    elif job_family in ['Research and Business Intelligence', 'Product & Service Value Proposition Management', 'Business Development & Partnerships', 'Trading', 'Middle Office']:
        return "Non-customer Facing"
    elif job_family in ['Audit', 'Compliance', 'Recovery & Collections', 'EWRM', 'Credit Risk', 'Market & Structural Risk', 'Non-financial Risk']:
        return "Internal Control"
    elif job_family in ['Accounting', 'Analysis & Control', 'Financial Management', 'Capital']:
        return "Management Control"
    elif job_family in ['Software Engineering', 'Systems Infrastructure & Communication Platforms']:
        return "IT Delivery"
    elif job_family in ['Product & IT Project Management']:
        return "Product & IT Project Management"
    elif job_family in ['Solution Application, Infrastructure & Data Architecture', 'Technology Risk & Cybersecurity']:
        return "IT Enterprise"
    elif job_family in ['Service & Delivery Management', 'End User Technologies']:
        return "Service Support"
    elif job_family in ['Data Analytics & Models', 'Data Management & Governance']:
        return "Data"
    elif job_family in ['Admin & Support', 'Properties & Gral. Services', 'Procurement & Third Party Cost Mgmt.']:
        return "General Services"
    elif job_family in ['HR Specialist', 'HR Management']:
        return "Human Resources"
    elif job_family in ['Operations']:
        return "Operations"
    elif job_family in ['Investor Relations', 'Supervisory & Public Stakeholder Management', 'Communication', 'Marketing']:
        return "Skateholder Management & Marketing"
    elif job_family in ['Tax', 'Legal', 'Governance']:
        return "Counsel & Governance"
    elif job_family in ['Top Management', 'Strategy & Corporate Development', 'Project', 'Early Careers']:
        return "Other Staff & Support"
    else:
        return None

#Agregar una nueva columna "Job Family Group" al DataFrame
df_completo_01["Job Family Group"] = df_completo_01["Job Family"].apply(get_job_family_group)

"""La función revisa cuál es el valor de "Job Family Group" y lo incluye en una columna nueva que indica el "Job Family Category" correspondiente"""

#Definir la función para obtener "Job Family Category"
def get_job_family_category(job_family_group):
    if job_family_group in ['Customer Facing', 'Non-customer Facing']:
        return "Business"
    elif job_family_group in ['Internal Control', 'Management Control']:
        return "Control & Oversight"
    elif job_family_group in ['T Delivery', 'Product & IT Project Management', 'IT Enterprise', 'Service Support', 'Data', 'General Services', 'Human Resources', 'Operations', 'Skateholder Management & Marketing', 'Counsel & Governance', 'Other Staff & Support']:
        return "Staff & Support"
    else:
        return None

#Agregar una nueva columna "Job Family Group" al DataFrame
df_completo_01["Job Family Category"] = df_completo_01["Job Family Group"].apply(get_job_family_category)

df_completo_01.shape

"""##Convertimos en categórica la variable "Gender"
"""

#Codificación one-hot para 'Gender'
df_completo_01_encoded = pd.get_dummies(df_completo_01, columns=["Gender"],prefix="")

df_completo_01_encoded.shape

df_completo_01_encoded.head(3)

#Codificación one-hot para 'Job Family Group'
df_completo_01_ohe = pd.get_dummies(df_completo_01_encoded, columns=["Job Family Group"], prefix="JFG")

df_completo_01_ohe.shape

# Codificación one-hot para 'Job Family Category'
df_completo_01_ohe = pd.get_dummies(df_completo_01_ohe, columns=["Job Family Category"], prefix="JFC")

df_completo_01_ohe.shape

df_completo_01_ohe.head(3)

df_completo_01_et_num=df_completo_01.copy()

#Etiquetado numérico para 'Job Family Group'
df_completo_01_et_num["JFG_numerical"] = pd.factorize(df_completo_01_encoded["Job Family Group"])[0]

df_completo_01_et_num.shape

# Etiquetado numérico para 'Job Family Category'
df_completo_01_et_num["JFC_numerical"] = pd.factorize(df_completo_01_et_num["Job Family Category"])[0]

df_completo_01_et_num.shape

df_completo_01_et_num.head(3)

columns_to_normalize=['n_children','spain_of_control','pct_women','pct_below40','pct_above60','avg_age_sub','avg_ten_sub','pct_corp_seg','pct_STEM',
         'pct_mngt_lvl','what_performance_rating_h','what_performance_rating_f','how_performance_rating',
         'risk_performance_rating','overall_manager_rating','emp_what_perf_rating','emp_how_perf_rating','emp_rsk_perf_rating','overall_employee_rating','Valoracion 360 Global',
         'Think Customer – Pienso en el cliente - Global','Embrace Change – Impulso el cambio - Global','Act Now – Actúo con rapidez - Global','Move Together – Trabajo en equipo - Global',
         'Speak Up – Hablo abiertamente - Global','Valoracion 360 Autovaloracion','Think Customer – Pienso en el cliente - Autovaloracion','Embrace Change – Impulso el cambio - Autovaloracion',
         'Act Now – Actúo con rapidez - Autovaloracion','Move Together – Trabajo en equipo - Autovaloracion','Speak Up – Hablo abiertamente - Autovaloracion','Valoracion 360 Manager',
         'Think Customer – Pienso en el cliente - Manager','Embrace Change – Impulso el cambio - Manager','Act Now – Actúo con rapidez - Manager','Move Together – Trabajo en equipo - Manager',
         'Speak Up – Hablo abiertamente - Manager','Valoracion 360 Colaboradores','Think Customer – Pienso en el cliente - Colaboradores','Embrace Change – Impulso el cambio - Colaboradores',
         'Act Now – Actúo con rapidez - Colaboradores','Move Together – Trabajo en equipo - Colaboradores','Speak Up – Hablo abiertamente - Colaboradores']

data_to_normalize = df_completo_01_ohe[columns_to_normalize]

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaled_df = scaler.fit_transform(data_to_normalize)

scaled_df.shape

print(columns_to_normalize)

data_to_normalize.shape

df_completo_01_ohe.shape

df_completo_01_ohe_scaled = pd.DataFrame(scaled_df, columns=columns_to_normalize)

df_completo_01_ohe.head(3)

df_completo_01_ohe_scaled.head(10)

"""**Random forest de regresión**"""

df_completo_01_ohe_scaled. info

df_completo_01_ohe_scaled = df_completo_01_ohe_scaled.fillna(0)

# Importa las bibliotecas necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

X = df_90porciento.drop('Valoracion 360 Global', axis=1)
y = df_90porciento['Valoracion 360 Global']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crea el modelo de Random Forest de regresión
rf_regressor = RandomForestRegressor(n_estimators=50,max_depth=10,random_state=42)

# Entrena el modelo en los datos de entrenamiento
rf_regressor.fit(X_train, y_train)

# Realiza predicciones en el conjunto de prueba
y_pred = rf_regressor.predict(X_test)

# Evalúa el rendimiento del modelo (por ejemplo, usando el error cuadrático medio)
mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE): {mse}")
print(f'R-squared (R^2): {r2}')

# También puedes analizar la importancia de las características si lo deseas
feature_importances = rf_regressor.feature_importances_
print("Importancia de las características:")
for feature, importance in zip(X.columns, feature_importances):
    print(f"{feature}: {importance}")

total_filas = len(df_completo_01_ohe_scaled)
filas_10porciento = int(6616 * 0.10)
filas_90porciento = total_filas - filas_10porciento
df_10porciento = df_completo_01_ohe_scaled.sample(n=filas_10porciento, random_state=42)
df_90porciento = df_completo_01_ohe_scaled.drop(df_10porciento.index)

r2 = r2_score(y_test, y_pred)
print(f'R-squared: {r2}')

from sklearn.model_selection import cross_val_score

X = df_10porciento.drop('Valoracion 360 Global', axis=1)
y = df_10porciento['Valoracion 360 Global']

rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

#Utilizamos una cv de 5#
scores = cross_val_score(rf_regressor, X, y, cv=5, scoring='neg_mean_squared_error')

# Los resultados de cross_val_score son negativos, así que los convertiremos en positivos#
rmse_scores = np.sqrt(-scores)

# Calculamos el promedio y la desviación estándar del RMSE#
mean_rmse = rmse_scores.mean()
std_rmse = rmse_scores.std()

print(f'RMSE promedio: {mean_rmse}')
print(f'Desviación estándar del RMSE: {std_rmse}')

"""Serializamos ahora nuestro modelo para posteriomente poder productivizarlo. Para ello utilizaremos joblib:"""

import pickle
import joblib

# Save the model to a file
model_filename = "modelo_rfregression.grupoSantander.pkl"
joblib.dump(rf_regressor, model_filename)

from google.colab import files
files.download(model_filename)

"""**PRODUCTIVIZACIÓN DEL MODELO**
Inferimos que el modelo va a ser utilizado de forma manual, por lo que la herramienta elegida es Streamlit.

"""

import streamlit as st
import joblib

model = RandomForestRegressor(n_estimators=50)
X = df_10porciento.drop('Valoracion 360 Global', axis=1)
y = df_10porciento['Valoracion 360 Global']
model.fit(X, y)

##Importamos nuestro modelo##
model = joblib.load('modelo_rfregression.grupoSantander.pkl')

# Set the title and subtitle
st.title("Forecast of candidates for Manager positions")
st.subheader("Select the value in the different options to obtain an assessment of the candidate")

# Create input fields for each feature
feature1 = st.slider("Think Customer - Pienso en el cliente - Global", 1.00, 2.00, 3.00, 4.00)
feature2 = st.slider("Embrace Change - Impulso el cambio - Global", 1.00, 2.00, 3.00, 4.00)
feature3 = st.slider("Act Now - Actúo con rapidez - Global", 1.00, 2.00, 3.00, 4.00)
feature4 = st.slider("Move together - Trabajo en equipo - Global", 1.00, 2.00, 3.00, 4.00)
feature5 = st.slider("Speak up - Hablo abiertamente - Global", 1.00, 2.00, 3.00, 4.00)


# Create a button to perform the prediction
if st.button("Predict"):
    # Prepare the input data as a DataFrame
    input_data = pd.DataFrame({
        "Think Customer": [feature1],
        "Embrace Change": [feature2],
        "Act Now": [feature3],
        "Move together": [feature4],
        "Speak up": [feature5],
        "Spain of Control": [feature6]
    })

    # Make the prediction using the loaded model
    prediction = model.predict(input_data)[0]

    # Display the prediction
    st.write(f"Valoracion 360 Global: {prediction:.2f}")