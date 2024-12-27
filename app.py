from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # Proses validasi login
        if username == "admin" and password == "password":
            return "Login berhasil!"
        else:
            return "Login gagal. Periksa username atau password Anda."

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
