import traceback
from twisted.python import log

def stack():
    print('The python stack:')
    traceback.print_stack(file=log.logfile)

from twisted.internet import reactor
reactor.callWhenRunning(stack)
reactor.run()
