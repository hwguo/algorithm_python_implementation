#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   henry
#   E-mail  :   hwguo1988@gmail.com
#   Date    :   17/11/06 23:32:17
#   Desc    :   
#

class Trie:
    """ Trie tree python implementation
    """
    def __init__(self):
        self.root = {}
        self.END = '/'


    def add(self, word):
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node[self.END] = None


    def find(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.END in node


def main():
    trie = Trie()
    trie.add('haha')
    trie.add('habe')
    trie.add('hct')

    print trie
    print trie.find('h')


if __name__ == '__main__':
    main()
