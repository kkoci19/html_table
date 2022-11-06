from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route('/')
def index():
    users = (
        {'first_name': 'Klaus', 'last_name': 'Koci'},
        {'first_name': 'adaada', 'last_name': 'sdsds'},
        {'first_name': 'Sara', 'last_name': 'Dalipi'},
        {'first_name': 'zxcz', 'last_name': 'mmvmv'}
    )

    return render_template('index.html', user=users)


if __name__ == "__main__":
    app.run(debug=True)
