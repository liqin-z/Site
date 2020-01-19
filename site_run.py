if __name__ == "__main__":
    from app import app
    from configparser import ConfigParser
    import os
    import socket
    import webbrowser
    import time
    import threading
    
    config = ConfigParser()
    config.read('config.ini')

    print("Site is running on local machine: " + socket.gethostname() + " at " + time.ctime())
    # addrs = socket.getaddrinfo(socket.gethostname(), None)
    # Check all users running this site

    def start_server():
        print("Server is running at " + time.ctime())
        app.run(host='localhost',port=8000,debug=True,use_reloader=True)

    def start_client():
        print("Client is running at " + time.ctime())
        webbrowser.open("http://{0}:{1}".format(config['client']['HOST'],config['client']['PORT']))
 
    start_server()
