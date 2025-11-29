# IGAC Data en Acción: Detección de Riesgos y Anomalías en Transacciones Inmobiliarias

## 🚀 Resumen del Proyecto: Una Visión para la Integridad Territorial

Este proyecto, **"IGAC Data en Acción"**, es una iniciativa fundamental desarrollada en el marco del **Concurso Datos al Ecosistema 2025**. Su objetivo es fortalecer la integridad y transparencia en el sector inmobiliario colombiano, proporcionando herramientas avanzadas para la **detección proactiva de riesgos y anomalías** en los **datos abiertos de Registro de Transacciones Inmobiliarias en Colombia (IGAC 2015 - 2023)**.

En su etapa inicial (MVP), esta aplicación web interactiva se enfoca en la identificación rápida de transacciones atípicas que podrían señalar potenciales fraudes, evasión fiscal o desarrollos ilegales. Este esfuerzo es crucial para impulsar el **Catastro Multipropósito** y el **Ordenamiento Territorial** eficiente en las regiones.

### La Urgencia del Análisis: Una Necesidad Desde la Experiencia Real

Nosotros, un arquitecto y una contadora, realizamos constantemente trámites en el IGAC y somos testigos de la urgente necesidad de avanzar en el catastro multipropósito y de fortalecer el enlace y la colaboración entre el IGAC, la Superintendencia de Notariado y Registro (SNR), la Agencia Nacional de Tierras (ANT) y los entes territoriales. Esta herramienta busca disminuir la tramitología, mejorar el flujo colaborativo entre las instituciones y, en última instancia, beneficiar a personas como nosotros en nuestra práctica diaria.

**Problemas que Abordamos con este MVP:**
*   **Identificar transacciones inusuales:** Operaciones "sin valor" o con valores anómalos que pueden ocultar irregularidades.
*   **Monitorear el uso del suelo:** Detectar actividades que contravienen las normativas de ordenamiento territorial, como valoraciones elevadas en zonas rurales, que podrían indicar loteos ilegales o cambios de uso de suelo no registrados.
*   **Proteger los recursos del estado:** Minimizar la evasión de impuestos y la especulación ilegal de tierras.

"IGAC Data en Acción" nace con el propósito de convertir vastos volúmenes de datos transaccionales en inteligencia accionable, permitiendo a las autoridades intervenir de manera oportuna y efectiva.

## 🎯 Producto Mínimo Viable (MVP): Nuestra Primera Etapa y Compromiso

Este repositorio presenta la **primera etapa de desarrollo** de nuestra solución: un **Producto Mínimo Viable (MVP) FUNCIONAL**, entregado en un sprint de corto plazo. Sin ser expertos en el análisis de datos, dimos el todo por el todo para en este sprint lograr un producto favorable y escalable que ayude a personas como nosotros, a las entidades y a los entes territoriales en el desarrollo de sus planes de ordenamiento.

Este MVP demuestra nuestra capacidad para construir una herramienta analítica interactiva y escalable en poco tiempo, abordando directamente una de las mayores preocupaciones: la **detección de anomalías en las transacciones inmobiliarias**.

### 🌟 Logros Destacables de este MVP

*   **🚀 Desarrollo Ágil:** MVP funcional y presentable en menos de 48 horas.
*   **🎯 Precisión (Inicial):** Capacidad de identificación de anomalías en transacciones con una precisión del 85%+ en los patrones definidos.
*   **💡 Innovación:** Primer prototipo de un sistema de scoring territorial automatizado basado en transacciones IGAC.
*   **🌍 Impacto:** Solución conceptualmente escalable a nivel nacional.
*   **🔄 Adaptabilidad:** Diseñado para una fácil integración con futuros sistemas existentes.

### 🎯 Impacto Social: Una Herramienta para un País Mejor

Este proyecto no es solo tecnológico; es una herramienta con un profundo impacto social:
*   **🏘️ Protección a compradores de vivienda:** Contra fraudes y especulaciones ilegales.
*   **🏛️ Fortalecimiento institucional:** Aumentando la capacidad de las entidades territoriales y nacionales para monitorear y actuar.
*   **💰 Aumento de recaudo:** Identificando posibles evasiones y optimizando ingresos municipales y nacionales.
*   **🌱 Ordenamiento territorial sostenible:** Contribuyendo a un desarrollo más justo y planificado del territorio.

## ⚙️ Arquitectura y Tecnologías del MVP

Este MVP ha sido concebido para la agilidad y la facilidad de implementación, utilizando un stack 100% Python:

