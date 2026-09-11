import tkinter as tk
from tkinter import messagebox
import sqlite3

# =========================
# BANCO DE DADOS
# =========================

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL
    )
""")

conexao.commit()


# =========================
# FUNÇÃO PARA SALVAR CLIENTE
# =========================

def salvar_cliente():
    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Validação dos campos
    if nome == "" or email == "" or telefone == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos antes de salvar."
        )
        return

    # Inserção no banco de dados
    cursor.execute("""
        INSERT INTO clientes (nome, email, telefone)
        VALUES (?, ?, ?)
    """, (nome, email, telefone))

    conexao.commit()

    messagebox.showinfo(
        "Sucesso",
        "Cliente cadastrado com sucesso!"
    )

    limpar_formulario()


# =========================
# FUNÇÃO PARA LIMPAR FORMULÁRIO
# =========================

def limpar_formulario():
    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# =========================
# INTERFACE GRÁFICA
# =========================

janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x300")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=20)

# Nome
label_nome = tk.Label(
    janela,
    text="Nome:"
)
label_nome.pack()

entrada_nome = tk.Entry(
    janela,
    width=40
)
entrada_nome.pack(pady=5)

# E-mail
label_email = tk.Label(
    janela,
    text="E-mail:"
)
label_email.pack()

entrada_email = tk.Entry(
    janela,
    width=40
)
entrada_email.pack(pady=5)

# Telefone
label_telefone = tk.Label(
    janela,
    text="Telefone:"
)
label_telefone.pack()

entrada_telefone = tk.Entry(
    janela,
    width=40
)
entrada_telefone.pack(pady=5)

# Frame dos botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=20)

# Botão Salvar
botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar Cliente",
    width=15,
    command=salvar_cliente
)
botao_salvar.grid(row=0, column=0, padx=5)

# Botão Limpar
botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    width=15,
    command=limpar_formulario
)
botao_limpar.grid(row=0, column=1, padx=5)


# =========================
# EXECUTAR PROGRAMA
# =========================

janela.mainloop()

# Fechar conexão com o banco
conexao.close()
