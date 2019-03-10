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

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nter <= 0:
   print("Please enter a positive integer")
elif nter == 1:
    print("Fibonacci bis zu",nter,":")
    print(n1)
else:
    liste=[]
    while count < nter:
        #print(n1,end=' , ')
        nn = n1 + n2
        liste.append(n1)
        # update values
        n1 = n2
        n2 = nn
        count += 1
        if count == nter-1:
            lastn=n1
end = timer()

if args.all:
    print ("all Fibonacci numbers up to position: ", args.nn, ": ",str(liste).strip('[]'))
    print("runtime: ",end - start)
if args.n:
    print ("Fibonacci number at position:", args.nn, ": ", lastn)
    print("runtime: ",end - start)
