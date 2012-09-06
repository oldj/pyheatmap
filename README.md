#pyHeatMap

 * Author: oldj
 * Email: oldj.wu@gmail.com
 * Blog: http://oldj.net/
 * Source: https://github.com/oldj/pyheatmap


这是一个生成热图的小程序，基于 Python 和 PIL 开发。


##程序截图：

###点击图

![点击图](https://raw.github.com/oldj/pyheatmap/master/examples/hit.png)

###热图

![热图](https://raw.github.com/oldj/pyheatmap/master/examples/heat.png)


##安装：

###通过 pip 安装：

    pip install pyheatmap

###通过 easy_install 安装：

    easy_install pyheatmap


###通过源码安装：

    git clone git://github.com/oldj/pyheatmap.git
    cd pyheatmap
    python setup.py install


##使用示例：

    # -*- coding: utf-8 -*-

    import urllib
    from pyheatmap.heatmap import HeatMap

    def main():

        # 下载测试数据
        url = "https://raw.github.com/oldj/pyheatmap/master/examples/test_data.txt"
        sdata = urllib.urlopen(url).read().split("\n")
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


##版权及致谢：

 本程序完全免费，并基于 LGPL 协议开源。


##更新历史：

 - 2012-09-03 建立本项目。



