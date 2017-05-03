# coding: utf-8
import sys


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv

    if not args:
        print('usage: [--script] (cypher) (key)')
        sys.exit(1)

    cypher = list(args[1])
    key = list(args[2])
    code = []
    for k, c in zip(key, cypher):
        if k == c:
            code.append(0)
        else:
            code.append(1)
    codestr = (str(w) for w in code)
    codestr = (''.join(codestr))
    n = int(codestr, 2)
    plaintxt = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    text_file = open("code.txt", "w")
    text_file.write("original code: %r" % (codestr) + "\n"
                    "plain txt: %r" % (plaintxt))
    text_file.close()


if __name__ == '__main__':
    main()
