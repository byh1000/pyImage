import threading, requests, time
from multiprocessing import Process


def sum(seq, low, high):
    total = 0
    for i in range(low, high):
        total += i
    print(seq , "Subthread", total)

def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')

if __name__ == '__main__':
    t1 = Process(target=sum, args=(1, 1, 300000,))
    t1.start()
    #t2 = Process(target=sum, args=(2, 1, 100000))
    #t2.start()
    #t3 = Process(target=sum, args=(3, 1, 100000))
    #t3.start()

    #t4 = Process(target=getHtml, args=('http://google.com',))
    #t4.start()
    #t5 = Process(target=getHtml, args=('http://www.wipson.com',))
    #t5.start()

    print("Main Thread")

