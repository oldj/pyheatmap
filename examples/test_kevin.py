__author__ = 'kevin'
# -*- coding: utf-8 -*-

import urllib.request
from pyheatmap.heatmap import HeatMap


def main():

    data = []
    # download test data
    url = "https://raw.github.com/oldj/pyheatmap/master/examples/test_data.txt"
    for line in urllib.request.urlopen(url):
        line_str = str(line, encoding='utf-8').split("\n")
        for ln in line_str:
            if ',' in ln:
                a = ln.split(",")
                a = [int(i) for i in a]
                data.append(a)
    # print(data)

    hm = HeatMap(data)
    hm.clickmap(save_as="hit.png")
    hm.heatmap(save_as="heat.png")

    '''
    data = []
    for ln in sdata:
        a = ln.split(",")
        if len(a) != 2:
            continue
        a = [int(i) for i in a]
        data.append(a)

    # start painting
    hm = HeatMap(data)
    hm.clickmap(save_as="hit.png")
    hm.heatmap(save_as="heat.png")
    '''
if __name__ == "__main__":
    main()