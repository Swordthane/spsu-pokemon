from server import server

class world(server):
    def __init__(self, ipAddress, port):
        server.__init__(ipAddress, port)

    def tick(self):
        pass
