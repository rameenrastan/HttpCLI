# controller module mapping requests
import socket
import sys


def map_request(request):
    if request is not None:
        if request['option'] == 'get':
            return generate_get_request(request)
        elif request['option'] == 'post':
            return generate_post_request(request)
        else:
            print('Error encountered while mapping request.')
            return None
    else:
        sys.exit(1)


def generate_get_request(request):

    complete_url = request.get('url')
    url = complete_url.rsplit('/')[0]
    count = len(url)
    param = complete_url[count:]

    print('param: %s' % param)

    request_str = "GET /%s HTTP/1.1\r\nHost: %s " % (param, url)

    headers = request.get('h')
    if headers is not None:
        for i in headers:
            request_str += "\r\n" + i

    request_str += "\r\n\r\n\r\n"

    return request_str


def generate_post_request(request):

    url = request.get('url')
    request_str = "POST / HTTP/1.1\r\nHost: %s " % url

    headers = request.get('h')
    if headers is not None:
        for i in headers:
            request_str += "\r\n" + i

    request_str += "\r\n\r\n\r\n"

    if request.get('f') is not None:

        request_str += request.get('f')

    elif request.get('d') is not None:

        request_str += request.get('d')    

    return request_str


def serve_request(request):

    request_str = map_request(request)

    if request_str is not None:

        port = 80

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print('error during socket creation: %s' % e)
            sys.exit(0)

        url = request.get('url')
        url_str = url.rsplit('/')[0]

        print('url: %s' % url_str)

        try:
            s.connect((url_str, port))
            print('debug connect 2')
            s.sendall(request_str.encode('ascii'))
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
    print('main')


if __name__ == '__main__':
    main()
