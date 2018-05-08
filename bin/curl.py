#!/usr/bin/python3

import io
import os
import sys
import queue
import threading
import pycurl
import time

ln = 1
ln_mutex = threading.Lock()
q = queue.Queue(maxsize=0)
done = 0

max_threads = 5
qu = [[0, 0, 0, 0, 0, '']]

def format_byte_str(num):
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei']:
        if abs(num) < 1024.0:
            return "%3.1f%sB" % (num, unit)
        num /= 1024.0
    return "%.1f%sB" % (num, 'FuckMi')

def put_progress(download_t, download_d, upload_t, upload_d, line, filename):
    global qu
    qu[line-1] = [download_t, download_d, upload_t, upload_d, line, filename]

def progress(download_t, download_d, upload_t, upload_d, line, filename):
    a = 0
    ln_mutex.acquire()
    try:
        global ln
        cl = line - ln
        if cl < 0: sys.stdout.write('\33['+str(-cl)+'A')
        else: sys.stdout.write('\n'*cl)
        sys.stdout.write('\33[2K\r' + format_byte_str(download_d) + " of "
                        + format_byte_str(download_t) + ": " + filename)
        ln = line
    finally:
        ln_mutex.release()

def download_curl(line, url, filename):
    try:
        c = pycurl.Curl()
        f = open(filename, "wb");

        c.setopt(c.URL, url)
        c.setopt(c.NOPROGRESS, False)
        c.setopt(c.XFERINFOFUNCTION,
        lambda download_t, download_d, upload_t, upload_d:
            put_progress(download_t, download_d, upload_t, upload_d, line, filename))
        c.setopt(c.WRITEDATA, f)
        c.perform()
    except:
        sys.stderr.write("Failed while downloading: " + filename)
        c.close()
        return 0
    c.close()
    f.close()
    return 0

def thread_loop():
    global q
    while True:
        tmp = q.get()
        download_curl(tmp[0], tmp[1], tmp[2])
        q.task_done()

def progress_loop():
    global qu
    global done
    while done == 0:
        time.sleep(.100)
        for t in qu:
            if t[4] == 0: continue
            progress(t[0], t[1], t[2], t[3], t[4], t[5])
            t[4] = 0

class mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        thread_loop()
        
class myprogress(threading.Thread):
    def __init__(self, d):
        threading.Thread.__init__(self)
        self.func = d
    def run(self):
        self.func()

def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Usage: " + argv[0] + " [file with URLs].\n")
        exit(1)

    f = open(argv[1], "r")
    url = f.read().splitlines()
    f.close()

    global max_threads
    threads = [None]*max_threads


    global qu
    qu = [[0, 0, 0, 0, 0, '']]*(len(url)//2)
    for cnt in range(0, len(url)//2):
        q.put([cnt+1, url[2*cnt+0], url[2*cnt+1]])

    for t in threads:
        t = mythread()
        t.setDaemon(True)
        t.start()

    progress_t = myprogress(progress_loop)
    progress_t.start()

    q.join()

    global done
    done = 1
    time.sleep(.150)
    print()

main(sys.argv)

