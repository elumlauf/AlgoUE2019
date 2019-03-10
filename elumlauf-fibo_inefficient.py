from timeit import default_timer as timer
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("nn", type=int, help="Position der letzten Fibonaccizahl")
text="elumlauf-fibo_efficient.py berechnet Fibonacci Zahlen: mit <int> -all werden alle Zahlen angegeben, " \
     "mit <int> -n wird die Zahl an der Position <int> angegeben"
#parser = argparse.ArgumentParser(description = text)
#parser = argparse.ArgumentParser(description='This is my help')
parser.add_argument("-all", help="shows all Fibonacci numbers up to entered position", action="store_true")
parser.add_argument("-n", help="shows only the Fibonacci number corresponding to the entered position", action="store_true")
args = parser.parse_args()

nter = args.nn
start = timer()

def recursion_fibo(n):
   if n <= 1:
       return n
   else:
       return(recursion_fibo(n-1) + recursion_fibo(n-2))

# check if the number of terms is valid
if nter <= 0:
   print("Please enter a positive integer")
else:
    liste=[]
    #print("Fibonacci sequence:")
    for i in range(nter):
        #print(recursion_fibo(i))
        liste.append(recursion_fibo(i))
        #print(recursion_fibo(i), end =" , ")
end = timer()

if args.all:
    print ("all Fibonacci numbers up to position ", args.nn, ": ",str(liste).strip('[]'))
    print("runtime: ",end - start)
if args.n:
    print ("Fibonacci number at position", args.nn, ": ", liste[-1])
    print("runtime: ",end - start)

