import sys

def simInt(principal,interest,time):
    return(principal*interest*time)/100

if __name__ == "__main__":
    p= int(sys.argv[1])
    i = float(sys.argv[2])
    t = float(sys.argv[3])
    
    simple_interest = simInt(p, i, t)
    print(f"The simple interest is: {simple_interest}")