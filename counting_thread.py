import threading

"""
     |  __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None)
     |      This constructor should always be called with keyword arguments. Arguments are:
     |      
     |      *group* should be None; reserved for future extension when a ThreadGroup
     |      class is implemented.
     |      
     |      *target* is the callable object to be invoked by the run()
     |      method. Defaults to None, meaning nothing is called.
     |      
     |      *name* is the thread name. By default, a unique name is constructed of
     |      the form "Thread-N" where N is a small decimal number.
     |      
     |      *args* is the argument tuple for the target invocation. Defaults to ().
     |      
     |      *kwargs* is a dictionary of keyword arguments for the target
     |      invocation. Defaults to {}.
     |      
     |      If a subclass overrides the constructor, it must make sure to invoke
     |      the base class constructor (Thread.__init__()) before doing anything
     |      else to the thread.
"""
class CountingThread(threading.Thread):
   def __init__(self,num):
      print "thread created!"
      threading.Thread.__init__(self,None, None,None, (),{},None)
      self.num = num
   def run(self):
      for i in range (1,1000):
         i = i*1  #waste time
      for i in range(1,self.num):
         for j in range (1,1000000):
            j =j*1  #waste time
         print "I am a thread that will count up to", self.num, "and I am at", i
      print self.num, "! done!"
