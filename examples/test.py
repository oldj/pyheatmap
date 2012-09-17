# -*- coding: utf-8 -*-
#
# author: oldj
# blog: http://oldj.net
# email: oldj.wu@gmail.com
#

# -*- coding: utf-8 -*-

from pyheatmap.heatmap import HeatMap


def loadDataFromFile(fn):

    lines = open(fn).read().split("\n")
    data = []
    for ln in lines:
        a = ln.split(",")
        if len(a) != 2:
            continue
        a = [int(i) for i in a]
        data.append(a)

    return data


def example2():

    data_1 = loadDataFromFile("test_data.txt")
    data_2 = loadDataFromFile("test_data2.txt")

    hm = HeatMap(data_1)
    hit_img = hm.clickmap()
    hm2 = HeatMap(data_2)
    hit_img2 = hm2.clickmap(base=hit_img, color=(0, 0, 255, 255))
    hit_img2.save("hit2.png")


def example1():

    # 加载测试数据
    data = loadDataFromFile("test_data.txt")

    # 开始绘制
    hm = HeatMap(data)
    hm.clickmap(save_as="hit.png")
    hm.heatmap(save_as="heat.png")


def main():
#    example1()
    example2()


if __name__ == "__main__":
    main()

