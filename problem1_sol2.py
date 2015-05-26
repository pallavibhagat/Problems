# -*- coding: utf-8 -*-
import re
s = "We are at Ignite Solutions! Their email­-id is careers@ignitesol.com"
print re.sub(r'[\-a-zA-Z]+', lambda x: x.group(0)[::-1], s)


"""
Here I am facing issue with (-). its not coming at the proper place
"""