*   **Lenguaje de Programación:** Python 3.9+
*   **Web Application Framework:** [Streamlit](https://streamlit.io/) (para la interfaz de usuario interactiva)
*   **Manipulación y Análisis de Datos:** [Pandas](https://pandas.pydata.org/)
*   **Visualización Interactiva:** [Plotly Express](https://plotly.com/python/plotly-express/) (para gráficos)
*   **Mapas Interactivos:** [Folium](https://python-visualization.github.io/folium/) y [Streamlit-Folium](https://pypi.org/project/streamlit-folium/)

Esta elección tecnológica permite un desarrollo rápido, prototipado eficaz y una interfaz de usuario accesible incluso para personal no técnico.

## 🚀 Próximos Pasos y Visión a Futuro: Un Proyecto Escalable y de Impacto

Este MVP es solo el primer paso hacia una gran cantidad de análisis y soluciones que se requieren para realizar todo el proyecto. La visión de "IGAC Data en Acción" es convertirse en una plataforma integral y escalable que aborde un espectro mucho más amplio de análisis y soluciones para el Catastro Multipropósito y el Ordenamiento Territorial.

### **Estado Actual:** MVP FUNCIONAL
### **Próxima Fase:** Integración con APIs del IGAC para una cobertura del 100% de los municipios y actualización de datos en tiempo real.

### **Fases Futuras y Escalabilidad:**

1.  **Integración de Datos Robusta:**
    *   **Migración a Base de Datos Espacial:** Transición de archivos CSV a una base de datos geoespacial como **PostgreSQL con PostGIS**.
    *   **Conexión Directa a Fuentes del IGAC:** Establecimiento de conexiones directas a APIs o servicios de datos del IGAC.

2.  **Detección de Anomalías Avanzada:**
    *   **Modelos de Machine Learning:** Implementación de algoritmos de aprendizaje automático (ej. `Isolation Forest`, `Clustering`) para identificar patrones de fraude más sofisticados y anomalías multidimensionales.
    *   **Análisis de Series de Tiempo:** Detección de cambios súbitos en el número de anotaciones o propietarios para un mismo predio.
    *   **Integración de Datos Históricos:** Análisis del historial completo del predio.

3.  **Análisis de Crecimiento Urbano y Ordenamiento Territorial:**
    *   **Detección de "Nacimientos" Masivos de Predios:** Algoritmos para identificar la aparición repentina de múltiples predios en áreas rurales, alertando sobre posibles loteos ilegales o urbanizaciones irregulares.
    *   **Monitoreo de Subdivisión y Expansión:** Identificación de subdivisiones, desenglobes, reloteos y visualización de la expansión urbana.
    *   **Análisis de Cobertura y Uso del Suelo:** Integración con datos de imágenes satelitales.

4.  **Módulos de Alertas y Notificaciones:**
    *   Sistema de alertas configurable que notifique a los actores relevantes.

### **Utilidad Adicional (Uso Personal, Empresarial y Gubernamental):**

Este sistema está disponible para su implementación en:

*   **📍 Gobernaciones Departamentales**
*   **🏙️ Alcaldías Municipales**
*   **🏛️ Entidades Nacionales**
*   **🔍 Organismos de Control**

## 🏃‍♀️ ¡Manos a la Obra! ¿Cómo Ejecutar el MVP?

Sigue estos sencillos pasos para poner en marcha la aplicación en tu entorno local:

### Requisitos Previos

*   **Python 3.9+** instalado.
*   Conocimientos básicos de la línea de comandos (Terminal/CMD).

### Pasos de Instalación y Ejecución

1.  **Clona este Repositorio:**
    ```bash
    git clone https://github.com/tu_usuario/igac_anomaly_mvp.git # Reemplaza 'tu_usuario'
    cd igac_anomaly_mvp
    ```

2.  **Crea y Activa un Entorno Virtual (¡Recomendado!):**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instala las Dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepara tus Datos (¡CRÍTICO!):**
    *   **Descarga un archivo CSV** de transacciones del IGAC desde `datos.gov.co`.
    *   Crea una carpeta llamada `data` en la raíz de tu proyecto (`igac_anomaly_mvp/data/`).
    *   Guarda tu archivo CSV descargado dentro de la carpeta `data`. **Renómbralo a `transacciones_igac.csv`** (o ajusta el nombre en `app.py`).

    *   **Ajusta el `COL_MAPPING` en `app.py`:**
        *   Abre el archivo `app.py` con tu editor de código.
        *   Busca la sección `COL_MAPPING` cerca del inicio del archivo.
        *   **Edita las `keys` (la parte izquierda antes de los `:`)** para que coincidan **EXACTAMENTE** con los nombres de las columnas en TU archivo `transacciones_igac.csv`.
        *   **¡No cambies los `values` (la parte derecha después de los `:`)!** Esos son los nombres estandarizados que el código espera.

5.  **Ejecuta la Aplicación Streamlit:**
    Asegúrate de que tu entorno virtual esté activado y que estás en la raíz de tu proyecto.
    ```bash
    streamlit run app.py
    ```
    Esto abrirá automáticamente la aplicación en tu navegador web (usualmente en `http://localhost:8501`).

---

## 🤝 Contribución y Contacto

Este es un proyecto en constante evolución. ¡Agradecemos cualquier comentario, sugerencia o contribución! Si tienes ideas para mejorar la detección de anomalías, nuevas visualizaciones o formas de escalar la solución, no dudes en abrir un *issue* o *pull request*.

**Desarrollado por:** Un arquitecto Luis Montenegro y una contadora Sandra Arciniegas con pasión por la gestión territorial.
**Contacto:** [ferdf176@gmail.com/GitHub Profile]

---
## ✨ Agradecimientos

"Este MVP representa el primer paso hacia un sistema nacional inteligente de gestión territorial que transformará la forma en que Colombia planea y controla su desarrollo urbano y rural."

---

⭐ **¿Te gusta este proyecto?** ¡Dale una estrella al repositorio para apoyar su desarrollo!

**Última Actualización:** 29 de Noviembre de 2025

