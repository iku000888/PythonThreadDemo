import counting_thread

th1 = counting_thread.CountingThread(10)
th2 = counting_thread.CountingThread(20)
th3 = counting_thread.CountingThread(30)
th4 = counting_thread.CountingThread(40)

print th1
print th2
print th3
print th4


th1.start()
th2.start()
th3.start()
th4.start()

#th54.run()
#th20.run()
#th4.run()
