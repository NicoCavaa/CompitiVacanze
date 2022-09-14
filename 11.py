class NumeriRomani:
    def romani(self, s):
        nRom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = 0
        for i in range(len(s)):
            if i > 0 and nRom[s[i]] > nRom[s[i - 1]]:
                n += nRom[s[i]] - 2 * nRom[s[i - 1]]
            else:
                n += nRom[s[i]]
        return n

print(NumeriRomani().romani('MCLX'))
print(NumeriRomani().romani('M'))
print(NumeriRomani().romani('X'))
