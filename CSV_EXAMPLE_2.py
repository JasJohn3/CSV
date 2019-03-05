import csv

with open('mycsv.csv','w',newline='') as file:
    fieldnames = ['Column 1','Column 2', 'Column 3']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()


    for i in range(100):
        writer.writerow({'Column 1': 'co1', 'Column 2': 'col2', 'Column 3': 'col3'})


import _thread
import time

def print_epoch(name_of_thread, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count+=1
        print(name_of_thread, "----------",time.time())

try:
    _thread.start_new_thread(print_epoch,("Thread 1", 2))
    _thread.start_new_thread(print_epoch,("Thread 2", 3))
except:
    print("Program Encountered an Error")
while 1:
    pass