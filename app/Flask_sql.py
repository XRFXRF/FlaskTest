from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:X19995858@127.0.0.1/Flask_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


db=SQLAlchemy(app)

class Role(db.Model):
    __tablename__='Roles'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)

    users=db.relationship('User',backref='role')

    def __repr__(self) -> str:
        return '<Role:{n} {i}>'.format(n=self.name,i=self.id)

class User(db.Model):
    __tablename__='Users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(16),unique=True)
    email=db.Column(db.String(32),unique=True)
    password=db.Column(db.String(32))
    role_id=db.Column(db.Integer,db.ForeignKey('Roles.id'))
    
    def __repr__(self) -> str:
        return '<Role:{n} {i} {e} {p}>'.format(n=self.name,i=self.id,e=self.email,p=self.password)

#remove all items in tables
db.drop_all()
db.create_all()


@app.route('/')
def index():
    return 'H'

if __name__=='__main__':
    
    app.run()