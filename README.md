# 📌 Projeto: Análise de Algoritmos de Ordenação

Este projeto implementa e testa **três algoritmos de ordenação** em **C++**: 
- 🔹 **Selection Sort** (Ordenação por Seleção)
- 🔹 **Insertion Sort** (Ordenação por Inserção)
- 🔹 **Merge Sort** (Ordenação por Merge-Sort)

## 🎯 **Objetivo da Tarefa**
1. Criar uma função que verifica se um **array está ordenado**.
2. Implementar os **três algoritmos de ordenação** e medir seu desempenho.
3. Executar testes com conjuntos de dados de **10.000 a 100.000 elementos**.
4. **Gerar gráficos** comparando o tempo de execução de cada algoritmo.
5. **Analisar qual algoritmo é mais eficiente** para cada caso de teste.

---

## 📂 **Estrutura do Diretório**
```
📦 atividade-ordenacao
 ┣ 📂 testes/          # Diretório com arquivos de entrada para testes
 ┃ ┣ 📂 caso01/        # Testes com 10.000 elementos
 ┃ ┣ 📂 caso02/        # Testes com 20.000 elementos
 ┃ ┣ 📂 caso03/        # Testes com 50.000 elementos
 ┃ ┣ 📂 caso04/        # Testes com 75.000 elementos
 ┃ ┗ 📂 caso05/        # Testes com 100.000 elementos
 ┣ 📂 graficos/        # Diretório onde os gráficos são salvos
 ┣ 📜 ordenacao.cpp    # Implementação dos algoritmos de ordenação
 ┣ 📜 teste_ordenacao.cpp  # Código que executa os algoritmos e mede tempo
 ┣ 📜 testar_ordenacao.py  # Script para rodar os testes e gerar gráficos
 ┗ 📜 README.md        # Este arquivo com a documentação do projeto
```
---

## 🚀 **Passo a Passo para Executar os Testes**

### 🔧 **1️⃣ Compilar o Código C++**
Primeiro, precisamos compilar os arquivos `ordenacao.cpp` e `teste_ordenacao.cpp`:
```
g++ -Wall -o teste_ordenacao teste_ordenacao.cpp ordenacao.cpp
chmod +x teste_ordenacao
```
Isso gera um **executável** chamado `teste_ordenacao`, que será usado para ordenar os arquivos de teste.

---

### 🏃 **2️⃣ Executar os Testes de Ordenação**
Cada teste recebe um **arquivo de entrada** e executa um dos algoritmos de ordenação.

#### **Rodar apenas Selection Sort**
```
./teste_ordenacao -s < testes/caso01/exemplo-10000-1.txt > saida_selecao.txt
```
#### **Rodar apenas Insertion Sort**
```
./teste_ordenacao -i < testes/caso01/exemplo-10000-1.txt > saida_insercao.txt
```
#### **Rodar apenas Merge Sort**
```
./teste_ordenacao -m < testes/caso01/exemplo-10000-1.txt > saida_merge.txt
```
📌 Após executar os testes, os **números ordenados são salvos** nos arquivos `saida_selecao.txt`, `saida_insercao.txt` e `saida_merge.txt`.

Para verificar:
```
cat saida_selecao.txt
cat saida_insercao.txt
cat saida_merge.txt
```
Os números devem estar **ordenados em ordem não decrescente**.

---

### 🖥️ **3️⃣ Criar e Ativar o Ambiente Virtual Python**
Para rodar o script que **gera os gráficos**, primeiro criamos um ambiente virtual:
```
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate # Windows
```
Agora instalamos as bibliotecas necessárias:
```
pip install pandas matplotlib
```
---

### 📊 **4️⃣ Executar os Testes de Forma Fragmentada**

#### 🔹 **Rodar todos os algoritmos a partir do testar_ordenacao.py**
- **Comando**:
```
  python3 testar_ordenacao.py 
```

