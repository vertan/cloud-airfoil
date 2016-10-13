from tasks import add

for i in xrange(10000):
    add.delay(i,i)
