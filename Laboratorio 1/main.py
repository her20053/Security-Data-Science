import pandas as pd

def main():
    
    # Carga de datos
    data = pd.read_csv("./Laboratorio 1/dataset_pishing.csv")

    # Imprimir los primeros 5 registros

    print(data.head())

    # Imprimir los ultimos 5 registros

    print(data.tail())


                 
if __name__ == "__main__":
    main()