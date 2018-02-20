from flask import Flask, render_template, redirect, url_for, request
import password

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form['logUserName']
        user_password = request.form['logPass']
        hashed_pass = queries.get_hashed_pass(user_name)
        check_login = password.verify_password(password, hashed_pass)
        if check_login == True:
            return render_template('boards.html')
        else:
            return render_template('login.html', wrongpass=False)
    return render_template('login.html')


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        username = request.form["regUserName"]
        password = request.form["regPass"]
        isUser = queries.check_username(username)
        if isUser:
            return redirect(url_for("registration"))
        else:
            hashed_password = password.hash_password(password)
            queries.create_user(username, hashed_password)
            return redirect(url_for("login"))
    else:
        return render_template("registration.html")


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
