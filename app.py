# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static
import os

# --- 0. CONFIGURACIÓN INICIAL ---
DATA_FILE_PATH = os.path.join('data', 'transacciones_igac.csv') 

# --- DICCIONARIO ADAPTADO A TUS COLUMNAS REALES ---
COL_MAPPING = {
    'FECHA_RADICA_TEXTO': 'fecha_transaccion',
    'MUNICIPIO': 'nombre_municipio',
    'DEPARTAMENTO': 'nombre_departamento',
    'TIENE_VALOR': 'sin_valor_declarado',   # TIENE_VALOR indica si existe valor → usamos inverso para anormalidad
    'TIPO_PREDIO_ZONA': 'tipo_predio_zona',
    'VALOR': 'valor_declarado',
    'LATITUD': 'latitud',                   # Si no existen en tu CSV, elimínalas
    'LONGITUD': 'longitud'
}

# --- 1. CARGA Y PROCESAMIENTO DE DATOS ---
@st.cache_data
def load_and_process_data(file_path, col_map):
    st.info("Cargando y procesando datos...")

    if not os.path.exists(file_path):
        st.error(f"ERROR: No existe el archivo '{file_path}'. Debe estar en /data/")
        st.stop()

    try:
        df = pd.read_csv(file_path, encoding='utf-8', sep=';', low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='latin1', sep=';', low_memory=False)

    if df.empty:
        st.error("El archivo está vacío.")
        st.stop()

    st.success(f"Datos cargados: {len(df)} registros.")

    # Renombrar columnas según mapeo
    df.rename(columns=col_map, inplace=True)

    # Convertir fecha
    if 'fecha_transaccion' in df.columns:
        df['fecha_transaccion'] = pd.to_datetime(df['fecha_transaccion'], errors='coerce', dayfirst=True)
        df.dropna(subset=['fecha_transaccion'], inplace=True)
    else:
        st.error("No se encontró columna de fecha.")
        st.stop()

    # Verificar que existan latitud y longitud (si tu CSV no las tiene, elimínalas del mapa)
    if 'latitud' in df.columns:
        df['latitud'] = pd.to_numeric(df['latitud'], errors='coerce')
    if 'longitud' in df.columns:
        df['longitud'] = pd.to_numeric(df['longitud'], errors='coerce')

    if 'latitud' in df.columns and 'longitud' in df.columns:
        df.dropna(subset=['latitud', 'longitud'], inplace=True)

    # Procesar valor declarado
    if 'valor_declarado' in df.columns:
        df['valor_declarado'] = pd.to_numeric(
            df['valor_declarado'].astype(str).str.replace('.', '', regex=False).str.replace(',', '.', regex=False),
            errors='coerce'
        )
    else:
        df['valor_declarado'] = 0

    # --- DETECCIÓN DE ANOMALÍAS ---
    df['es_anomalia'] = False
    df['tipo_anomalia'] = 'Normal'

    # Regla 1: Tiene valor declarado = NO o cero
    if 'sin_valor_declarado' in df.columns:
        mask_sin_valor = df['sin_valor_declarado'].astype(str).str.lower().isin(['no', '0', 'false'])
        df.loc[mask_sin_valor, 'es_anomalia'] = True
        df.loc[mask_sin_valor, 'tipo_anomalia'] = 'Sin Valor Declarado'

    mask_valor_cero = (df['valor_declarado'].isna()) | (df['valor_declarado'] == 0)
    df.loc[mask_valor_cero, 'es_anomalia'] = True
    df.loc[mask_valor_cero, 'tipo_anomalia'] = df['tipo_anomalia'].replace('Normal', 'Valor Cero/Nulo')

    # Regla 2: Valores muy altos en predios rurales
    if 'tipo_predio_zona' in df.columns:
        df_rural = df[df['tipo_predio_zona'].astype(str).str.contains('RURAL', case=False, na=False)]
        if not df_rural.empty:
            umbral = df_rural['valor_declarado'].quantile(0.95)
            mask_rural_alto = (
                df['tipo_predio_zona'].astype(str).str.contains('RURAL', case=False, na=False) &
                (df['valor_declarado'] > umbral)
            )
            df.loc[mask_rural_alto, 'es_anomalia'] = True
            df.loc[mask_rural_alto & (df['tipo_anomalia'] == 'Normal'), 'tipo_anomalia'] = 'Valor Alto en Zona Rural'

    df_anomalias = df[df['es_anomalia']].copy()

    st.success(f"Anomalías detectadas: {len(df_anomalias)} registros.")

    return df_anomalias, df

# --- 2. CONFIG STREAMLIT ---
st.set_page_config(layout="wide", page_title="IGAC Anomaly Detector MVP")
st.title("🚨 IGAC Data en Acción: Detección de Riesgos y Anomalías (MVP)")
st.markdown("Dashboard interactivo para analizar transacciones inmobiliarias con patrones de riesgo.")

# Cargar datos
df_anomalias, df_all = load_and_process_data(DATA_FILE_PATH, COL_MAPPING)

