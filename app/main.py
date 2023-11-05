# Uncomment this to pass the first stage
import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!!")
    HEADERS_END = '/r/n'*2
    HTTP_200 = "HTTP/1.1 200 huehuebrbr" + HEADERS_END
    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221))
    conn, addr = server_socket.accept()
    #print(f"Connected by {addr}")
    conn.recv(1024)
    conn.send(HTTP_200.encode())
    #conn.send(data.encode())


if __name__ == "__main__":
    main()
