# -*- coding: utf-8 -*-
#
# author: oldj
# blog: http://oldj.net
# email: oldj.wu@gmail.com
#

import random


def main():

    width = 400
    height = 300

    # 随机生成测试数据
    data = []
    r = 50
    for i in range(4):
        data.append([
            random.randint(0, width - 1),
            random.randint(0, height - 1),
            ])
    for i in xrange(12):
        data2 = []
        for x, y in data:
            x2 = x + random.randint(-r, r)
            y2 = y + random.randint(-r, r)
            data2.append([x2, y2])
        data.extend(data2)
    print(len(data))

    f = open("test_data.txt", "w")
    for x, y in data:
        f.write("%d,%d\n" % (x, y))
    f.close()


if __name__ == "__main__":
    main()
