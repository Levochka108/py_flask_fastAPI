from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

# Базовый шаблон
@app.route('/')
def index():
    return render_template('index.html')

# Шаблон категории товаров
@app.route('/category/<category_name>')
def category(category_name):
    return render_template('category.html', category_name=category_name)

# Шаблон отдельного товара
@app.route('/product/<product_name>')
def product(product_name):
    return render_template('product.html', product_name=product_name)

if __name__ == '__main__':
    app.run(debug=True)