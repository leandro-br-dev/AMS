import os
from dotenv import load_dotenv
from app import create_app, socketio

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = create_app()

if __name__ == '__main__':
    # Obter a porta da variável de ambiente, padrão para 5002
    port = int(os.getenv('FLASK_RUN_PORT', 5002))
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
