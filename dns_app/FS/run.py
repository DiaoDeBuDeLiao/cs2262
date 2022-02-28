from flask import Flask, request, Response
import requests
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'FS server, please register your hostname and IP address'

@app.route('/fabonacci')
def fabonacci():
    x = request.args.get('number')
    res = Fibonacci_Recursion_tool(int(x))
    return Response("the fibo for "+str(x)+" is: "+str(res), status = 200)

@app.route('/register')
def register():
    host_name = request.args.get('hostname')
    ip_address = '0.0.0.0'
    dict = {}
    dict['name'] = host_name
    dict['address'] = ip_address
    r = requests.post('http://0.0.0.0:53533', data = dict)
    return r.text



    
def Fibonacci_Recursion_tool(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursion_tool(n - 1) + Fibonacci_Recursion_tool(n - 2)

app.run(host='0.0.0.0',
        port=9090,
        debug=True)
