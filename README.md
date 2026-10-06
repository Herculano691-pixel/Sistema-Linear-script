# 📐 Resolvedor de Sistemas Lineares

Este projeto é uma aplicação em Python desenvolvida para a resolução de sistemas de equações lineares de até 10x10, utilizando o método de **Eliminação de Gauss com Substituição Retroativa** e **Pivoteamento Parcial**.

A aplicação possui uma interface gráfica moderna e intuitiva desenvolvida com **Streamlit**, permitindo que o usuário insira os coeficientes dinamicamente e visualize todas as etapas da resolução.

## ✨ Funcionalidades

- **Entrada Dinâmica:** Seleção do tamanho do sistema (N) de 1 a 10.
- **Interface Intuitiva:** Grid de inputs para a matriz de coeficientes (A) e o vetor de termos independentes (b).
- **Lógica Matemática Robusta:**
  - Implementação de Eliminação de Gauss.
  - Uso de Pivoteamento Parcial para maior estabilidade numérica.
  - Detecção automática do tipo de sistema:
    - ✅ **SPD (Sistema Possível e Determinado):** Exibe a solução única.
    - ⚠️ **SPI (Sistema Possível e Indeterminado):** Identifica infinitas soluções.
    - ❌ **SI (Sistema Impossível):** Identifica contradições no sistema.
- **Visualização de Resultados:** Exibe o sistema original, a matriz escalonada (triangular superior) e a solução final.

## 🚀 Como Executar Localmente

### Pré-requisitos
Certifique-se de ter o **Python 3.8 ou superior** instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Herculano691-pixel/Sistema-Linear-script.git
   cd "Sistema Linear script"
   ```

2. **Instale as dependências:**
   Abra o terminal e execute o seguinte comando para instalar as bibliotecas necessárias:
   ```bash
   pip install streamlit numpy pandas
   ```

3. **Inicie a aplicação:**
   Execute o comando do Streamlit para subir o servidor local:
   ```bash
   streamlit run solver_linear.py
   ```

4. **Acesse no navegador:**
   Após rodar o comando acima, o Streamlit abrirá automaticamente o seu navegador padrão no endereço `http://localhost:8501`.

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) - Para a interface web.
- [NumPy](https://numpy.org/) - Para processamento matemático e manipulação de matrizes.
- [Pandas](https://pandas.pydata.org/) - Para formatação de tabelas de dados.

---

