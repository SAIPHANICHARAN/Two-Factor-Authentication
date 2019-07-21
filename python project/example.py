import time
import threading

def calc_square(numbers):
    print(input("enter"))
        

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t2.start()
t1.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
