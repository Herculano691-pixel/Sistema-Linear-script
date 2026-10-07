import streamlit as st
import numpy as np
import pandas as pd

def gauss_elimination(A, b):
    """
    Resolve um sistema linear Ax = b utilizando Eliminação de Gauss
    com substituição retroativa.

    Retorna:
        - A matriz escalonada (forma triangular superior)
        - O vetor b transformado
        - A solução x (se existir e for única)
        - Uma mensagem de status sobre a natureza do sistema
    """
    n = len(b)
    # Trabalhamos com cópias para não alterar os dados originais do front-end
    A = A.astype(float).copy()
    b = b.astype(float).copy()

    # --- Fase 1: Escalonamento (Eliminação Progressiva) ---
    for i in range(n):
        # Pivoteamento Parcial: Encontra a linha com o maior elemento na coluna i
        # Isso melhora a estabilidade numérica e evita divisões por zero
        max_row = i + np.argmax(np.abs(A[i:, i]))
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        # Se o pivô for zero (ou muito próximo), a matriz é singular
        if abs(A[i, i]) < 1e-12:
            continue

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]

    # --- Fase 2: Análise de Solubilidade ---
    # Verifica se existem linhas de zeros na matriz A com valor não-zero em b
    for i in range(n - 1, -1, -1):
        if abs(A[i, i]) < 1e-12:
            if abs(b[i]) > 1e-12:
                return A, b, None, "Sistema Impossível (SI)"
            else:
                return A, b, None, "Sistema Possível e Indeterminado (SPI)"

    # --- Fase 3: Substituição Retroativa ---
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return A, b, x, "Sistema Possível e Determinado (SPD)"

# =============================================================================
# INTERFACE FRONT-END COM STREAMLIT
# =============================================================================

st.set_page_config(page_title="Resolutor de Sistemas Lineares", layout="wide")

st.title("📐 Resolutor de Sistemas Lineares")
st.markdown("""
Esta ferramenta resolve sistemas de equações lineares de até 10x10 utilizando o
**Método de Eliminação de Gauss**.
""")

# 1. Configuração do Tamanho do Sistema
with st.sidebar:
    st.header("Configurações")
    n = st.number_input("Tamanho do Sistema (N)", min_value=1, max_value=10, value=3, step=1)
    st.info("Insira os coeficientes da matriz A e os termos independentes do vetor b.")

# 2. Entrada de Dados Dinâmica
st.subheader("Entrada de Dados")
col_a, col_b = st.columns([3, 1])

with col_a:
    st.write("**Matriz de Coeficientes (A)**")
    # Cria uma grade de inputs para a matriz A
    # Usamos containers para organizar as linhas
    matrix_a_data = []
    for i in range(n):
        cols = st.columns(n)
        row_values = []
        for j in range(n):
            val = cols[j].number_input(f"a{i+1},{j+1}", value=0, key=f"a_{i}_{j}")
            row_values.append(val)
        matrix_a_data.append(row_values)

with col_b:
    st.write("**Vetor b**")
    vector_b_data = []
    for i in range(n):
        val = st.number_input(f"b{i+1}", value=0, key=f"b_{i}")
        vector_b_data.append(val)

A = np.array(matrix_a_data)
b = np.array(vector_b_data)

# 3. Execução do Cálculo
if st.button("Calcular Solução", type="primary"):
    # Chamada da lógica matemática
    A_esc, b_esc, sol, status = gauss_elimination(A, b)

    st.divider()
    st.subheader("Resultados")

    # Exibição do Sistema Original
    st.write("### 1. Sistema Original")
    df_orig = pd.DataFrame(A, columns=[f"x{i+1}" for i in range(n)])
    df_orig['='] = b
    st.table(df_orig)

    # Exibição do Sistema Escalonado
    st.write("### 2. Sistema após Escalonamento (Forma Triangular)")
    df_esc = pd.DataFrame(A_esc, columns=[f"x{i+1}" for i in range(n)])
    df_esc['='] = b_esc
    st.table(df_esc)

    # Exibição da Solução Final
    st.write("### 3. Conclusão")
    if status == "Sistema Possível e Determinado (SPD)":
        st.success(f"**{status}**")
        # Formata a solução para exibição amigável
        sol_dict = {f"x{i+1}": round(val, 4) for i, val in enumerate(sol)}
        st.markdown("#### Solução Final:")
        st.write(sol_dict)
    else:
        st.error(f"**{status}**")
        st.warning("Não foi possível encontrar uma solução única para este sistema.")

st.markdown("---")
st.caption("Desenvolvido por Breno, Lucas e Chrystopher | Python & Streamlit")
