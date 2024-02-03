import pandas as pd

def main():
    
    # Cargue el dataset en un dataframe de pandas, muestre un ejemplo de cinco observaciones.
    data = pd.read_csv("./Laboratorio 1/dataset_pishing.csv")

    # Muestre la cantidad de observaciones etiquetadas en la columna status como “legit” y como “pishing”. ¿Está balanceado el dataset?

    print(data["status"].value_counts())

    


                 
if __name__ == "__main__":
    main()