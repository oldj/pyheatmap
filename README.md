# pyHeatMap

 * Author: oldj
 * Email: oldj.wu@gmail.com
 * Blog: http://oldj.net/
 * Source: https://github.com/oldj/pyheatmap


pyHeatMap is a Python library for painting heat maps. It depends on [Pillow](https://python-pillow.github.io/).
Python 2/3 compatible.


## Screenshots

### hit map

![hit map](https://raw.github.com/oldj/pyheatmap/master/examples/hit.png)

### heat map

![heat map](https://raw.github.com/oldj/pyheatmap/master/examples/heat.png)


## Install

### by pip:

    pip install pyheatmap

### by easy_install:

    easy_install pyheatmap


### from source code:

    git clone git://github.com/oldj/pyheatmap.git
    cd pyheatmap
    python setup.py install


## Example:

```python
# -*- coding: utf-8 -*-

from pyheatmap.heatmap import HeatMap
import requests

def main():

    # download test data
    url = "https://raw.github.com/oldj/pyheatmap/master/examples/test_data.txt"
    sdata = requests.get(url).text.split("\n")
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

if __name__ == "__main__":
    main()

```

## Copyright

 This library is free and is provided under the MIT open source license.


## Update

 - 2015-08-31 Python 2/3 compatible.
 - 2012-09-03 Create.



