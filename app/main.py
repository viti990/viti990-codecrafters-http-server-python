# Uncomment this to pass the first stage
import socket

BUFFER = 1024
CRLF = "\r\n"
HEADERS_END = CRLF + CRLF
HTTP_200 = "HTTP/1.1 200 OK" + HEADERS_END
HTTP_404 = "HTTP/1.1 404 NOT FOUND" + HEADERS_END
def parse(string_chunk):
    start_line = string_chunk.split(CRLF)[0]
    path = start_line.split(" ")[1]
    if path == '/' + CRLF:
        print('200')
        response = HTTP_200
    elif path.startswith('/echo'):
        print('200')
        response = HTTP_200[:-4] + "{0}Content-Type: text/plain{0}Content-Length: {1}{0}{0}".format(CRLF, len(path[6:])) + \
        path[6:]
    elif path.startswith('/user-agent'):
        print('200')
        response = HTTP_200[:-4] + "{0}Content-Type: text/plain{0}Content-Length: {1}{0}{0}".format(CRLF, len(string_chunk.split(CRLF)[2].split(': ')[1])) + \
        string_chunk.split(CRLF)[2].split(': ')[1]
    else:
        print('404')
        response = HTTP_404
    print(response)
    return response
def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!!")
    
    with socket.create_server(("localhost", 4221)) as server_socket:
        while True:
            conn, address = server_socket.accept() 
            with conn:
                chunk = conn.recv(BUFFER)
                string_chunk = chunk.decode("utf-8")
                response = parse(string_chunk)
                conn.send(response.encode())


if __name__ == "__main__":
    main()