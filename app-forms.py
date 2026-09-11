```python
import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3


# ==========================================
# CONEXÃO COM O BANCO DE DADOS
# ==========================================

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

# Criação da tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL
)
""")

conexao.commit()


# ==========================================
# FUNÇÃO PARA SALVAR CLIENTE
# ==========================================

def salvar_cliente():

    nome = entrada_nome.get().strip()
    email = entrada_email.get().strip()
    telefone = entrada_telefone.get().strip()

    # Verifica se todos os campos foram preenchidos
    if nome == "" or email == "" or telefone == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha todos os campos antes de salvar."
        )
        return

    # Insere o cliente no banco
    cursor.execute("""
    INSERT INTO clientes (nome, email, telefone)
    VALUES (?, ?, ?)
    """, (nome, email, telefone))

    conexao.commit()

    messagebox.showinfo(
        "Sucesso",
        "Cliente cadastrado com sucesso!"
    )

    # Limpa os campos
    limpar_formulario()


# ==========================================
# FUNÇÃO PARA LIMPAR O FORMULÁRIO
# ==========================================

def limpar_formulario():

    entrada_nome.delete(0, tk.END)
    entrada_email.delete(0, tk.END)
    entrada_telefone.delete(0, tk.END)

    entrada_nome.focus()


# ==========================================
# FUNÇÃO PARA VISUALIZAR CLIENTES
# ==========================================

def visualizar_clientes():

    # Cria uma nova janela
    janela_clientes = tk.Toplevel(janela)

    janela_clientes.title("Clientes Cadastrados")
    janela_clientes.geometry("750x400")
    janela_clientes.resizable(False, False)

    # Título
    titulo = tk.Label(
        janela_clientes,
        text="Clientes Cadastrados",
        font=("Arial", 18, "bold")
    )

    titulo.pack(pady=15)

    # ======================================
    # TABELA
    # ======================================

    colunas = ("id", "nome", "email", "telefone")

    tabela = ttk.Treeview(
        janela_clientes,
        columns=colunas,
        show="headings",
        height=12
    )

    # Cabeçalhos
    tabela.heading("id", text="ID")
    tabela.heading("nome", text="Nome")
    tabela.heading("email", text="E-mail")
    tabela.heading("telefone", text="Telefone")

    # Largura das colunas
    tabela.column("id", width=50, anchor="center")
    tabela.column("nome", width=200)
    tabela.column("email", width=250)
    tabela.column("telefone", width=150)

    tabela.pack(padx=20, pady=10)

    # ======================================
    # BUSCA OS CLIENTES NO BANCO
    # ======================================

    cursor.execute("""
    SELECT id, nome, email, telefone
    FROM clientes
    ORDER BY id
    """)

    clientes = cursor.fetchall()

    # Insere os clientes na tabela
    for cliente in clientes:
        tabela.insert(
            "",
            tk.END,
            values=cliente
        )

    # Caso não exista nenhum cliente
    if len(clientes) == 0:

        messagebox.showinfo(
            "Clientes",
            "Nenhum cliente cadastrado.",
            parent=janela_clientes
        )


# ==========================================
# FUNÇÃO PARA FECHAR O PROGRAMA
# ==========================================

def fechar_programa():

    conexao.close()
    janela.destroy()


# ==========================================
# JANELA PRINCIPAL
# ==========================================

janela = tk.Tk()

janela.title("Cadastro de Clientes")
janela.geometry("450x400")
janela.resizable(False, False)


# ==========================================
# TÍTULO
# ==========================================

titulo = tk.Label(
    janela,
    text="Cadastro de Clientes",
    font=("Arial", 20, "bold")
)

titulo.pack(pady=20)


# ==========================================
# CAMPO NOME
# ==========================================

label_nome = tk.Label(
    janela,
    text="Nome:"
)

label_nome.pack()

entrada_nome = tk.Entry(
    janela,
    width=45
)

entrada_nome.pack(pady=5)


# ==========================================
# CAMPO E-MAIL
# ==========================================

label_email = tk.Label(
    janela,
    text="E-mail:"
)

label_email.pack()

entrada_email = tk.Entry(
    janela,
    width=45
)

entrada_email.pack(pady=5)


# ==========================================
# CAMPO TELEFONE
# ==========================================

label_telefone = tk.Label(
    janela,
    text="Telefone:"
)

label_telefone.pack()

entrada_telefone = tk.Entry(
    janela,
    width=45
)

entrada_telefone.pack(pady=5)


# ==========================================
# FRAME DOS BOTÕES
# ==========================================

frame_botoes = tk.Frame(janela)

frame_botoes.pack(pady=20)


# ==========================================
# BOTÃO SALVAR
# ==========================================

botao_salvar = tk.Button(
    frame_botoes,
    text="Salvar Cliente",
    width=16,
    command=salvar_cliente
)

botao_salvar.grid(
    row=0,
    column=0,
    padx=5
)


# ==========================================
# BOTÃO LIMPAR
# ==========================================

botao_limpar = tk.Button(
    frame_botoes,
    text="Limpar",
    width=16,
    command=limpar_formulario
)

botao_limpar.grid(
    row=0,
    column=1,
    padx=5
)


# ==========================================
# BOTÃO VISUALIZAR CLIENTES
# ==========================================

botao_visualizar = tk.Button(
    janela,
    text="Visualizar Clientes",
    width=35,
    command=visualizar_clientes
)

botao_visualizar.pack(pady=5)


# ==========================================
# BOTÃO SAIR
# ==========================================

botao_sair = tk.Button(
    janela,
    text="Sair",
    width=35,
    command=fechar_programa
)

botao_sair.pack(pady=5)


# ==========================================
# INICIA O PROGRAMA
# ==========================================

janela.protocol(
    "WM_DELETE_WINDOW",
    fechar_programa
)

entrada_nome.focus()

janela.mainloop()
```
