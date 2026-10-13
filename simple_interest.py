def simInt(principal,interest,time):
    return(principal*interest*time)/100

if __name__ == "__main__":
    p= float(input("Enter the principal amount: "))
    i = float(input("Enter the interest rate: "))
    t = float(input("Enter the time in years: "))
    
    simple_interest = simInt(p, i, t)
    print(f"The simple interest is: {simple_interest}")