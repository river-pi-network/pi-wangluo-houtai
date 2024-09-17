from app.routes import app
from app.models import db

app.config.from_object('config.Config')
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
