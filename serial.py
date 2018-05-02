import requests

output_dir = './out_serial/'
input_links = []


def readInput(links=[]):
    with open('top100.txt') as f:
        links = [l.strip() for l in f.readlines()]
    return links


def readPages(links):
    for link in links:
        r = requests.get(link)
        print('Saving "{}"'.format(link))
        with open(output_dir + link.split('http://')[-1] + '.html', 'w+') as f:
            f.write(r.text)


if __name__ == '__main__':
    input_links = readInput()
    readPages(input_links)
