from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "probaho123"

@app.route("/")
def home():
    return "Hello, this is my first Flask website!"

@app.route("/about")
def about():
    return "This is the About page of Probaho Bondhu Sangathan"

@app.route("/members")
def members():
    if not session.get("logged_in"):
        return redirect("/login")
    search = request.args.get("search", "")
    conn = sqlite3.connect("somiti.db")
    cursor = conn.cursor()
    if search:
        cursor.execute("SELECT id, naam, amount, month FROM members WHERE naam LIKE ?", ("%" + search + "%",))
    else:
        cursor.execute("SELECT id, naam, amount, month FROM members")
    rows = cursor.fetchall()
    conn.close()
    member_list = []
    for row in rows:
        member_list.append({
            "id": row[0],
            "naam": row[1],
            "amount": int(row[2]),
            "month": row[3]
        })
    return render_template("members.html", members=member_list, search=search)

@app.route("/add")
def add():
    if not session.get("logged_in"):
        return redirect("/login")
    return render_template("add_member.html")

@app.route("/add", methods=["POST"])
def add_member():
    naam = request.form["naam"]
    amount = int(request.form["amount"])
    month = request.form["month"]
    conn = sqlite3.connect("somiti.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (naam, amount, month) VALUES (?, ?, ?)", (naam, amount, month))
    conn.commit()
    conn.close()
    return redirect("/members")

@app.route("/delete/<int:id>")
def delete_member(id):
    if not session.get("logged_in"):
        return redirect("/login")
    conn = sqlite3.connect("somiti.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect("/members")

@app.route("/edit/<int:id>")
def edit(id):
    if not session.get("logged_in"):
        return redirect("/login")
    conn = sqlite3.connect("somiti.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, naam, amount, month FROM members WHERE id = ?", (id,))
    row = cursor.fetchone()
    conn.close()
    member = {
        "id": row[0],
        "naam": row[1],
        "amount": int(row[2]),
        "month": row[3]
    }
    return render_template("edit_member.html", member=member)

@app.route("/edit/<int:id>", methods=["POST"])
def update_member(id):
    naam = request.form["naam"]
    amount = int(request.form["amount"])
    month = request.form["month"]
    conn = sqlite3.connect("somiti.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE members SET naam=?, amount=?, month=? WHERE id=?", (naam, amount, month, id))
    conn.commit()
    conn.close()
    return redirect("/members")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "probaho123":
            session["logged_in"] = True
            return redirect("/members")
        else:
            error = "Username অথবা Password ভুল!"
    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)