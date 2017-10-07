# controller module mapping requests
import socket
import sys


def map_request(request):
    if request['option'] == 'get':
        generate_get_request(request)
    elif request['option'] == 'post':
        generate_post_request(request)
    else:
        print('Error encountered while mapping request.')


def generate_get_request(request):
    print('generate get request called')


def generate_post_request(request):
    print('generate post request called')


def serve_request(url):

    if url is not None:

        port = 80

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print('error during socket creation: %s' % e)
            sys.exit(0)

        try:
            s.connect((url, port))
            s.sendall(generate_get_request(url).encode('utf-8'))
        except socket.gaierror:
            print('error resolving host')
            s.close()
            sys.exit(0)

        data = s.recv(4096)
        print(data)
        s.close()

    else:
        print('Unknown error encountered while serving request.')


def main():
    print('main called')


if __name__ == '__main__':
    main()
