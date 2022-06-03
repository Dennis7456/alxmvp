from hirehub import create_app
from hirehub import db
from hirehub.models import User
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
    print(User.query.get(1))