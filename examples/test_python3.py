# -*- coding: utf-8 -*-
__author__ = 'kevin'

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

    hm = HeatMap(data)
    hm.clickmap(save_as="hit.png")
    hm.heatmap(save_as="heat.png")

    
if __name__ == "__main__":
    main()
