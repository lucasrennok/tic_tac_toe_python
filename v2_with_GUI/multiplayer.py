from server import server
from client import client

class multiplayer:
    def __init__(self, host_server, port_server, max_connections, max_bytes, first,game):
        self.first = first
        self.game = game
        if(first==True):
            self.server = client(host_server,port_server, max_bytes)
        else:
            self.server = server("",port_server,max_connections,max_bytes)
        
    def start_server(self):
        self.server.accept_connections()

    def any_receive_mesage(self):
        mesage = self.server.receive_mesage()
        return mesage

    def start_client(self):
        self.server.connect_to_server()

    def any_send_mesage(self,x,y):
        mesage = str(self.calculate_cube(x,y))
        self.server.send_mesage(mesage)
        return mesage

    def close_multiplayer(self):
        self.server.close_connection()

    def calculate_cube(self,p_x,p_y):
        coordinate = 1
        if(p_x==1):
            coordinate = 4
        elif(p_x==2):
            coordinate = 7
        coordinate+=p_y
        return coordinate

    def get_play_first(self):
        return self.first