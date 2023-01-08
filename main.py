import json

from flask import Flask

app = Flask(__name__)

store=[{"name":"table","inventory":3,"price":800},
       {"name":"chair","inventory":16,"price":120},
       {"name":"couch","inventory":1,"price":1200}]
@app.route('/')
def blabla():
    return "hi!!"
@app.route('/buy/<prod>')
def buy(prod):
    for item in store:
        if item["name"]==prod:
            item["inventory"]=item["inventory"]-1

            return json.dumps(item["inventory"])
@app.route('/sale/<prod>/<is_admin>')
def sale(prod,is_admin):
   if is_admin=="true":
       for item in store:
           if item["name"] == prod:
               if item["price"]>10:
                   item["price"] = item["price"]/2
                   return json.dumps(item["price"])
   return "cant do this active,sorry..."

@app.route('/store/<prod>')
def index(prod):
    dict={"name":prod,"price":0}
    for item in store:
        if item["name"]==prod:
            dict["price"]=item["price"]
    return json.dumps(dict)
port_number=3000
if __name__ == '__main__':
    app.run(port=port_number)