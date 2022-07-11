#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：modeling range of micro-region 
@File    ：postprocess.py
@Author  ：hoult18
@Date    ：2022/7/10 10:40 
"""
from config import *
print(boundary)
for L in lengths:
    first_eigenvalue = -1
    with open(f"{boundary}\\{boundary}-" + str(L) + ".dat", "r") as openfile:
        for line in openfile:
            if "MODE NO      EIGENVALUE" in line:
                for line in openfile:
                    if "1" in line:
                        first_eigenvalue = float(line[8:])
                        break
                break
    print(f"{L} {first_eigenvalue}")
