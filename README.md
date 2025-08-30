# 🎬 MoviesPy

MoviesPy é uma aplicação web simples e prática, desenvolvida em **Python** com **Flask**, para gerenciar sua lista de filmes. O sistema usa arquivos **CSV exportados do Letterboxd** como base de dados, ajudando a organizar o que você já assistiu e o que ainda quer ver.

## ✨ Funcionalidades

- **Importação de Dados:** Utilize arquivos CSV exportados diretamente do Letterboxd.
- **Organização Inteligente:** Separa automaticamente os filmes em duas listas:
  - `list_movies.csv` (filmes não assistidos)
  - `watched.csv` (filmes assistidos)
- **Sugestões Aleatórias:** Receba sugestões de filmes aleatórios para assistir.
- **Marcação Automática:** Ao marcar um filme como assistido na interface, ele é movido automaticamente para a lista `watched.csv`.
- **Filtragem:** Filtre a exibição para ver apenas filmes assistidos ou não assistidos.
- **Interface Intuitiva:** Uma interface web simples e direta, construída com Flask, HTML e CSS.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask**
- **CSV (Letterboxd export)**
- **HTML + CSS**

---

## 📂 Estrutura do Projeto
``` MoviesPy/
├── data/
│   ├── list_movies.csv   # Filmes não assistidos
│   └── watched.csv       # Filmes assistidos
│
├── static/               # Arquivos CSS, imagens e ícones
├── templates/            # Páginas HTML
├── app.py                # Código principal da aplicação Flask
├── requirements.txt
└── README.md
``` 
---

## ▶️ Como Executar

Siga os passos abaixo para rodar a aplicação localmente:

1.  **Exporte sua lista do Letterboxd** em formato CSV e salve-a na pasta `data/`. Renomeie o arquivo para `list_movies.csv`.

2.  **Clone o repositório:**
    ```bash
    git clone https://github.com/santrenan/MoviesPy.git
    cd MoviesPy
    ```

3.  **Crie e ative um ambiente virtual e instale as dependências:**
    ```bash
    # Para Windows
    python -m venv venv
    venv\Scripts\activate
    pip install -r .\requirements.txt

    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

5.  **Acesse no navegador:**
    Abra seu navegador e vá para o endereço `http://127.0.0.1:5001`.
