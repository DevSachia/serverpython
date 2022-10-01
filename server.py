import socket
import os
import mimetypes


HEADER = 1024
#define port
PORT = 2728
#define ip adress
SERVER = socket.gethostbyname(socket.gethostname()) #get the ip address automatically, its help full when we run this server in deferent device.
ADDR = (SERVER,PORT) 
FORMAT = 'utf-8'
#create a new socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind socket to a adress

server.bind(ADDR)

def getresource_path(http_path: str): #works above python 3.5
    if http_path.endswith('/'):
             http_path = http_path[0:-1]  #remove the last char('/') if client type / with the path
    print(http_path, http_path.split('.'))
    path_segments = http_path.split('.')
    if not (http_path == ''):
        if len(path_segments) > 1:
            print("Requested a file with extension")
            html_file_path = os.path.join(
                os.getcwd(), "htdocs", http_path[1:]) 
        else:
            html_file_path = os.path.join(
                os.getcwd(), "htdocs", f"{http_path[1:]}.html") #geting requested file path platform independntly
    else:
        html_file_path = os.path.join(os.getcwd(), "htdocs", "index.html") #geting file path platform independntly
    print(html_file_path)
    return html_file_path




#Handle new connections and contribue
def start():
    server.listen() #listning for new connections
    print(f"[Listening] server is listening on {SERVER}")
    while True:
        conn,addr = server.accept()  #making soket to listen and wait for new connections
        #wait to recive information from client
        print(f"[New connection] {addr} connected")
        msg = conn.recv(HEADER).decode(FORMAT)
        split_header = msg.split("\r\n") #spliting the request to geting  the resource path
        path = split_header[0]
        path_version_header = path.split(" ")
        try:
            http_url = path_version_header[1] # inclued path + Query parameters
            http_path = http_url.split('?')[0] #get path by separate of Query parameter
            resourse_path = getresource_path(http_path) #geting relvant html content path
            try:
                htmlFile = open(resourse_path,"r") #opening a html path relavant to desiered file
                html_file_content = htmlFile.read()
                htmlFile.close()
                content_type = mimetypes.guess_type(resourse_path)
                http_response = f"HTTP/1.1 200 OK\r\nServer: My Custom Server\r\nContent-Length: {len(html_file_content)}\r\nContent-Type: {content_type[0]}\r\n\n{html_file_content}"
                conn.sendall(http_response.encode())
            except FileNotFoundError:
                conn.sendall("HTTP/1.1 404 File not found".encode())
        except IndexError:
            conn.sendall("HTTP/1.1 400 Bad Request".encode())
        conn.close() 
        


print("[Starting] Server is starting")
start()




