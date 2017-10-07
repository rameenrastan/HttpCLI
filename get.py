# HTTPClient used to process GET / POST Requests
import socket
import sys


def run():

    # port number for socket
    port = 80

    # socket creation
    try:
        s = socket.socket()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        # print error trace and exit call
        print('error during socket creation: %s' % e)
        sys.exit(0)

    # connect to url
    try:
        s.connect(('www.acasann.com', port))
        s.sendall(b"GET / HTTP/1.1\r\nHost: www.cnn.com\r\n\r\n")
    except socket.gaierror:
        print('error resolving host')
        s.close()
        sys.exit(0)

    # process response
    data = s.recv(4096)
    print(data)
    # close socket
    s.close()


# main function
def main():
    run()


# main function call
if __name__ == '__main__':
    main()
