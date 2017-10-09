# controller module mapping requests
import socket
import sys


# map user request to proper request controller method
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


# process request to obtain complete url, url (for connection), and params
def process_url(request):
    complete_url = request.get('url')
    url = complete_url.rsplit('/')[0]
    param = complete_url[(len(url) + 1):]

    return {'complete_url': complete_url, 'url': url, 'param': param}


# generate get request to send through socket
def generate_get_request(request):
    url_dict = process_url(request)

    request_str = "GET /%s HTTP/1.1\r\nHost: %s " \
                  % (url_dict.get('param'), url_dict.get('complete_url'))

    headers = request.get('h')
    if headers is not None:
        for i in headers:
            request_str += "\r\n" + i

    request_str += "\r\n\r\n\r\n"
    return request_str


# generate post request to send through socket
def generate_post_request(request):
    url_dict = process_url(request)

    request_str = "POST /%s HTTP/1.1\r\nHost: %s " % \
                  (url_dict.get('param'), url_dict.get('complete_url'))

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


# serve user request
def serve_request(request):
    request_str = map_request(request)

    if request_str is not None:

        port = 80

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as e:
            print('error during socket creation: %s' % e)
            sys.exit(0)

        url = request.get('url').rsplit('/')[0]

        try:
            s.connect((url, port))
            s.sendall(request_str.encode('utf-8'))
        except socket.gaierror:
            print('error resolving host')
            s.close()
            sys.exit(0)

        data = s.recv(4096)
        data = data.decode('utf-8')

        # display response to user
        print("\n%s" % data)
        s.close()
        sys.exit(1)

    else:
        print('Unknown error encountered while serving request.')


def main():
    print('main')


if __name__ == '__main__':
    main()
