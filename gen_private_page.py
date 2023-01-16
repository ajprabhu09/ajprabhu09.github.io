#! /usr/bin/python3
import os
import hashlib
import sys


assert len(sys.argv) > 1

passw = sys.argv[1]

hash = hashlib.sha1(passw.encode()).hexdigest()

file = f"""---
layout: post
title: {passw}
permalink: /password/{hash}/
---
put your protected content here

"""
# print(hash)

assert not os.path.exists(f"password/{hash}")

os.system(f"mkdir password/{hash}")
with open(f"password/{hash}/index.markdown",'w+') as f:
    f.write(file)
