# HTTPClient used to process GET / POST Requests
import socket
import sys


def get_request(url):
    # format: get [-v] [-h key:value] URL
    return "GET / HTTP/1.1\r\nHost: %s\r\n\r\n" % url


def post_request(url):
    # format: post [-v] [-h key:value] [-d inline-data] [-f file] URL
    # TODO process post request
    return "" % url


def run(url):

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
        s.connect((url, port))
        s.sendall(get_request(url).encode('utf-8'))
    except socket.gaierror:
        # print error, close socket and exit system
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
    # TODO replace with correct URL from user input
    url = 'www.cnn.com'
    run(url)


# main function call
if __name__ == '__main__':
    main()
