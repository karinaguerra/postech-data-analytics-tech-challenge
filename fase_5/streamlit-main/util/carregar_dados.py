import pandas as pd

def carregar_dados(file_path):
    # Carregar os dados do arquivo CSV
    df = pd.read_csv(file_path)

    return df

def main():
    # Caminho para o arquivo CSV
    file_path = "fase_5/streamlit-main/data/df_concat.csv"

    # Carregar os dados do arquivo CSV
    df = carregar_dados(file_path)

    return df

# Se o arquivo for executado diretamente, chama a função main()
if __name__ == "__main__":
    main()
