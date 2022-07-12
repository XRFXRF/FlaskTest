from flask import Flask,render_template
app = Flask(__name__)

@app.route('/',methods=['GET',"POST","PUT"])
def index1():
    return render_template('index.html')

@app.route('/orders/<int:order>')
def get_order_id(order):
    return 'order_id {i}'.format(i=order)

if __name__ == '__main__':
    app.run()
