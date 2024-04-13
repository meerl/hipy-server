#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : qjs_drpy_test.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Author's Blog: https://blog.csdn.net/qq_32394351
# Date  : 2024/4/13

from qjs_drpy import Drpy

if __name__ == '__main__':
    drpy = Drpy(debug=1)
    # drpy.init('https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/raw/main/js/荐片.js')
    # drpy.init('https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/raw/main/js/555影视[飞].js')
    # drpy.init('https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/raw/main/js/农民影视.js')
    # drpy.init('https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/raw/main/js/996影视.js')
    # drpy.init('https://ghproxy.liuzhicong.com/https://github.com/hjdhnx/dr_py/raw/main/js/奇珍异兽.js')
    # with open('../files/drpy_js/freeok.js', encoding='utf-8') as f:
    # with open('../files/drpy_js/农民影视.js', encoding='utf-8') as f:
    with open('../files/drpy_js/农民影视新.js', encoding='utf-8') as f:
        # with open('../files/drpy_js/耐看.js', encoding='utf-8') as f:
        code = f.read()
    drpy.init(code)
    drpy.setDebug(1)
    # print(drpy.homeContent())
    # print(drpy.homeVideoContent())
    # print(drpy.categoryContent('2', 1, False, {}))
    # print(drpy.detailContent('https://m.emsdn.cn/vod-detail-id-38818.html'))
    # f = quickjs.Function(
    #     "adder", """
    #             function adder(x, y) {
    #                 return x + y;
    #             }
    #             """)

    # print(drpy.categoryContent('3', 1, False, {}))
    # print(drpy.categoryContent('2', 1, False, {}))
    # print(drpy.detailContent("3$/detail/790.html"))
    # print(drpy.detailContent("https://nkvod.com/detail/185851.html"))
    # print(drpy.playerContent("索尼", "https://www.cs1369.com/play/790-1-1.html", []))
    # print(drpy.playerContent("量子资源", "https://nkvod.com/play/185851-2-1.html", []))
    print(drpy.searchContent("斗罗大陆", False, 1))
