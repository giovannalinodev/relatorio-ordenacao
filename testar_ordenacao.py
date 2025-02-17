import os
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

# Diretório onde estão os arquivos de teste
teste_dir = "testes"

# Diretório para salvar gráficos
output_dir = "graficos"
os.makedirs(output_dir, exist_ok=True)

# Algoritmos de ordenação e suas flags
algoritmos = {
    "Selection Sort": "-s",
    "Insertion Sort": "-i",
    "Merge Sort": "-m"
}

# Lista para armazenar os tempos de execução
resultados = []

# Iterar sobre os diretórios de casos de teste
for caso in sorted(os.listdir(teste_dir)):
    caso_path = os.path.join(teste_dir, caso)
    if os.path.isdir(caso_path):
        for arquivo in sorted(os.listdir(caso_path)):
            arquivo_path = os.path.join(caso_path, arquivo)
            tamanho = int(arquivo.split('-')[1])  # Extrair tamanho do arquivo
            
            for nome_alg, flag in algoritmos.items():
                cmd = f"./teste_ordenacao {flag} < {arquivo_path}"
                
                # Executar o comando e capturar stdout + stderr
                processo = subprocess.run(cmd, shell=True, capture_output=True, text=True)

                # Combina stdout e stderr
                saida_completa = processo.stdout + "\n" + processo.stderr
                
                # Busca a linha que contém "Tempo de ordenação"
                tempo_linha = None
                for linha in saida_completa.split("\n"):
                    if "Tempo de ordenação" in linha:
                        tempo_linha = linha
                        break

                # Se encontrou a linha com tempo, extrai o número correto
                if tempo_linha:
                    tempo_exec = float(tempo_linha.split()[-2])  # Captura o valor correto
                    resultados.append({
                        "Caso": caso,
                        "Tamanho": tamanho,
                        "Algoritmo": nome_alg,
                        "Tempo": tempo_exec
                    })
                else:
                    print(f"⚠ Erro: tempo não encontrado para {nome_alg} no arquivo {arquivo}")

# Criar DataFrame com os tempos
df = pd.DataFrame(resultados)

# Gerar gráficos para cada caso de teste
for caso in df["Caso"].unique():
    df_caso = df[df["Caso"] == caso]
    plt.figure(figsize=(10, 6))
    
    for algoritmo in df["Algoritmo"].unique():
        df_alg = df_caso[df_caso["Algoritmo"] == algoritmo]
        plt.plot(df_alg["Tamanho"], df_alg["Tempo"], marker='o', label=algoritmo)
    
    plt.xlabel("Tamanho do Array")
    plt.ylabel("Tempo de Execução (s)")
    plt.title(f"Desempenho dos Algoritmos - {caso}")
    plt.legend()
    plt.grid()
    
    # Salvar gráfico no diretório de saída
    plt.savefig(os.path.join(output_dir, f"grafico_{caso}.png"))
    plt.close()

print(f"Gráficos salvos no diretório: {output_dir}")
