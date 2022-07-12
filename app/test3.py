from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
app.secret_key='qwer'

class Login(FlaskForm):
    username=StringField('USER',validators=[DataRequired()])
    password=PasswordField('Pin',validators=[DataRequired()])
    password2=PasswordField('Pin2',validators=[DataRequired(),
    EqualTo('password','Pins are NOt equal!')])
    submit=SubmitField('SUBMIT!')

@app.route('/form',methods=['GET',"POST"])
def login():
    login_form=Login()

    if request.method=='POST':

        Username=request.form.get('username')
        password=request.form.get('password')
        password2=request.form.get('password2')

        if login_form.validate_on_submit():
            print(Username,password)
            return 'Success!'
        else:
            flash('Wrong!')

    return render_template('A.html',form=login_form)

@app.route('/',methods=['GET',"POST","PUT"])
def index1():
    if request.method=='POST':
        Username=request.form.get('username')
        Pass=request.form.get('password')
        Pass2=request.form.get('password2')
        print(Username,Pass,Pass2)
        if not all([Username,Pass,Pass2]):
            flash('Not completed!')
        elif Pass2!=Pass:
            flash("Passwords don't fit!")
        else:
            return 'Success!'
    

    return render_template('A.html')


if __name__ == '__main__':
    app.run()