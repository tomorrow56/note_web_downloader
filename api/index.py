import os
import sys

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from flask import Flask, send_from_directory
from flask_cors import CORS
from src.models.user import db
from src.routes.user import user_bp
from src.routes.download import download_bp
from src.routes.health import health_bp
from src.routes.debug import debug_bp

# Set static folder path
static_folder = os.path.join(project_root, 'src', 'static')
app = Flask(__name__, static_folder=static_folder)
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# CORS設定を追加
CORS(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(download_bp, url_prefix='/api')
app.register_blueprint(health_bp, url_prefix='/api')
app.register_blueprint(debug_bp, url_prefix='/api')

# Database configuration (disabled for Vercel)
if os.environ.get('VERCEL'):
    # Use in-memory database for Vercel
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
else:
    # Use file-based database for local development
    db_path = os.path.join(project_root, 'src', 'database', 'app.db')
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print(f"Database initialization warning: {e}")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
            return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

# Export app for Vercel
# The app is automatically used by Vercel when deployed
