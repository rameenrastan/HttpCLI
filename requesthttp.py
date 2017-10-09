# entry point for http request application

# COMP 445 Assignment 1
# cURL-like Command Line
# Rameen Rastan-Vadiveloo (27191863)
# Vincent Fugnitto (27207999)


import client
import controller


def main():
    request = client.parse()
    controller.serve_request(request)


if __name__ == '__main__':
    main()
