#from tasks import add

#for i in xrange(10000):
#    add.delay(i,i)

from test_tasks import get_flow_simple, get_flow

get_flow_simple.delay()
