from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
 
app = Flask(__name__)
 
app.secret_key = 'password'
 
 
class LoginForm(FlaskForm):
    username = StringField("用户名:", validators=[DataRequired()])
    password = PasswordField("密码:", validators=[DataRequired()])
    password2 = PasswordField("确认密码:", validators=[DataRequired(), EqualTo("password", "密码填写输入不一致")])
    submit = SubmitField("提交")
 
 
@app.route('/form', methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
 
        if login_form.validate_on_submit():
            return "success"
        else:
            flash("参数有误")
    return render_template("WTForms_Login2.html", form=login_form)
 
 
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
 
        if not all([username, password, password2]):
            flash(u"参数不完整")
 
        elif password != password2:
            flash(u"密码错误")
        else:
            return "success"
 
    return render_template("WTForms_Login2.html")
 
 
if __name__ == '__main__':
    app.run()