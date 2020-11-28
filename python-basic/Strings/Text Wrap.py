import textwrap

def wrap(string, max_width):
    res = textwrap.fill(string, width=max_width)
    return res

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)