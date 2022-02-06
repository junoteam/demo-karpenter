# from multiprocessing import Pool
import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from pathos.multiprocessing import ProcessingPool as Pool
from threading import Thread

load_dotenv(find_dotenv())
APP_PORT = os.environ.get('APP_PORT')
APP_HOST = os.environ.get('APP_HOST')
DEBUG = os.environ.get('DEBUG')

app = Flask(__name__)


class Loader:

    @staticmethod
    def create_file():
        f = open("file.txt", "a")
        f.write("Now the file has more content!")
        f.close()

    @staticmethod
    def del_file():
        if os.path.exists("file.txt"):
            os.remove("file.txt")

    @staticmethod
    def make_load():
        def f(x):
            # Put any cpu (only) consuming operation here. I have given 1 below -
            while True:
                if not os.path.exists("file.txt"):
                    return
                x * x

        # decide how many cpus you need to load with.
        no_of_cpu_to_be_consumed = 3

        p = Pool(processes=no_of_cpu_to_be_consumed)
        p.map(f, range(no_of_cpu_to_be_consumed))


@app.route('/', methods=['GET'])
def george():
    return '1984'


@app.route('/start', methods=['GET'])
def start_load():
    def start_balagan():
        Loader.create_file()
        Loader.make_load()

    Thread(target = start_balagan).start()
    return 'Kick my grandma in the ankle!'


@app.route('/stop', methods=['GET'])
def stop_load():
    Loader.del_file()
    return 'No Fate...'


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=DEBUG)
