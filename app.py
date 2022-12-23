import flask 

app = flask.Flask(__name__)

def get_latest_packages():
    return [
        {'name': 'flask', 'version': '2.2.0'},
        {'name': 'sqlalchemy', 'version': '3.4.0'},
        {'name': 'pandas', 'version': '1.5.0'},
    ]

@app.route('/')
def index():
    test_packages = get_latest_packages
    return flask.render_template('index.html', packages = test_packages)

# Rout
@app.route('/about')
# View
def about():
    return flask.render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)