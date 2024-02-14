# Uncomment this to pass the first stage
import socket

BUFFER = 1024
CRLF = "\r\n"
HEADERS_END = CRLF + CRLF
HTTP_200 = "HTTP/1.1 200 OK" + HEADERS_END
HTTP_404 = "HTTP/1.1 404 NOT FOUND" + HEADERS_END

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!!")
    
    with socket.create_server(("localhost", 4221)) as server_socket:
        while True:
            conn, address = server_socket.accept() 
            with conn:
                chunk = conn.recv(BUFFER)
                string_chunk = chunk.decode("utf-8")
                start_line = string_chunk.split(CRLF)[0]
                path = start_line.split(" ")[1]
                if path[0] == '/':
                    print('200')
                    if len(path)-1 == 0:
                        response = HTTP_200
                    else:
                        response = HTTP_200[:-4] + "{0}Content-Type: text/plain{0}Content-Length: {1}{0}".format(CRLF, len(path[1:].split('/')[1])-1) + \
                        path[1:].split("/")[1]
                    print(response.encode())
                    conn.send(response.encode())
                else:
                    print('404')
                    conn.send(HTTP_404.encode())


if __name__ == "__main__":
    main()