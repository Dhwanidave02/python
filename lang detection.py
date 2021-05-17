# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:06:02 2021

@author: DHWANI
"""

from langdetect import detect
text = input("Enter any text in any language: ")
print(detect(text))