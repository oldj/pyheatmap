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


def tosave(f):
    u""""""

    def func(self, save_as, *kw, **kw2):
        self.save_as = save_as
        result = f(self, save_as, *kw, **kw2)
        self.save()
        return result

    return func

