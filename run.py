from app import create_app
import os

config_name = os.getenv("FLASK_ENV") or "default"
app = create_app(config_name)

if __name__ == '__main__':
    app.run()

# Before starting server obliged to use next commands in terminal:
# flask db init
# flask db migrate
# flask db upgrade
# python run.py
