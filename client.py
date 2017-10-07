import argparse

# python CLI module


def setup():

    parser = argparse.ArgumentParser(add_help=False)

    #add arguments to CLI
    parser.add_argument('option', type=str, nargs='+', choices=set(("get", "post", "help", "get help", "post help")))
    parser.add_argument('-v', action="store_true")
    parser.add_argument('-h', nargs='+', type=str)
    parser.add_argument('-d', type=str)
    parser.add_argument('-f', type=str)
    parser.add_argument('-url', type=str)

    args = parser.parse_args()

    #check if get or post request is called without specifying a URL
    if args.url == None and (args.option == ["get"] or args.option == ["post"]):

        print('Must specify URL.')

    #help
    if args.option == ["help"]:

        print ('\nhttpclient is a curl-like application but supports HTTP protocol only:')
        print ('Usage:\n\thttpclient command [arguments]')
        print ('The commands are:\n\tget\texecutes a HTTP GET request and prints the response.')
        print ('\tpost\texecutes a HTTP POST request and prints the response.')
        print ('\thelp\tprints this screen.')
        print ('Use "httpclient help [command]" for more information about a command.\n')

    #get help
    elif args.option == ["get","help"]:

        print ('\nusage: httpclient get [-v] [-h key:value] URL')
        print ('get executes a HTTP GET request for a given URL.')
        print ('\t-v\tPrints the detail of a response such as protocol, status, and headers.')
        print ('\t-h key:value\tAssociates headers to HTTP request with the format "key:value".\n')

    #post help
    elif args.option == ["post","help"]:

        print ('\nusage: httpclient post [-v] [-h key:value] [-d inline-data] [-f file] URL')
        print ('post executes a HTTP POST request for a given URL with inline data or from file.')
        print ('\t-v\tPrints the detail of a response such as protocol, status, and headers.')
        print ('\t-h key:value\tAssociates headers to HTTP request with the format "key:value".')
        print ('\t-d string\tAssociates an inline data to the body HTTP POST request.')
        print ('\t-f file\tAssociates the content of a file to the body HTTP POST request.')
        print ('Either [-d] or [-f] can be used but not both.\n')     
    
    args_dict = vars(args)

    if (args.option == ["get"] or args.option == ["post"]) and args.url:
        return args_dict
    
    #print(args_dict)
    #print (args.h.split(":"))
    

def main():
    setup()

if __name__ == '__main__':
    main()
