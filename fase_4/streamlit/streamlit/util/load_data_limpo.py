import pandas as pd

def load_data_limpo(file_path):
    # Carregar os dados do arquivo CSV
    df = pd.read_csv(file_path)

    return df

def main():
    # Caminho para o arquivo CSV
    file_path = "C:/Users/KarinaNascimento1/Documents/05_Pessoal/02_Fiap/FASE4/fase_4/streamlit/data/ipeadata_limpo.csv"

    # Carregar os dados do arquivo CSV
    df = load_data_limpo(file_path)

    return df

# Se o arquivo for executado diretamente, chama a função main()
if __name__ == "__main__":
    main()