from flask import Flask, render_template, request, redirect, url_for, session, flash
from model.personagem import Personagem
from model.racas import todas_racas
from model.classes import CLASSES
from model.metodos import EstiloClassico, EstiloAventureiro, EstiloHeroico
from model.atributos import Atributos

app = Flask(__name__)
app.secret_key = 'uma_chave_secreta_muito_segura'

@app.route('/')
def index():
    session.clear()
    return render_template('index.html', racas=todas_racas, classes=CLASSES)

@app.route('/personagem', methods=['POST'])
def criar_personagem():
    nome = request.form.get('nome')
    raca_idx_str = request.form.get('raca')
    classe_idx_str = request.form.get('classe')

    if not nome or not raca_idx_str or not classe_idx_str:
        return "Erro: Nome, Raça ou Classe não selecionada. Por favor, volte e escolha uma opção.", 400

    try:
        raca_idx = int(raca_idx_str)
        classe_idx = int(classe_idx_str)
    except ValueError:
        return "Erro: Valores de raça ou classe inválidos. Por favor, tente novamente.", 400

    session['nome'] = nome
    session['raca_idx'] = raca_idx
    session['classe_idx'] = classe_idx

    return redirect(url_for('escolher_metodo'))

@app.route('/metodo')
def escolher_metodo():
    if 'nome' not in session:
        return redirect(url_for('index'))
    return render_template('metodo.html')

@app.route('/distribuir_atributos', methods=['POST'])
def distribuir_atributos():
    metodo_escolhido = request.form.get('metodo')

    if metodo_escolhido == 'classico':
        metodo = EstiloClassico()
        atributos_obj = metodo.distribuir()
        session['atributos'] = {
            'forca': atributos_obj.forca,
            'destreza': atributos_obj.destreza,
            'constituicao': atributos_obj.constituicao,
            'inteligencia': atributos_obj.inteligencia,
            'sabedoria': atributos_obj.sabedoria,
            'carisma': atributos_obj.carisma,
        }
        return redirect(url_for('mostrar_ficha'))

    elif metodo_escolhido in ['aventureiro', 'heroico']:
        metodo = EstiloAventureiro() if metodo_escolhido == 'aventureiro' else EstiloHeroico()
        valores = metodo.distribuir()
        session['valores_rolados'] = valores
        return redirect(url_for('distribuir_interativo'))
    
    return redirect(url_for('index'))

@app.route('/distribuir_interativo')
def distribuir_interativo():
    valores = session.get('valores_rolados')
    if not valores:
        return redirect(url_for('escolher_metodo'))
    return render_template('distribuir_interativo.html', valores=sorted(valores, reverse=True))

@app.route('/gerar_ficha_final', methods=['POST'])
def gerar_ficha_final():
    atributos_distribuidos = {}
    campos = ['forca', 'destreza', 'constituicao', 'inteligencia', 'sabedoria', 'carisma']
    
    # Validação para garantir que todos os campos foram preenchidos
    for campo in campos:
        valor_str = request.form.get(campo, '').strip()
        if not valor_str:
            return "Erro: Por favor, distribua todos os 6 valores antes de continuar.", 400
        try:
            atributos_distribuidos[campo] = int(valor_str)
        except ValueError:
            return f"Erro: O valor para '{campo}' é inválido.", 400
    
    valores_originais = sorted(session.get('valores_rolados', []), reverse=True)
    valores_enviados = sorted(list(atributos_distribuidos.values()), reverse=True)

    if valores_originais != valores_enviados:
        return "Erro: Os valores distribuídos não correspondem aos valores rolados. Por favor, tente novamente.", 400

    session['atributos'] = atributos_distribuidos
    return redirect(url_for('mostrar_ficha'))

@app.route('/ficha')
def mostrar_ficha():
    if 'nome' not in session or 'atributos' not in session:
        return redirect(url_for('index'))

    nome = session['nome']
    raca = todas_racas[session['raca_idx'] - 1]
    classe = CLASSES[session['classe_idx'] - 1]
    atributos = Atributos(**session['atributos'])

    personagem = Personagem(nome, raca, classe, atributos_obj=atributos)
    return render_template('ficha.html', personagem=personagem, atributos=atributos)

if __name__ == '__main__':
    app.run(debug=True)