if df_anomalias.empty:
    st.warning("No se detectaron anomalías.")
    st.stop()

# --- SIDEBAR ---
st.sidebar.header("Filtros de Datos")

min_date_data = df_all['fecha_transaccion'].min().date()
max_date_data = df_all['fecha_transaccion'].max().date()

date_range_selection = st.sidebar.date_input(
    "Rango de Fechas",
    value=(min_date_data, max_date_data),
    min_value=min_date_data,
    max_value=max_date_data
)

if len(date_range_selection) == 2:
    start_date, end_date = pd.to_datetime(date_range_selection[0]), pd.to_datetime(date_range_selection[1])
    df_anomalias_filtered = df_anomalias[
        (df_anomalias['fecha_transaccion'] >= start_date) &
        (df_anomalias['fecha_transaccion'] <= end_date)
    ].copy()
else:
    df_anomalias_filtered = df_anomalias.copy()

# Filtro por tipo de anomalía
all_anomaly_types = sorted(df_anomalias_filtered['tipo_anomalia'].unique())
selected_anomaly_types = st.sidebar.multiselect(
    "Tipo de Anomalía",
    options=all_anomaly_types,
    default=all_anomaly_types
)
df_anomalias_filtered = df_anomalias_filtered[df_anomalias_filtered['tipo_anomalia'].isin(selected_anomaly_types)].copy()

# Filtro por municipio
all_municipios = sorted(df_anomalias_filtered['nombre_municipio'].dropna().unique())
selected_municipios = st.sidebar.multiselect("Municipios", options=all_municipios, default=[])

if selected_municipios:
    df_anomalias_filtered = df_anomalias_filtered[
        df_anomalias_filtered['nombre_municipio'].isin(selected_municipios)
    ].copy()

st.sidebar.markdown("---")
st.sidebar.info(f"Mostrando {len(df_anomalias_filtered)} anomalías filtradas.")

# --- 3. CONTENIDO PRINCIPAL ---
st.header("📊 Resumen de Alertas de Riesgo")

if df_anomalias_filtered.empty:
    st.warning("No hay datos con los filtros aplicados.")
else:
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Alertas", len(df_anomalias_filtered))
    col2.metric("Municipios", df_anomalias_filtered['nombre_municipio'].nunique())
    col3.metric("Valor Total Anómalo (COP)",
                f"{df_anomalias_filtered['valor_declarado'].sum():,.0f}")

    st.markdown("---")

    # Gráficos
    col_chart_1, col_chart_2 = st.columns(2)

    with col_chart_1:
        st.subheader("Distribución por Tipo de Alerta")
        fig_pie = px.pie(
            df_anomalias_filtered, names='tipo_anomalia', title='Tipos de Alerta', hole=0.3
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    with col_chart_2:
        st.subheader("Alertas por Municipio")
        anomalias_por_municipio = df_anomalias_filtered['nombre_municipio'].value_counts().reset_index()
        anomalias_por_municipio.columns = ['Municipio', 'Cantidad']
        fig_bar = px.bar(anomalias_por_municipio.head(10), x='Municipio', y='Cantidad',
                         title='Top 10 Municipios con Más Alertas')
        st.plotly_chart(fig_bar, use_container_width=True)

    # Línea de tiempo
    st.subheader("Evolución Temporal de Alertas")
    anom_time = df_anomalias_filtered.groupby(
        pd.Grouper(key='fecha_transaccion', freq='M')
    ).size().reset_index(name='count')
    fig_line = px.line(anom_time, x='fecha_transaccion', y='count',
                       title='Alertas por Mes', markers=True)
    st.plotly_chart(fig_line, use_container_width=True)

    # Mapa
    st.subheader("🗺️ Mapa de Alertas")

    if 'latitud' in df_anomalias_filtered.columns:
        center_lat = df_anomalias_filtered['latitud'].mean()
        center_lon = df_anomalias_filtered['longitud'].mean()
        m = folium.Map(location=[center_lat, center_lon], zoom_start=6)

        for _, row in df_anomalias_filtered.iterrows():
            folium.CircleMarker(
                location=[row['latitud'], row['longitud']],
                radius=5,
                color='red',
                fill=True,
                fill_color='red',
                fill_opacity=0.7,
                tooltip=f"""
                <b>Tipo:</b> {row['tipo_anomalia']}<br>
                <b>Municipio:</b> {row['nombre_municipio']}<br>
                <b>Fecha:</b> {row['fecha_transaccion'].date()}<br>
                <b>Valor:</b> {row['valor_declarado']:,.0f}
                """
            ).add_to(m)

        folium_static(m, width=900, height=500)
    else:
        st.info("El archivo no contiene LATITUD y LONGITUD. No se puede generar mapa.")

    # Tabla
    st.subheader("🔍 Detalle")
    st.dataframe(df_anomalias_filtered[['fecha_transaccion', 'nombre_departamento',
                                        'nombre_municipio', 'tipo_anomalia',
                                        'valor_declarado']])
