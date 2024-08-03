from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

books = []

app.jinja_env.globals.update(enumerate=enumerate)

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        books.append({'title': title, 'author': author})
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = books[book_id]
    if request.method == 'POST':
        book['title'] = request.form['title']
        book['author'] = request.form['author']
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book, book_id=book_id)

@app.route('/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    books.pop(book_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
