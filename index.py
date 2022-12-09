import _thread
from flask import Flask
from flask import request
import math
from time import sleep

arr=[None]*10

def buckerSort(i):
    
    #arr[math.floor((x[i]*10))]=x[i]
    index=math.floor(i*10)
   # print(index)
    arr[index]=i
    
    

def bucketSortParallel(buckets):
    for i in buckets:
        print(i)
        arg_tuple=(i,)
        _thread.start_new_thread(buckerSort,arg_tuple)
    print(arr)



    

  


app=Flask(__name__)

@app.route('/',methods = ['POST'])

def getArrayAndSort():
    array=request.json['array']
    bucketSortParallel(array)
    sleep(0.001)
    return {'sorted':arr}


        

if __name__ == '__main__':

    app.run(debug=False)



