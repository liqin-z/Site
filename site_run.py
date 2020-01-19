from app import app
from configparser import ConfigParser
import os
import socket
import webbrowser
import time
import threading

def start_server():
    print("Server is running at " + time.ctime())
	app.run(host=config['client']['HOST'], port=config['client']['PORT'], debug=config['client']['debug'], use_reloader=config['client']['use_reloader'])

def start_client():
    print("Client is running at " + time.ctime())
	webbrowser.open("http://{0}:{1}".format(config['client']['HOST'],config['client']['PORT']))

if __name__ == "__main__":
    config = ConfigParser()
    config.read('config.ini')

    print("Site is running on local machine: " + socket.gethostname() + " at " + time.ctime())
    # addrs = socket.getaddrinfo(socket.gethostname(), None)
    # Check all users running this site

    start_server()


    