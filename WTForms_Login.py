from flask import Flask,render_template,request,flash
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app = Flask(__name__)
app.secret_key='qwer'

class Login(FlaskForm):
    username=StringField('USER',validators=[DataRequired()])
    PASS=PasswordField('Pin',validators=[DataRequired()])
    PASS2=PasswordField('Pin2',validators=[DataRequired(),EqualTo('PASS','Pins are NOt equal!')])
    submit=SubmitField('SUBMIT!')

@app.route('/',methods=['GET',"POST","PUT"])
def login1():
    print('OK!!!')
    login_form=Login()

    if request.method=='POST':

        Username=request.form.get('username')
        Pass=request.form.get('PASS')
        Pass2=request.form.get('PASS2')
        print('ok!')

        if login_form.validate_on_submit():
            print(Username,Pass)
            return 'Success!'
        else:
            flash('Wrong!')

    return render_template('WTForms_Login.html',F=login_form)



if __name__ == '__main__':
    app.run()