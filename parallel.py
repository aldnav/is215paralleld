import multiprocessing as mp
import requests

output_dir = './out_serial/'
input_links = []


def readInput(q):
    with open('top100.txt') as f:
        for l in f.readlines():
            q.put(l.strip())
    return q


def readPage(q):
    while True:
        link = q.get()

        if link is None:
            break

        r = requests.get(link)
        print('Saving "{}"'.format(link))
        with open(output_dir + link.split('http://')[-1] + '.html', 'w+') as f:
            f.write(r.text)


if __name__ == '__main__':
    global q
    mp.set_start_method('spawn')
    q = mp.Queue()
    readInput(q)
    q.put(None)

    num_processes = 4
    workers = []
    for i in range(num_processes):
        workers.append(mp.Process(target=readPage, args=(q,)))
    
    for worker in workers:
        worker.start()
    
    for worker in workers:
        worker.join()
