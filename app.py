from flask import render_template, Flask, request

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        print("Received form data:")
        print("Name:", request.form.get('name'))
        print("Email:", request.form.get('email'))
        print("Message:", request.form.get('message'))
        return render_template("contact.html", success=True)


