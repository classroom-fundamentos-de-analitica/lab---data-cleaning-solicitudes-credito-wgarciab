"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #

    df = df.dropna()

    df_str_columns = ['sexo', 'tipo_de_emprendimiento', 'idea_negocio', 'barrio', 'línea_credito']

    for column in df_str_columns:
        df[column] = df[column].str.lower()
        df[column] = df[column].str.replace('-', ' ')
        df[column] = df[column].str.replace('_', ' ')

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype('int64')

    df['fecha_de_beneficio'] = pd.to_datetime(
        df['fecha_de_beneficio'],
        infer_datetime_format=True, 
        errors='ignore',
        dayfirst=True,
    )
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].dt.strftime("%Y/%m/%d")

    df['monto_del_credito'] = df['monto_del_credito'].str.strip('$')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',', '')
    df['monto_del_credito'] = df['monto_del_credito'].astype('float64')


    subset=df.columns.values.tolist()
    subset.remove('Unnamed: 0')
    df.drop_duplicates(subset=subset, inplace=True)

    return df
