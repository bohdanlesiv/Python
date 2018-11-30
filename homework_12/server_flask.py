from csv_utils import CSV_UTIlS
from csv_utils import ExceptionProductExists
from flask import jsonify
from flask import Flask,request
app = Flask(__name__)

csv_proces = CSV_UTIlS('data.csv')

@app.route('/list', methods=['GET'])
def get_product():
    filter = request.args.get('name')
    if filter is None:
       products = csv_proces.get_full_list()
    else:
       products = csv_proces.get_product(filter)

    return  jsonify(products)

@app.route('/add',methods= ['POST'])
def add():
    product_name = request.form['product_name']
    amount = request.form['amount']
    message =''
    code = -1

    try:
        csv_proces.add_product(product_name,amount)
        message ='OK'
        code = 200
    except ExceptionProductExists:
        message ='Product already exists'
        code =400
    except :
        message ='Internal eroor'
        code =400

    return message,code



if __name__ == "__main__":
    app.run(debug =True)