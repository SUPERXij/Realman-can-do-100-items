fp = open('test1.txt')
a = fp.read()
fp.close()

fp = open('test2.txt')
b = fp.read()
fp.close()

fp = open('test3.txt', 'w')
l = list(a + b)
l.sort()
s = ''
s = s.join(l)
fp.write(s)
fp.close()
