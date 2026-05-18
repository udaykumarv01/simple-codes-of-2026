import os
 
curdir=os.getcwd()
os.mkdir('folder1')

import time 

time.sleep(5)

os.rename('folder1','folder2')