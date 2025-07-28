from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from document_loader import load_documents
from search import search_documents
from chatbot import generate_response

app = Flask(__name__)
app.secret_key = 'dein_geheimer_schlüssel'  # Tipp: für Produktion sicher in Umgebungsvariable!

# Login-Konfiguration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Dummy-Benutzerklasse
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Login-Seite
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == 'geheimespasswort':  # Passwort definierst du selbst
            user = User(id='1')
            login_user(user)
            return redirect(url_for('chat'))
    return render_template('login.html')

# Chat-Seite
@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    response = ''
    if request.method == 'POST':
        question = request.form['question']
        documents = load_documents()
        context = search_documents(question, documents)
        response = generate_response(question, context)
    return render_template('chat.html', response=response)

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# App starten
if __name__ == '__main__':
    app.run(debug=True)
