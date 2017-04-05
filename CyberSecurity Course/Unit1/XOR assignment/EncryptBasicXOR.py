# coding: utf-8
import sys


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv
    # usage information to user
    if not args:
        print(
            'usage: [--script] (code) N.B script will create 2 files one containing the cypher the other the key')
        sys.exit(1)

    code = list(args[1])
    cypher = []
    # function to generat key

    def GenerateKey(code):
        import numpy as np
        global key
        key = np.random.choice([0, 1], size=(len(code),))
        return key
    # Call key function
    GenerateKey(code)
    likey = key.tolist()
    Key = str(key)
    Key = Key.strip('\[\]')
    text_file = open("Key.txt", "w")
    text_file.write("key: %r" % (Key))
    text_file.close()
    # Generate the cypher
    code = list(map(int, code))
    for k, c in zip(likey, code):
        if k == c:
            cypher.append(0)
        else:
            cypher.append(1)
    cypherstr = (str(w) for w in cypher)
    cypherstr = (''.join(cypherstr))
    text_file = open("cypher.txt", "w")
    text_file.write("cypher: %r" % (cypherstr))
    text_file.close()


if __name__ == '__main__':
    main()
