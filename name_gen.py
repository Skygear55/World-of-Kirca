# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:53:39 2020

@author: k.kirilov
"""

import numpy as np
import random as rm 
import csv

class nameGen():
    def __init__(self, file_path, n):
        self.file_path = file_path
        self.n = n
        self.data = self.get_name_list(self.file_path)
        self.chain = self.build_markov_chain(self.data, self.n)
        
    def get_name_list(self, file_path, encoding = 'utf-8'):
        name_list = []
        with open (file_path, encoding = encoding) as names_csv: 
            names = csv.reader(names_csv)
            for row in names:
                name_list.append(''.join(row))
            return name_list
        
    def build_markov_chain(self, data, n):
        chain = {
            '_initial': {}, 
            'names': set(data)
            } 
        for name in chain['names']: 
            word_wrapped = name + "."
            for i in range(len(word_wrapped) - n):
                _tuple = word_wrapped[i : i+n]
                _next = word_wrapped[i + 1 : i + n + 1]
                
                if _tuple not in chain: 
                    entry = chain[_tuple] = {}
                if i == 0:    
                    if _tuple not in chain['_initial']: 
                        chain['_initial'][_tuple] = 1
                    else:
                        chain['_initial'][_tuple] += 1
                if _next not in entry:
                    entry[_next] = 1
                else:
                    entry[_next] += 1
        return chain    
    
    def select_random_item(self, items):
        rnd = rm.random() * sum(items.values())
        for item in items: 
            rnd -= items[item]
            if rnd < 0:
                return item
            
    def generate(self, chain):
        _tuple = self.select_random_item(chain['_initial'])
        result = [_tuple]
    
        while True:
            _tuple = self.select_random_item(chain[_tuple])
            last_character = _tuple[-1]
            if last_character == '.':
                break
            result.append(last_character)
    
        generated = ''.join(result)
        if generated not in chain['names']:
            return generated
        else:
            return self.generate(chain)
    
def nameGen_caller(): 
    pass

#post on stackoverflow to ask why this works better than the original cod