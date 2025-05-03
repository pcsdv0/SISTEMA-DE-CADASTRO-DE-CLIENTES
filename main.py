from flask import Flask, render_template, request, redirect, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Função de conexão ao banco
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastro_clientes"
    )

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adicionar', methods=['POST'])
def adicionar():
    nome_completo = request.form['nome_completo']
    cpf = request.form['cpf']
    email = request.form['email']
    telefone = request.form['telefone']
    data_nascimento = request.form['data_nascimento']
    db = conectar()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO Clientes (nome_completo, cpf, email, telefone, data_nascimento) VALUES (%s, %s, %s, %s, %s)",
            (nome_completo, cpf, email, telefone, data_nascimento)
        )
        db.commit()
        flash('Cliente adicionado com sucesso!')
    except mysql.connector.IntegrityError as e:
        db.rollback()
        flash(f'Erro ao adicionar cliente: {e.msg}')
    finally:
        cursor.close()
        db.close()
    return redirect('/')

@app.route('/lista')
def lista():
    db = conectar()
    cursor = db.cursor()
    cursor.execute("SELECT id, nome_completo, cpf, email, telefone, DATE_FORMAT(data_nascimento, '%Y-%m-%d') FROM Clientes")
    clientes = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('lista.html', clientes=clientes)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    db = conectar()
    cursor = db.cursor()
    if request.method == 'POST':
        nome_completo = request.form['nome_completo']
        cpf = request.form['cpf']
        email = request.form['email']
        telefone = request.form['telefone']
        data_nascimento = request.form['data_nascimento']
        try:
            cursor.execute(
                "UPDATE Clientes SET nome_completo = %s, cpf = %s, email = %s, telefone = %s, data_nascimento = %s WHERE id = %s",
                (nome_completo, cpf, email, telefone, data_nascimento, id)
            )
            db.commit()
            flash('Dados do cliente atualizados com sucesso!')
        except mysql.connector.IntegrityError as e:
            db.rollback()
            flash(f'Erro ao atualizar cliente: {e.msg}')
        finally:
            cursor.close()
            db.close()
        return redirect('/lista')
    else:
        cursor.execute("SELECT id, nome_completo, cpf, email, telefone, DATE_FORMAT(data_nascimento, '%Y-%m-%d') FROM Clientes WHERE id = %s", (id,))
        cliente = cursor.fetchone()
        cursor.close()
        db.close()
        return render_template('editar.html', cliente=cliente)

@app.route('/excluir/<int:id>', methods=['POST'])
def excluir(id):
    db = conectar()
    cursor = db.cursor()
    cursor.execute("DELETE FROM Clientes WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    db.close()
    flash('Cliente excluído com sucesso!')
    return redirect('/lista')

if __name__ == '__main__':
    app.run(debug=True)