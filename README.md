## Proyecto 3  Curso Data Scientist  UOC 2024 
https://github.com/users/pugasoca/projects/1?pane=issue&itemId=89559047

**Descripipción:** Consumo Energía Eléctricade cooperativa energética.

![](img/fig0.comunidadenergetica.PNG)


**Autor:** José Puga Socarrás
- linkedin: https://www.linkedin.com/in/jose-puga-socarras-89677111
- Correo : jpugas@uoc.edu
  
**Consultor Técnico Temas Energéticos:** Ingeniero Eléctrico Alejandro Sanchez Venereo
  
https://www.linkedin.com/in/alejandro-sanchez-venereo-35069833/

**Dataset Donwload:**

https://www.sciencedirect.com/science/article/pii/S2352340924003421

**Artículo de datos:**

https://data.mendeley.com/datasets/vryvyfz2tj/1

**Autores de los datos y su artículo:**

Francisco Monteiro, Rafael Oliveira, Juan Almeida, Pedro Gonçalves, Paulo Bartolomeu,Jorge Neto y Ricardo Dios 
Licencia Creative Commons: 
Este es un artículo de acceso abierto distribuido bajo los términos de la licencia Creative Commons CC-BY , que permite el uso, la distribución y la reproducción sin restricciones en cualquier medio, siempre que se cite correctamente la obra original.

**Contexto:**

Las comunidades energéticas son figuras jurídicas que permiten que los ciudadanos produzcan, consuman, almacenen, compartan y vendan energía renovable colectivamente.
Su finalidad principal es proporcionar beneficios ambientales, económicos y sociales a sus miembros y al entorno en el que desarrollan su actividad, más que una rentabilidad financiera.
El conjunto de datos contiene información sobre el consumo eléctrico y datos meteorológicos recopilados de 172 edificios residenciales pertenecientes a una cooperativa energética local. Ubicación:	Loureiro, Oliveira de Azeméis, Portugal.

**Objetivos**
- Caracterizar el perfil de consumo de energía eléctrica de los habitantes de la región y correlacionar los hábitos de consumo en función de las condiciones climáticas, como la temperatura, la luz o la humedad, 
- Ayudar a comprender los comportamientos y las tendencias de consumo. También pueden ser utilizados por los consumidores al tomar decisiones relacionadas con la compra/venta/almacenamiento de energía, teniendo en cuenta las perspectivas de consumo futuras y las condiciones meteorológicas.
- Construcción de modelos de aprendizaje, capaces de predecir el consumo futuro y modelos que pueden mejorarse al aprender el impacto causado por las condiciones ambientales relacionadas.
- Personal: Aplicar los conociemientos apendidos durante el curso.

 # Análisis de Calidad de los Datos
  
- loureiro_energy.csv:
   El conjunto de datos incluye mediciones de consumo de energía de 172 edificios de una cooperativa Energetica, recopiladas cada 15 minutos mediante medidores inteligentes entre el 05/05/2022 y el 02/09/2023. Consta de 46,608 filas, organizadas por fecha y hora, y presenta columnas para cada edificio, además de una columna de tiempo .
![loureiro_energy.csv](img/fig1.LoureiroDataset.PNG)

Columna 
Time: fecha y hora ejemplo:  2023-01-03 05:52:30  
Energy_Meter_1 ...  Energy_Meter_172: KWHora ejemplo= 0.058
- weather_aveiro_final.csv:
  Datos meteorológicos locales. Algunas columnas tienen valores faltantes (NaN). Los datos meteorológicos, tomados de una estación cercana en Aveiro, complementan las mediciones energéticas, coincidiendo en tiempo y número de registros; los datos meteorológicos fueron recopilados originalmente en intervalos de 10 minutos. Para coincidir con los intervalos de 15 minutos de los datos de consumo de energía, se remuestrearon promediando los minutos 10 y 20 para asignarlos al intervalo de 15 minutos, y los minutos 40 y 50 para el intervalo de 45 minutos, manteniendo los valores de los minutos 0 y 30.
![loureiro_energy.csv](img/fig2weather_aveiro_finalt.PNG)

Como se puede observar no existen valores duplicados en ninguno de los dos Dataset
![duplicados](img/Fig4Valoresduplicados.PNG)


# Análisis Exploratorio de Datos (EDA)

**Explicación para entender los datos sobre el consumo Energia**

## Consumo Típico Promedio en una Casa Estándar

**Hogar Promedio en  Europa:**

- **Consumo diario promedio:** 20-30 kWh (kilovatios hora).

## En 15 minutos, esto equivale a:

$$
\frac{20 \, \text{kWh}}{24 \, \text{horas}} \times  \frac{1}{4} \approx 0.208 \, \text{kWh} \, (208 \, \text{Wh})
$$

Lo que sería **200-250 Wh** cada 15 minutos en promedio.

## Hogar con Uso Intensivo de Energía (uso de aire acondicionado, calefacción, electrodomésticos grandes):

- **Consumo diario promedio:** 30-50 kWh.

### En 15 minutos:

$$
\frac{30 \, \text{kWh}}{24 \, \text{horas}} \times \frac{1}{4} \approx 0.3125 \, \text{kWh} \, (312.5 \, \text{Wh})
$$

Lo que sería **300-400 Wh** cada 15 minutos.

## Hogar Eficiente Energéticamente (uso de paneles solares, electrodomésticos eficientes, etc.):

- **Consumo diario promedio:** 10-15 kWh.

### En 15 minutos:

$$
\frac{10 \, \text{kWh}}{24 \, \text{horas}} \times  \frac{1}{4} \approx 0.104 \, \text{kWh} \, (104 \, \text{Wh})
$$

Lo que sería **100-150 Wh** cada 15 minutos.

## Factores que Afectan el Consumo:

### Uso de Electrodomésticos:

- **Refrigerador:** ~30-50 Wh cada 15 minutos.
- **Aire acondicionado:** ~300-1,000 Wh cada 15 minutos.
- **Televisión:** ~50-75 Wh cada 15 minutos.
- **Portátil:** ~10-20 Wh cada 15 minutos.

### Horarios Pico:

En las mañanas y tardes, el consumo suele ser más alto debido al uso de electrodomésticos como lavadoras, secadoras y equipos de cocina.




 
