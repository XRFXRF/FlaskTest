from flask import Flask,render_template
app = Flask(__name__)

@app.route('/',methods=['GET',"POST","PUT"])
def index1():
    url=[1,22,333]
    ss='qweee'
    return render_template('index.html',url_str=url,xx=ss)


if __name__ == '__main__':
    app.run()