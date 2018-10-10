from flask import Flask
from views.hello import Hello

app = Flask(__name__)
user_view = Hello.as_view('user_api')
app.add_url_rule('/<id>', view_func=Hello.as_view('user_api'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
