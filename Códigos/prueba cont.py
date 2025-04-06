import time
cont=0
start_time=time.time() #time

def fib(num):
  global cont
  cont = 0
  if isinstance(num,int)and num>0:
    return (fib_aux(abs(num)),cont,endtime)
  else:
    return 'error'
 
def fib_aux(num):
  if num==0 or num==1:
    return num 
  else:
    global cont
    cont = cont+1
    return fib_aux(num-1)+fib_aux(num-2) 
endtime=time.time()   
  
print(start_time-endtime)
