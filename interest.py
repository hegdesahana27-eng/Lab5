import sys
def simInt(principal,interest,time):
    return(principal* interest*time)/100
if __name__ == "__main__":
    p=int(input(sys.argv[1]))
    i=int(input(sys.argv[2]))
    t=int(input(sys.argv[3]))

    print("Simple interest:",simInt(p,i,t))