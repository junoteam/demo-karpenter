from multiprocessing import Pool
import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
APP_PORT = os.environ.get('APP_PORT')
APP_HOST = os.environ.get('APP_HOST')
DEBUG = os.environ.get('DEBUG')

app = Flask(__name__)

def make_load():
    def f(x):
        # Put any cpu (only) consuming operation here. I have given 1 below -
        while True:
            x * x

    # decide how many cpus you need to load with.
    no_of_cpu_to_be_consumed = 3

    p = Pool(processes=no_of_cpu_to_be_consumed)
    p.map(f, range(no_of_cpu_to_be_consumed))

@app.route('/', methods = ['GET'])
def george():
    return '1984'

@app.route('/start', methods = ['GET', 'POST'])
def start_load():
    make_load()
    return 'Kick my grandma in the ankle!'

@app.route('/stop', methods = ['GET', 'POST'])
def stop_load():
    return 'No Fate...'


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=DEBUG)