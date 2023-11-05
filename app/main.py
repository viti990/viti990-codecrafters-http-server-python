# Uncomment this to pass the first stage
import socket

BUFFER = 1024
CRLF = "\r\n"
HEADERS_END = CRLF + CRLF
HTTP_200 = "HTTP/1.1 200 OK" + HEADERS_END

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!!")
    
    with socket.create_server(("localhost", 4221), reuse_port=True) as server_socket:
        while True:
            conn, address = server_socket.accept()
            with conn:
                chunk = conn.recv(BUFFER)
                conn.send(HTTP_200.encode())


if __name__ == "__main__":
    main()