### 📈 **5️⃣ Gerar os Gráficos**
Os gráficos são **automaticamente salvos no diretório `graficos/`**. Para verificar:
```
ls graficos/
```
Para abrir um gráfico no Linux:
```
xdg-open graficos/grafico_caso01.png
```
No macOS:
```
open graficos/grafico_caso01.png
```

Cada gráfico compara os **tempos de execução dos algoritmos** para um conjunto de dados.

---

## 📊 **📌 Análise dos Resultados**
Os gráficos devem mostrar que:

✅ **Merge Sort é sempre o mais rápido** para grandes conjuntos de dados, pois sua complexidade é **O(n log n)**.  

🚨 **Selection Sort e Insertion Sort são muito mais lentos** para entradas grandes (**O(n²)**).  

---

## 📊 **Resultados e Análise**

Para cada conjunto de testes (`caso01` a `caso05`), foram gerados **gráficos comparando o tempo de execução dos três algoritmos de ordenação**. Os resultados foram analisados para verificar qual algoritmo é mais eficiente para cada caso.

### 📈 **Gráficos Gerados**
Os gráficos do tempo de execução em função do tamanho da entrada foram salvos na pasta `graficos/`. Cada gráfico exibe a performance de **Selection Sort, Insertion Sort e Merge Sort**.

- **caso01** → `graficos/grafico_caso01.png`
- **caso02** → `graficos/grafico_caso02.png`
- **caso03** → `graficos/grafico_caso03.png`
- **caso04** → `graficos/grafico_caso04.png`
- **caso05** → `graficos/grafico_caso05.png`

---

### 🏆 **Qual foi o melhor algoritmo?**
| Caso de Teste | Melhor Algoritmo | Justificativa |
|--------------|----------------|----------------|
| **Caso 01** (10.000 elementos) | **Merge Sort** | Foi o mais rápido e teve crescimento O(n log n). |
| **Caso 02** (20.000 elementos) | **Merge Sort** | Selection e Insertion Sort já apresentaram tempos significativamente maiores. |
| **Caso 03** (50.000 elementos) | **Merge Sort** | O tempo de execução de Selection Sort e Insertion Sort explodiu devido à complexidade O(n²). |
| **Caso 04** (75.000 elementos) | **Merge Sort** | Confirmação do comportamento de O(n log n), enquanto os outros métodos tornaram-se inviáveis. |
| **Caso 05** (100.000 elementos) | **Merge Sort** | O único algoritmo eficiente para esse tamanho. |

📌 **Conclusão:** O Merge Sort **é sempre o melhor algoritmo**, pois segue a complexidade O(n log n), enquanto os outros dois métodos tornam-se impraticáveis para grandes volumes de dados.

---

### **🔬 Análise de Complexidade Empírica vs. Teórica**
Os tempos de execução confirmam a teoria:

- **Merge Sort → O(n log n)** ✅   
  - O tempo cresce moderadamente, mostrando eficiência para grandes entradas.  
- **Selection Sort → O(n²)** ⚠️   
  - Cresce rapidamente, tornando-se inviável a partir de 20.000 elementos.  
- **Insertion Sort → O(n²)** ⚠️   
  - Assim como o Selection Sort, é viável apenas para pequenas entradas.

📌 **Análise final:**  
Os resultados experimentais **confirmam a análise teórica de complexidade Big-O**.

 O Merge Sort é claramente a **melhor escolha para entradas grandes**, enquanto os outros métodos são apenas didaticamente úteis para pequenas listas.

---


## 📝 **Conclusão**
✔️ Implementação dos três algoritmos de ordenação em C++.  
✔️ Execução dos testes para diferentes tamanhos de entrada.  
✔️ Criação de gráficos comparando os tempos de execução.  
✔️ Análise de quais algoritmos são mais eficiente para cada caso.  

Dessa forma, é possível concluir que o **Merge Sort é o mais eficiente para grandes volumes de dados**, enquanto o **Selection Sort e o Insertion Sort são viáveis apenas para pequenas entradas**.