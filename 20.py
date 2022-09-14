def specchia(linea):
    linea = linea.split('\n')
    maxL = max(map(len, linea))
    linea = map(lambda x: x + '\0'* (maxL - len(x)), linea)
    return '\n'.join(map(lambda x: ''.join(x).rstrip('\0'), zip(*linea))).replace('\0',' ')