# entry point for http request application
import client
import controller


def run():
    print('')


def main():
    request = client.parse()
    controller.serve_request(request)


if __name__ == '__main__':
    main()
