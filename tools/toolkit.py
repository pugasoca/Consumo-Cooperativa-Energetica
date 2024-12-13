import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def procesar_datos(filepath):
    # Cargar el archivo
    data = pd.read_csv(filepath)
    return data

def regresion_modelos(df, columnas, variable_objetivo, modelo_tipo=3,grado_polinomio=2):
    # Definir X y y a partir de las columnas indicadas
    X = df[columnas]
    y = df[variable_objetivo]
    
    resultados = {}

    # Modelo Lineal
    if modelo_tipo in [1, 3]:
        linear_model = LinearRegression()
        linear_model.fit(X, y)
        y_pred_linear = linear_model.predict(X)
        r2_linear = r2_score(y, y_pred_linear)
        rmse_linear = mean_squared_error(y, y_pred_linear, squared=False)
        resultados['lineal'] = {
            "R²": r2_linear,
            "RMSE": rmse_linear,
            "intercepto": linear_model.intercept_,
            "coeficientes": linear_model.coef_,
            "características": columnas
            
        }
      
    # Modelo Polinómico
    if modelo_tipo in [2, 3]:
        poly_features = PolynomialFeatures(degree=grado_polinomio)
        X_poly = poly_features.fit_transform(X)
        poly_model = LinearRegression()
        poly_model.fit(X_poly, y)
        y_pred_poly = poly_model.predict(X_poly)
        
        r2_poly = r2_score(y, y_pred_poly)
        rmse_poly = mean_squared_error(y, y_pred_poly, squared=False)
        resultados['polinomico'] = {
            "R²": r2_poly,
            "RMSE": rmse_poly,
            "intercepto": poly_model.intercept_,
            "coeficientes": poly_model.coef_,
            "características": poly_features.get_feature_names_out(columnas)   
        }
    #modelo reg. múltiple
    if modelo_tipo == 4:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=88)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        r2_mult = r2_score(y_test, y_pred)
        rmse_mult = np.sqrt(mean_squared_error(y_test, y_pred))  
        resultados['multiple'] = {
            "R²": r2_mult,
            "RMSE": rmse_mult, 
            "coeficientes": model.coef_,
            "características": columnas
        }

    
    print(formatear_resultados(resultados))
    #print(y_pred_linear)
    #print(y_pred_poly)
   
    
   
    

    # Imprime la tabla modelo lienal con los números formateados
   

    

    
    #transformo los coeficientes en diccionarios para tratarlos en conclusiones_coeficientes
    #coef_lin = pd.Series(linear_model.coef_,index=X.columns).to_dict()
    #coef_pol = pd.Series(poly_model.coef_, index=poly_features.get_feature_names_out(columnas)).to_dict()
    #conclusiones_coeficientes(resultados,coef_lin,coef_pol)
    return resultados


 
def conclusiones_coeficientes(resultados, coef_linear, coef_poly):
    salida=""
    
     # Análisis de Impacto y Significancia
    salida += "\nAnálisis de Coeficientes:\n"
    for feature, coef in coef_linear.items():
        salida += f"- En el modelo lineal, un aumento en {feature} en una unidad estándar se asocia con un cambio de {coef:.5f} en AveragePrice.\n"
    
    print("\nPara el modelo polinómico, las interacciones entre variables pueden revelar relaciones más complejas:")
    for feature, coef in coef_poly.items():
        if abs(coef) > 1e-4:  # Solo mostramos coeficientes significativos
             salida += f"- {feature} tiene un coeficiente de {coef:.5f}, indicando un impacto en AveragePrice.\n"
    print(salida)

    
def formatear_resultados(resultados):
    salida = ""
    # Resultados del Modelo Lineal
    if 'lineal' in resultados:
        salida += "Modelo Lineal:\n"
        salida += f"  R²: {resultados['lineal']['R²']:.4f}\n"
        salida += f"  RMSE: {resultados['lineal']['RMSE']:.4f}\n"
        salida += f"  Intercepto: {resultados['lineal']['intercepto']:.4f}\n"
        salida += "  Coeficientes:\n"
        for col, coef in zip(resultados['lineal']['características'], resultados['lineal']['coeficientes']):
            salida += f"    {col}: {coef:.4e}\n"   
       
    # Resultados del Modelo Polinómico
    if 'polinomico' in resultados:
        salida += "\nModelo Polinómico:\n"
        salida += f"  R²: {resultados['polinomico']['R²']:.4f}\n"
        salida += f"  RMSE: {resultados['polinomico']['RMSE']:.4f}\n"
        salida += f"  Intercepto: {resultados['polinomico']['intercepto']:.4f}\n"
        salida += "  Coeficientes:\n"
        for col, coef in zip(resultados['polinomico']['características'], resultados['polinomico']['coeficientes']):
            salida += f"    {col}: {coef:.4e}\n"
            
    if 'multiple' in resultados:
        salida += "\nModelo Multiple:\n"
        salida += f"  R²: {resultados['multiple']['R²']:.4f}\n"
        salida += f"  RMSE: {resultados['multiple']['RMSE']:.4f}\n"
        salida += "  Coeficientes:\n"
        for col, coef in zip(resultados['multiple']['características'], resultados['multiple']['coeficientes']):
            salida += f"    {col}: {coef:.4e}\n"
     

    # Conclusiones Automáticas
    if 'lineal' in resultados and 'polinomico' in resultados:
        r2_lineal = resultados['lineal']['R²']
        rmse_lineal = resultados['lineal']['RMSE']
        r2_polinomico = resultados['polinomico']['R²']
        rmse_polinomico = resultados['polinomico']['RMSE']
        coef_linear = resultados['lineal']['coeficientes']
        coef_poly = resultados['polinomico']['coeficientes']
        
        salida += "\nConclusiones:\n"
        if r2_polinomico > r2_lineal and rmse_polinomico < rmse_lineal:
            salida += "  El modelo polinómico muestra un mejor ajuste a los datos, con un mayor R² y menor RMSE.\n"
            salida += "  Esto sugiere una posible relación no lineal entre las variables independientes y el precio promedio.\n"
        elif r2_lineal >= r2_polinomico and rmse_lineal <= rmse_polinomico:
            salida += "  El modelo lineal es comparable o superior al polinómico en términos de ajuste.\n"
            salida += "  Esto sugiere que la relación entre las variables y el precio promedio podría ser lineal.\n"
        else:
            salida += "  Ambos modelos tienen valores de R² y RMSE similares, por lo que ninguno destaca significativamente sobre el otro.\n"
            salida += "  Es posible que el grado del modelo polinómico sea insuficiente o que los datos no sigan una relación clara.\n"
    
    elif 'lineal' in resultados:
        salida += "\nConclusiones:\n"
        salida += "  Solo se ajustó el modelo lineal, y sus resultados sugieren una relación potencialmente lineal entre las variables y el precio promedio.\n"    
    elif 'polinomico' in resultados:
        salida += "\nConclusiones:\n"
        salida += "  Solo se ajustó el modelo polinómico. Los valores de R² y RMSE sugieren una posible relación no lineal.\n"
    return salida
