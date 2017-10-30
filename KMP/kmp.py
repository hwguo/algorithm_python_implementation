#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   henry
#   E-mail  :   gzguohongwei@corp.netease.com
#   Date    :   17/10/28 21:20:40
#   Desc    :   
#


def find_next(pattern_str):
    next_array = []
    length = len(pattern_str)
    for i in range(length):
        prefix = set()
        postfix = set()
        prefix = {pattern_str[:j] for j in range(1, i+1)}
        postfix = {pattern_str[j:i+1] for j in range(1, i+1)}
        next_array.append(len((prefix&postfix or ({''})).pop()))

    for i in range(length):
        if next_array[i] == 0:
            next_array[i] = 1
        else:
            next_array[i] = i - next_array[i] + 1
    print next_array
    return next_array


def kmp(origin_str, pattern_str):
    length_ori = len(origin_str)
    length_pat = len(pattern_str)
    cur = 0     # 起始指针
    next_array = find_next(pattern_str)     # 求解next数组

    while cur < length_ori-length_pat:
        flag = 0
        for i in range(length_pat):
            if origin_str[cur+i] != pattern_str[i]:
                cur += next_array[i]
                flag = 1
                break
        if flag:
            continue
        else:
            return cur     # for循环匹配了pattern串
    
    return False


def main():
    print kmp('bacbababadababacambabacaddababacasdsd', 'ababaca')


if __name__ == '__main__':
    main()
