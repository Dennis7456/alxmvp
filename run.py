from distutils.log import debug
from hirehub import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)