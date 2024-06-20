
import os
import glob
from posixpath import splitext
directory_path = 'C:/Users/sai.h.chengalva/Desktop/Assignment1'
files = glob.glob("*.csv")
latest_created_file=0
for i in os.scandir(directory_path):
    print(i.stat())
    created_at=i.stat().st_ctime_ns

    if splitext(i)[1]==".csv" and created_at>latest_created_file:
        latest_created_file=created_at
print("The latest created file is")
for i in os.scandir(directory_path):
    # print(splitext(i)[1])
    if splitext(i)[1]==".csv" and i.stat().st_ctime_ns==latest_created_file:
        print(i.name)
    