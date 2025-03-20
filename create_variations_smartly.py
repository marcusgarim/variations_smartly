# Certifique-se de instalar as dependências necessárias:
# pip install pandas openpyxl

import pandas as pd
import os
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

def get_inputs(prompt):
    inputs = []
    count = 1
    while True:
        user_input = input(f"{prompt} {count} ou 0: ")
        if user_input == '0':
            print()
            break
        inputs.append(user_input)
        count += 1
    return inputs

def get_inputs_tk(prompt):
    inputs = []
    count = 1
    while True:
        user_input = simpledialog.askstring("Entrada de Dados", f"{prompt} {count} ou deixe vazio para terminar:")
        if not user_input:
            break
        inputs.append(user_input)
        count += 1
    return inputs

# Criando a janela principal do Tkinter
root = tk.Tk()
root.withdraw()  # Ocultar a janela principal

# Coletando dados do usuário
fundos = get_inputs_tk("Digite o seu Background")
logos = get_inputs_tk("Digite o seu Logo")
imagens = get_inputs_tk("Digite a sua Imagem")
titles = get_inputs_tk("Digite o seu Título")
copies = get_inputs_tk("Digite a sua Descrição")
ctas = get_inputs_tk("Digite o seu CTA")

# Criando a lista de variações
variacoes = []
for fundo in fundos:
    for logo in logos:
        for imagem in imagens:
            for title in titles:
                for copy in copies:
                    for cta in ctas:
                        variacoes.append([fundo, imagem, title, copy, cta, logo])

# Criando o DataFrame
df = pd.DataFrame(variacoes, columns=["Background", "Imagem", "Título", "Descrição", "CTA", "Logo"])

# Exibir as variações geradas
print(df.head())

# Salvar o DataFrame em uma planilha na pasta de Downloads do usuário atual
downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
current_time = datetime.now().strftime('%Y%m%d%H%M')
file_path = os.path.join(downloads_path, f'variacoes_feed_{current_time}.xlsx')
df.to_excel(file_path, index=False)

print()
print(f"Sua planilha salva com sucesso em: {file_path}")
