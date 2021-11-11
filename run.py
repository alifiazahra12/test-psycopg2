from app import app

if __name__ == "__main__":
    app.secret_key = 'kode rahasia'
    app.run(debug=True)