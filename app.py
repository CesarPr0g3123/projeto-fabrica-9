# Importar o Flask
from flask import Flask, jsonify

# Criar a aplicação Flask
app = Flask(__name__)

# Dados em memória - lista de livros
livros = [
    {"id": 1, "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": 2, "titulo": "1984", "autor": "George Orwell"},
    {"id": 3, "titulo": "Dom Casmurro", "autor": "Machado de Assis"},
    {"id": 4, "titulo": "Orgulho e Preconceito", "autor": "Jane Austen"},
    {"id": 5, "titulo": "A Revolução dos Bichos", "autor": "George Orwell"}
]

# Primeira rota: /livros - Lista todos os livros
@app.route('/livros', methods=['GET'])
def listar_livros():
    """
    Lista todos os livros cadastrados
    Retorna: JSON com lista de livros (id, título, autor)
    """
    return jsonify(livros)

# Segunda rota: /livros/<int:livro_id> - Busca livro específico
@app.route('/livros/<int:livro_id>', methods=['GET'])
def obter_livro(livro_id):
    """
    Obtém os dados de um livro específico
    Parâmetros: livro_id - ID do livro a ser buscado
    Retorna: JSON com dados do livro ou erro 404 se não encontrado
    """
    # Procurar o livro pelo ID
    livro_encontrado = None
    for livro in livros:
        if livro['id'] == livro_id:
            livro_encontrado = livro
            break
    
    # Se não encontrou, retorna erro 404
    if livro_encontrado is None:
        return jsonify({"erro": "Livro nao encontrado"}), 404
    
    # Se encontrou, retorna o livro
    return jsonify(livro_encontrado)

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)