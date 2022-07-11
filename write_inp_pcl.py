#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：modeling range of micro-region 
@File    ：write_inp_pcl.py
@Author  ：hoult18
@Date    ：2022/7/10 11:04 
"""
from config import *
def print_pcl_line(job_name):
    print(f"cmd/c abaqus job={job_name} interactive")

print(boundary)
for L in lengths:
    job_name = boundary+'-'+str(L)
    print_pcl_line(job_name=job_name)