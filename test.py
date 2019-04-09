import pandas 
import os
df = pandas.read_csv('Book1.csv')
df2 = pandas.read_csv('ValueCompare.csv')
titles=df['title']
keys=df2['key']
index=0
def replaceValue(start,end):
    index=start
    while index<end :
        keyIndex=0
        while keyIndex<len(keys):
                if titles[index] == keys[keyIndex]:
                        df.set_value(index,'google_product_category',df2['value'][keyIndex])
                        print(titles[index])
                keyIndex+=1
        index+=1
    df.to_csv('Book1.csv', index=False)



from threading import Thread
import threading
import time
# 0984393763


try:
        t = time.time()
        times=0
        while 1==1 :
                if times + 3 < len(titles) :
                        t1 = threading.Thread(target=replaceValue,args=(times,times+3))
                        t1.start()
                        times+=3
                else :
                        t1 = threading.Thread(target=replaceValue,args=(times,len(titles)))
                        t1.start()
                        break
        print ("done in ", time.time()- t)
except:
	print ("error")
