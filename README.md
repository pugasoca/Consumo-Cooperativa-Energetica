## Proyecto 3  Curso Data Scientist  UOC 2024 
https://github.com/users/pugasoca/projects/1?pane=issue&itemId=89559047

**Descripipción:** Consumo Energía Eléctricade cooperativa energética.

![comunidad](img/fig0.comunidadenergetica.png)

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
   El conjunto de datos incluye mediciones de consumo de energía de 172 edificios de una cooperativa Energetica, recopiladas cada 15 minutos mediante medidores inteligentes PLC entre el 05/05/2022 y el 02/09/2023. Consta de 46,608 filas, organizadas por fecha y hora, y presenta columnas para cada edificio, además de una columna de tiempo .  A algunos edificios les faltan entradas, que están marcadas como (NaN).
  
![loureiro_energy.csv](img/fig1.LoureiroDataset.PNG)

Columna 
Time: fecha y hora ejemplo:  2023-01-03 05:52:30  
Energy_Meter_1 ...  Energy_Meter_172: KWHora ejemplo= 0.058
- weather_aveiro_final.csv:
  Datos meteorológicos locales. Tomados de una estación cercana en Aveiro, complementan las mediciones energéticas, coincidiendo en tiempo y número de registros; fueron recopilados originalmente en intervalos de 10 minutos. Para coincidir con los intervalos de 15 minutos de los datos de consumo de energía, se remuestrearon promediando los minutos 10 y 20 para asignarlos al intervalo de 15 minutos, y los minutos 40 y 50 para el intervalo de 45 minutos, manteniendo los valores de los minutos 0 y 30.
![loureiro_energy.csv](img/fig2weather_aveiro_finalt.PNG)

Para comprender mejor la estructura de datos, a continuación se presenta una explicación detallada de cada columna:

- **“Hora”**: fecha y hora de la medición registrada.
- **“Energy_Meter_x”**: consumo de energía en intervalos de 15 minutos (kWh) del medidor con ID x.
- **“Avg_Temp”**: temperatura media del aire a 1,5 m sobre el suelo, presentada en grados Celsius (°C).
- **“Avg_Rel_Humidity”**: la humedad relativa promedio en porcentaje.
- **“Avg_Wind_Direction”**: dirección del viento, de 0 a 360°.
- **“Avg_Wind_Speed”**: velocidad del viento en m/s.
- **“Max_Inst_Wind_Speed”**: velocidad máxima instantánea del viento, también en m/s.
- **“Inst_Temp”**: temperatura instantánea del aire a 1,5 m, en grados Celsius (°C).
- **“Quantity_Precip”**: cantidad de precipitación en milímetros.
- **“Max_Inst_Precip”**: intensidad máxima de precipitación instantánea en mm/h.
- **“Total_Global_Rad”**: radiación global total, medida en KJ/m².

Como se puede observar no existen valores duplicados en ninguno de los dos Dataset
![duplicados](img/Fig4Valoresduplicados.PNG)

#### Se verifica que están todo el rango de valores de fecha . Para hacerlo contamos cuantos observaciones de fecha existen entre el minimo y el maximo y debe ser igual a la cantidad de observaciones 46608, creamos una serie de fechas basada en los parámetros que especificaste (start, end, freq). Tabién verificamos que los rangos son iguales a los rangos de las dos dataset 

![rango](img/fig5rangofechas.PNG)

 ## Identificando problemas como valores faltantes por dispositivos e interpretación de mediciones con valores cero 
 
![mapa](img/mapa_nulos_data_energy.png)

 
 ![nulos1](img/valores_nulos_porciento.png)
 
 ### Energy Meters con el porciento de valores faltantes con más del 75% de valores nulos:
 
 ['Energy_Meter_38', 'Energy_Meter_46', 'Energy_Meter_7']

 
### Energy Meters con más de 34,956/46,608 es decir más el 75 %  valores cero:

['Energy_Meter_122', 'Energy_Meter_102', 'Energy_Meter_21', 'Energy_Meter_121', 'Energy_Meter_156', 'Energy_Meter_68', 'Energy_Meter_57', 'Energy_Meter_83', 'Energy_Meter_133', 'Energy_Meter_72', 'Energy_Meter_113', 'Energy_Meter_144', 'Energy_Meter_137', 'Energy_Meter_140']

![nulosyceros](img/fig7nulosyceros.PNG)



Esta falta de datos y valores con ceros puede ser causada por muchos motivos: 

1.	**Falta de Consumo o Demanda:** Si no hay consumo de energía en el momento en que se realiza la medición, el PLC podría registrar un valor de cero. Por ejemplo, si un dispositivo o sistema que está siendo monitoreado está apagado o en reposo, el consumo de energía podría ser cero.
2.	Interrupciones o Fallos en la Comunicación: Si el PLC pierde la comunicación con el medidor de energía o con algún dispositivo asociado, es posible que registre un valor de cero debido a un fallo de comunicación o un error de lectura temporal.
3.	Error de Configuración: Un error de configuración en el PLC o en el sistema de adquisición de datos puede causar que los valores se registren como cero, si hay un problema con el mapeo de las direcciones de memoria, configuraciones incorrectas o una mala calibración del medidor de energía.
4.	**Mediciones en el Intervalo de 0**: En sistemas que toman lecturas en intervalos pequeños (como cada 15 minutos), podría ocurrir que en ciertos momentos el consumo de energía se registre como cero si no se consume energía en ese intervalo exacto.
5.	Condiciones Específicas de Medición: En algunos sistemas, el medidor de energía puede estar configurado para registrar un valor de cero durante ciertos períodos de inactividad, como cuando no se detecta flujo de energía o cuando los dispositivos monitoreados están apagados temporalmente.
6.	Reset o Inicialización del Sistema: Si el PLC o el colector de datos se reinicia o se restablece, puede haber momentos en los que los valores se inician en cero hasta que se obtengan nuevas mediciones

**Conclusión:**

De el mapa de calor de valores nulos de data_energy obsevamos varios dispositivos con gran cantidad de valores nulos, y algunos intervalos de tiempo todos los dispositivos tienen valores nulos.
Concluimos que la presencia de valores nulos y ceros en los datos es un comportamiento relativamente común en el sector de la energía en relación con la recopilacion de datos en exteriores por los motivios expuestos . 

En nuestro estudio, hay un 25% de valores nulos no debería influir de manera significativa en los resultados, pero para este estudio , y desde un ponto de vista técnico imputaremos los valores nulos 
con alguna de las tecnicas aprendidas durante el curso, con las mediciones en ceros en nuetro proyecto en partícular tomamos la decicion de darlos por buenos, recomendamos un estudio posterior imputando valores a los ceros. 

# No no obstante nos enfocaremos en el proyecto en los 10 dispositivos con mayor cantidad de datos y menos valores nulos siendo estos imputados por .... 


**Recomendación:**

Recomendamos realizar el mismo análisis exclusivamente con los PLC (Controladores Lógicos Programables) que hayan recopilado la mayor cantidad de datos. Alternativamente, se considerara la imputación de valores nulos. Esto permitiría mejorar la capacidad para entrenar modelos más precisos y confiables, reduciendo el riesgo de introducir sesgos derivados de la eliminación de datos. De esta manera, el modelo podría basarse en datos más completos y representativos, mejorando la calidad de las predicciones y análisis.



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

### Condiciones de las vivienda ( materiales aislantes,ventanas,etc)
### Condicones meterorologoicas ( Temperatura, viento, incidencia del sol, lluvias ) Están serán motivo de estudios del presente proyecto 

![nulosyceros](img/fig8tot3nulos.PNG)

 
