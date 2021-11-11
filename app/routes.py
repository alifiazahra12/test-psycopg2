from app import app
from flask import render_template, request, session, redirect, url_for
from app.db import db_cursor, db_connect #Import Fungsi dari file db.py

@app.route('/')
def index():
    cur = db_cursor(db_connect())   # Cursor untuk ambil database
    s = "SELECT * FROM mahasiswa"   # ya ini query
    cur.execute(s)                  # Cursor jalankanlah query s
    list_users = cur.fetchall()     # Gatau fetchall() apaan tapi penting buat ambil semua data link:https://www.psycopg.org/docs/cursor.html#cursor.fetchall
    return render_template("index.html", list_users=list_users)

@app.route('/edit')
def edit():
    return render_template("edit.html")

@app.route('/hapus')
def hapus():
    return render_template("hapus.html")


@app.route('/input', methods=['GET', 'POST'])
def input():
    conn = db_connect()         # Koneksiin ke DB nya
    cur = db_cursor(conn)       # Cursor untuk ambil database
    if request.method == 'POST':
        npm = request.form['npm']
        nama = request.form['nama']
        kelas = request.form['kelas']
        cur.execute("INSERT INTO mahasiswa (npm, nama, kelas) VALUES (%s,%s,%s);", (npm, nama, kelas)) # eksekusi query
        conn.commit()   # Kalo abis di eksekusi harus di commit biar datanya masuk
        conn.close()    # gatau penting atau ngga. Tapi ini buat nutup koneksi dari DB nya
        return redirect(url_for("index"))
    return render_template("input.html")