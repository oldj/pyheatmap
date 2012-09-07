# -*- coding: utf-8 -*-
#
# author: oldj
# blog: http://oldj.net
# email: oldj.wu@gmail.com
#

def getMaxSize(data):
    max_w = 0
    max_h = 0

    for hit in data:
        w = hit[0]
        h = hit[1]
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h

    return max_w, max_h


def mkCircle(r, w):
    u"""根据半径r以及图片宽度 w ，产生一个圆的list
    @see http://oldj.net/article/bresenham-algorithm/
    """

    #__clist = set()
    __tmp = {}

    def c8(ix, iy, v=1):
        # 8对称性
        ps = (
            (ix, iy),
            (-ix, iy),
            (ix, -iy),
            (-ix, -iy),
            (iy, ix),
            (-iy, ix),
            (iy, -ix),
            (-iy, -ix),
            )
        for x2, y2 in ps:
            p = w * y2 + x2
            __tmp.setdefault(p, v)
            #__clist.add((p, v))

    # 中点圆画法
    x = 0
    y = r
    d = 3 - (r << 1)
    while x <= y:
        for iy in range(x, y + 1):
            c8(x, iy, y + 1 - iy)
        if d < 0:
            d += (x << 2) + 6
        else:
            d += ((x - y) << 2) + 10
            y -= 1
        x += 1

    #__clist = __tmp.items()

    return __tmp.items()


def mkColors(n=240):
    u"""生成色盘
    @see http://oldj.net/article/heat-map-colors/

    TODO: 根据 http://oldj.net/article/hsl-to-rgb/ 将 HSL 转为 RGBA
    """

    colors = []
    n1 = int(n * 0.4)
    n2 = n - n1

    for i in range(n1):
        color = "hsl(240, 100%%, %d%%)" % (100 * (n1 - i / 2) / n1)
        #color = 255 * i / n1
        colors.append(color)
    for i in range(n2):
        color = "hsl(%.0f, 100%%, 50%%)" % (240 * (1.0 - float(i) / n2))
        colors.append(color)

    return colors

