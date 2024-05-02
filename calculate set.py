from itertools import combinations

def generate_set(x,limit):
    l=[]
    for i in range(x):
        l1=[]
        for j in range(limit):
            x = int(input(f"enter the {j+1} element of {i+1} set: "))
            l1.append(x)
        l.append(tuple(l1))
    s=set(l)
    return s

def calculate_set(superset):
    solved_set = set()
    x = input("you want to find the union of set?(yes/no)\n")
    for subsets in superset:
        if x == "yes":
            solved_set |= set(subsets)
        elif x== "no":
            solved_set &= set(subsets)
    return(solved_set)
    
if __name__=="__main__":
    a=int(input("Enter the number of set: "))
    b=int(input("How many element are there in a set: "))
    print(calculate_set(generate_set(a,b)))


    





