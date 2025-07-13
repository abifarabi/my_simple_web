from flask import Flask, render_template, request

app = Flask(__name__)


template = """
            <style>
      body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        font-family: Arial, sans-serif;
        background: #fff;
      }
      .centered-nav {
        font-size: 2rem;
        font-weight: bold;
      }
      .centered-nav a {
        color: purple;
        margin: 0 1rem;
        text-decoration: underline;
      }
    </style>
    <div class="centered-nav">
      <a href="/get">Form GET</a> | <a href="/post">Form POST</a>
    </div>
"""
@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/intro')
def index():
    # return '<h3><a href="/get">Form GET</a> | <a href="/post">Form POST</a></h3>'
    return template


# GET TERM
@app.route('/get')
def form_get():
    # Ambil query string 
    nama = request.args.get('nama')
    return render_template('form_get.html', nama=nama)

# POST TERM
@app.route('/post', methods=['GET', 'POST'])
def form_post():
    pesan = None
    if request.method == 'POST':
        nama = request.form.get('nama')
        pesan = f'Halo, {nama}! Data dikirim via POST.'
    return render_template('form_post.html', pesan=pesan)

@app.route('/apagitu')
def apagitu():
    # Ambil query string 
    return render_template('/apagitu/file.html')

@app.route('/contoh_penerapan_css')
def contoh_penerapan_css():
    return render_template('/apagitu/css_implementation.html')

if __name__ == '__main__':
    app.run(debug=True)