from flask import Flask, render_template


app = Flask( __name__ )

@app.route('/')
def home():
    return render_template('index.html', filas = 8, columnas= 8, color= '#DAF7A6', color2='#E74C3C')

@app.route('/4')
def home4():
    return render_template('index.html', filas=4, columnas=4, color= '#AF7AC5', color2='#5DADE2 ')

@app.route('/<int:rows>/<int:columns>')
def home_personalizado(rows, columns):
    return render_template('index.html', filas = rows, columnas = columns, color = '#48C9B0', color2 = '#99A3A4 ')

@app.route('/<int:rows>/<int:columns>/<color>/<color2>')
def home_personalizado2(rows, columns, color, color2):
    return render_template('index.html', filas = rows, columnas = columns, color = color, color2 = color2)

if __name__ == "__main__":
    app.run( debug = True )