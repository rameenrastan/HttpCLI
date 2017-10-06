import argparse

# python CLI module
def setup():
    parser = argparse.ArgumentParser()
    parser.add_argument('GET')
    args = parser.parse_args()
    print (args.GET)

def main():
    setup()

if __name__ == '__main__':
    main()
