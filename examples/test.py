# -*- coding: utf-8 -*-
#
# author: oldj
# blog: http://oldj.net
# email: oldj.wu@gmail.com
#

# -*- coding: utf-8 -*-

from pyheatmap.heatmap import HeatMap

def main():

    # 加载测试数据
    sdata = open("test_data.txt").read().split("\n")
    data = []
    for ln in sdata:
        a = ln.split(",")
        if len(a) != 2:
            continue
        a = [int(i) for i in a]
        data.append(a)

    # 开始绘制
    hm = HeatMap(data)
    hm.clickmap(save_as="hit.png")
    hm.heatmap(save_as="heat.png")

if __name__ == "__main__":
    main()

