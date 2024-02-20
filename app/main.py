# Uncomment this to pass the first stage
import socket
import threading
import sys
BUFFER = 1024
CRLF = "\r\n"
HEADERS_END = CRLF + CRLF
HTTP_200 = "HTTP/1.1 200 OK" + HEADERS_END
HTTP_201 = "HTTP/1.1 201 OK" + HEADERS_END
HTTP_404 = "HTTP/1.1 404 NOT FOUND" + HEADERS_END
def worker(conn):
    chunk = conn.recv(BUFFER)
    string_chunk = chunk.decode("utf-8")
    start_line = string_chunk.split(CRLF)[0]
    path = start_line.split(" ")[1]
    print(string_chunk)
    if string_chunk.startswith("GET"):
        if path == '/':
            response = HTTP_200
            print('200')
        elif path.startswith('/echo'):
            response = HTTP_200[:-4] + "{0}Content-Type: text/plain{0}Content-Length: {1}{0}{0}".format(CRLF, len(path[6:])) + \
            path[6:]
            print('200')
        elif path.startswith('/user-agent'):
            response = HTTP_200[:-4] + "{0}Content-Type: text/plain{0}Content-Length: {1}{0}{0}".format(CRLF, len(string_chunk.split(CRLF)[2].split(': ')[1])) + \
            string_chunk.split(CRLF)[2].split(': ')[1]
            print('200')
        elif path.startswith('/files'):
            try:
                body = open("{}/{}".format(sys.argv[2],path[7:]),"r").read()
                response = HTTP_200[:-4] + "{0}Content-Type: application/octet-stream{0}Content-Length: {1}{0}{0}".format(CRLF, len(body)) + \
                body
                print('200')
            except:
                response = HTTP_404[:-4]+"{0}Content-Length: {1}{0}{0}".format(CRLF, 0)
                print('404')
        else:
            response = HTTP_404
            print('404')
    elif string_chunk.startswith("POST"):
        body = string_chunk.split(HEADERS_END)[1]
        body.open("{}/{}".format(sys.argv[2],path[7:]),"w").write()
        response = HTTP_201
    conn.send(response.encode())
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!!")
    server_socket = socket.create_server(("localhost", 4221)) 
    while True:
        conn, address = server_socket.accept()
        threading.Thread(target=worker, args=(conn,)).start()
if __name__ == "__main__":
    main()