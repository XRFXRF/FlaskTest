from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:X19995858@127.0.0.1/Flask_Libmanager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Author(db.Model):
    __tablename__='Authors'
    id= db.Column(db.Integer,primary_key=True)
    name=db.Column (db.String(16),unique=True)
    books=db.relationship('Book',backref='auth')

    def __repr__(self) -> str:
        return 'Author: {}'.format(self.name)
    
class Book(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=name=db.Column (db.String(16),unique=True)
    author_id=db.Column(db.Integer,db.ForeignKey('Authors.id'))
    def __repr__(self) -> str:
        return 'Book: {} {}'.format(self.name,self.author_id)
    
db.drop_all()
db.create_all()

au1=Author(name='Wang')
au2=Author(name='Hui')
au3=Author(name='Liu')
db.session.add_all([au1,au2,au3])
db.session.commit()





@app.route('/',methods=['GET',"POST","PUT"])
def index1():
    return render_template('Libmanager.html')

if __name__ == '__main__':
    app.run()
